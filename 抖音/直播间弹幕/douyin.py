import re
import gzip
import requests
import subprocess
from loguru import logger
from functools import partial
from websocket import WebSocketApp
from douyin_pb2 import PushFrame, Response, ChatMessage

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "__ac_nonce": "068930a7900de9821ef49"
}


def on_message(ws, message):
    """1.转换PushFrame"""
    frame = PushFrame()
    frame.ParseFromString(message)

    # 在此消息中存在payload这个key, 所对应的value需要进一步反序列化
    # print('frame消息:', frame)

    """2.根据Response + gzip解压数据，生成数据对"""
    source_bytes = gzip.decompress(frame.payload)
    response = Response()
    response.ParseFromString(source_bytes)

    # 在此消息中存在messages这个key, 其中包含method类型, WebcastChatMessage类型为弹幕消息
    # print('response消息:', response)

    """3.在接收消息的过程中需要将原始数据返回给服务器完成校验"""
    if response.need_ack:
        frame.payload_type = 'ack'
        frame.LogID = frame.LogID
        # frame.payload = response.internal_ext.encode('utf-8')  # 经过测试不向服务器推送不影响弹幕接收
        ws.send(frame.SerializeToString())  # 数据序列化后发送给服务器

    """4.读取所有的数据"""
    for item in response.messages:
        # print(item.method)

        # 判断是否是弹幕消息, 如果不是则略过
        if item.method != 'WebcastChatMessage':
            continue

        message = ChatMessage()
        message.ParseFromString(item.payload)
        info = f"[{message.user.nickName}]: {message.content}"
        logger.info(info)
        # print('弹幕消息:', info)


def on_error(ws, error):
    print(f"{ws} -> 发生错误: {error}")


def on_close(ws, close_status_code, close_msg):
    print(f"{ws} -> 连接关闭: 状态码={close_status_code}, 原因={close_msg}")


def on_open(ws):
    print(f"{ws} -> 连接已建立...")


def get_id_cookie(room_url):
    response = requests.get(room_url, headers=headers, cookies=cookies)
    room_id = re.findall(r'\\"roomId\\":\\"(\d+)\\"', response.text)[0]
    cookie = response.cookies.get_dict().get('ttwid')
    return room_id, cookie


def main():
    url = "https://live.douyin.com/646454278948"
    room_id, cookie = get_id_cookie(url)
    sign = execjs.compile(open('获取sign值.js', encoding='utf-8').read()).call('get_sign', room_id)
    # print(sign)

    # websocket请求
    wss_url = f'wss://webcast100-ws-web-lq.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.14-beta.0&update_version_code=1.0.14-beta.0&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/138.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=r-7535744996729707359_d-1_u-1_fh-7535744667671139855_t-1754552358705&internal_ext=internal_src:dim|wss_push_room_id:7535731753667939098|wss_push_did:7534719531689707046|first_req_ms:1754552358600|fetch_time:1754552358705|seq:1|wss_info:0-1754552358705-0-0|wrds_v:7535744975254850553&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7534719531689707046&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&insert_task_id=&live_reason=&room_id={room_id}&heartbeatDuration=0&signature={sign}'
    ws = WebSocketApp(
        url=wss_url,
        header=headers,
        cookie=f'ttwid={cookie}',
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.run_forever()


if __name__ == '__main__':
    main()
