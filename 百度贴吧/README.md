## 百度贴吧帖子列表 — sign 逆向 & tbs 分析


```
POST https://tieba.baidu.com/c/f/frs/page_pc
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
```

### 逆向参数

- **sign** — 请求签名，JS 侧 MD5(key=value 排序拼接 + 固定盐值)，Node 实现见 `Sign生成.js`

### tbs 详解

#### 它是什么

tbs 是百度贴吧的 CSRF 令牌。与传统 CSRF 不同，它**不作为隐藏域嵌入 HTML**（贴吧是纯 SPA，HTML 里 `window.TBCONFIG = {"tbs": null}` 初始为空），而是通过 **API 动态获取**。

#### 获取方式

```
GET https://tieba.baidu.com/dc/common/tbs
→ {"tbs": "b4892d858e3682481784206798", "is_login": 0}
```

接口不需要登录态即可调用（`is_login=0`），每次新 Session 返回不同的值，同一 Session 内多次调用返回相同值。

#### 什么时候需要

| 操作类型 | 是否需要 tbs | 说明 |
|---------|-------------|------|
| 浏览帖子列表 (page_pc) | **不需要** | 不传也能正常返回数据 |
| 发帖 / 回复 / 点赞 / 关注 | **需要** | 写操作校验 CSRF |

tbs 的设计比传统框架更精细——"看帖不需要 token，写帖才要"。这符合 CSRF 的核心目的：防止攻击者冒用你的身份执行写操作，而不是防止读操作。

#### 为什么不是 HTML 嵌入

传统的 CSRF token 由服务端渲染到 `<form>` 隐藏域中。百度贴吧是 CSR 架构：

```
服务端返回:  <div id="app"></div>
             window.TBCONFIG = {"tbs": null}   ← 初始为 null
```

页面完全由客户端 JS 渲染，没有服务端 HTML 模板。所以 tbs 必须通过 API 下发。

#### 浏览器端完整链路

```
① HTML 加载:  window.TBCONFIG.tbs = null

② base.js 注册请求拦截器，所有非 GET 请求自动注入:
   e.data.tbs = e.data.tbs || e.tbs || Yt.tbs

③ GET /dc/common/tbs  →  拿到 tbs

④ POST /c/f/frs/page_pc  →  响应中返回 anti.tbs（与请求中的 tbs 值一致）

⑤ index.js:  Object(i.e)("tbs", n.anti.tbs)  →  写入全局 store  →  Yt.tbs 更新

⑥ 后续所有写操作自动携带该 tbs
```

#### 断点调试位置

在 Chrome DevTools Sources 面板可搜索以下标记打断点：

| 位置 | 文件 | 搜索关键词 |
|------|------|-----------|
| tbs 初始化为 null | HTML 内联脚本 | `window.TBCONFIG` |
| 请求拦截器自动注入 tbs | `base.8fc54b03.js` | `e.data.tbs = e.data.tbs` |
| 从响应中提取 tbs 并存入 store | `index.5431dd8c.js` | `Object(i.e)("tbs"` |
| GET /dc/common/tbs 发起处 | Network 面板筛选 `common/tbs` | — |
