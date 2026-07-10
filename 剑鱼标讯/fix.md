## 修复记录：解密失败问题

### 问题现象
`demo.py` 能正常获取接口加密响应数据（`data`、`secretKey`），但调用 `node 剑鱼标讯.js` 解密时崩溃，`subprocess` 返回空 stdout。

### 根因
`剑鱼标讯.js` 第1行 `window = global` 写在 `require('jsencrypt')` 之前。

jsencrypt 是 webpack 打包的浏览器库，其 UMD wrapper 通过 `this` 引用全局上下文。`window = global` 的提前赋值污染了全局环境，导致 webpack bootstrap 内部的 `setTimeout` polyfill 初始化失败，整个 RSA 解密模块无法加载。

### 修复
将 `window = global` 移至 `require('jsencrypt')` 之后：

```diff
- window = global;
  const fs = require('fs');
  const crypto = require('crypto').webcrypto;
  const JSEncrypt = require('jsencrypt');
+ window = global;
```

### 解密流程
1. RSA 私钥解密 `secretKey` → 得到 16 字节 AES 密钥
2. Base64 解码 `data` → 前 16 字节为 CBC-IV，剩余为密文
3. AES-CBC(128) 解密 → 得到明文 JSON
