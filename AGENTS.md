# Ticket 独立仓库

本仓库提取自 bifrost/applications/ticket。Web 和票务引擎保持来源项目行为。

- 启动：python3 start.py；已有依赖时 python -m web。端口20002，数据目录.runtime_web。
- Web 没有演示模式参数；本机独立页面不另设密码；正式 HTTPS 入口先验证统一账号及应用授权，真实业务仍需扫码绑定12306账号。
- 不启动真实订单、扫码或查询进行自动化验收；临时数据和模拟响应用于测试。
- 不提交Cookie、Token、二维码、证件信息、会话文件、数据库或日志。
- LICENSE 与 Bifrost 一致；THIRD_PARTY_NOTICES.md 保留原依赖许可声明。
- 独立启动不使用 app.yaml / package.yaml 中依赖 Bifrost 的相对路径。
- Web 验证：pytest web/tests；unittest web.test_manifest_contract；node --check web/static/app.js 与 rules.js。
- 原桌面说明在 README_DESKTOP.md、README_GUI.md；不得把旧 Release 说明当成本仓库已发布产物。
- 按任务范围修改，保留业务、来源声明与用户现有数据。
