- 网站地址：https://etax.ningbo.chinatax.gov.cn:8443
- 逆向类型：Cookie 反爬（瑞数类动态验证）
- 逆向参数：响应 Cookie

流程：

1. 首次请求首页 → 返回加密 HTML，内嵌一段加密 JS + meta 密钥
2. 提取 `<meta id="HRHkMu6mGL8x">` 的 content（参与解密的 key）
3. 提取页面内联加密 JS + 外部解密 JS
4. 在 Node.js 中补浏览器环境（mod.js），执行解密 JS
5. 解密后的 JS 动态计算出合法 Cookie（`document.cookie`）
6. 携带该 Cookie 再次请求首页 → 通过验证，拿到真实页面

## 无限 debugger 问题

该网站在浏览器中调试时会触发无限 debugger，常见的 hook 方案不可用。

原因：0xsdeo 分析认为是 eval 作用域问题导致常规 bypass 方式报错，详见 http://antidebug-breaker.com/scripts/antidebug/bypass-debugger/#eval作用域问题导致报错。

解决方案：使用 [YSbrowser](https://github.com/selfshore/YSbrowser)（群友 蛋蛋 提供），该浏览器内置反反调试能力，不会触发该网站的无限 debugger。
