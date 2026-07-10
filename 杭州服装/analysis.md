## 分析记录：API 签名认证失败（2026-07-10）

### 现象
`demo.py` 请求 `https://newopenapiweb.17qcc.com/api/services/app/SearchFactory/GetPageList` 返回 403：

```json
{"Success":false, "Error":{"Code":403, "Message":"签名认证失败-1"}}
```

### 排查过程

1. **首页正常**：`https://hangzhou.qccqcc.com/` 返回 200，`qccppm` 变量存在（格式 `xxx|xxx|xxx`，3 段 pipe 分割）

2. **本地加密/解密正常**：JS 内部 `encrypt_payload` → `decrypt_response` 自成闭环，AES-CBC 加解密、RSA-SHA1 签名均能通过

3. **旧硬编码数据也失败**：`demo2.py` 中历史抓取的有效请求数据（修复编码后）同样返回 `-1`，说明服务端已整体拒绝旧版加密参数

4. **缺失 KM/Ver 字段**：`encrypt_payload` 不生成 `KM`、`Ver` 字段，demo2.py 中却有。补上后错误码从 `-0` 变为 `-1`（`-0` 为字段缺失，`-1` 为签名不匹配）

5. **对比当前网站 JS**：拉取 `https://j.17qcc.com/combo?font&config&encrypt&jq&cookie&global&merge&tj&recommend&t=0624`（149KB），搜索关键字段：

| 旧版字段 | 新版出现次数 |
|----------|:---:|
| `qccppm` | 0 |
| `Sign` | 0 |
| `Content` | 0 |
| `RsaPubAes` | 0 |
| `TimesTamp` | 0 |
| `SHA1withRSA` | 0 |
| `GetPageList` | 0 |

### 结论

**网站已完全替换加密/签名方案。** 旧版代码（`杭州服装.js` + `mod.js`）提取自旧网站 JS，与新算法不兼容。需要从当前 `combo?encrypt` 文件中重新逆向。

### 旧版加密流程（供参考）

```
qccppm = "32位AES密钥|16位IV|32位TimesTamp"

encrypt_payload:
  1. AES-CBC(Pkcs7) 加密请求 JSON → Content（hex）
  2. RSA-SHA1 签名 Content → Sign（base64）
  3. RSA-PublicKey 加密 AES 密钥 → RsaPubAes（base64）
  4. POST: {KM, Ver, Content, Sign, RsaPubAes, IV, TimesTamp}

decrypt_response:
  1. AES-CBC(Pkcs7) 解密响应 hex → JSON 明文
```

### 需要逆向的新版 JS

- URL：`https://j.17qcc.com/combo?font&config&encrypt&jq&cookie&global&merge&tj&recommend&t=0624`
- 文件已保存，高度混淆，需使用 JS 调试工具（Chrome DevTools overrides / Frida / 补环境）逆向
