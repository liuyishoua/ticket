# 独立 Web 服务运行

本仓库从 Bifrost 的 applications/ticket 提取，Web 和票务引擎源码保持一致。
不依赖门户登录、平台虚拟环境或前端构建，不复制原服务数据。

推荐 `python3 start.py`，首次自动创建 .venv 并安装 requirements.txt，之后启动 Web 服务。
使用 `--no-browser` 禁止尝试打开浏览器，`--port 8877` 修改端口，
`--data-dir /absolute/path` 使用独立数据目录，`--setup-only` 仅安装依赖。

已有 Python 环境时可直接安装依赖后运行 `python -m web`。
服务默认监听 127.0.0.1:8767；没有单独的控制台登录，真实业务操作需要扫码绑定12306账号。
默认数据目录 .runtime_web；其中含会话凭证和业务信息，不提交 Git。

同一数据目录只运行一个服务。停止服务后再备份整个 .runtime_web，避免漏掉会话文件和 SQLite 数据。
预约执行要求服务持续运行；恢复已有数据时沿用原程序的预约恢复规则。

原桌面程序、命令行入口、测试和图片都保留，桌面运行细节见 README_GUI.md。
原 README 保存在 README_DESKTOP.md，里面的 Windows 发布产物不是本独立仓库已经发布的文件。
app.yaml 和 package.yaml 仍是来源项目的 Bifrost 接入配置，独立 Web 启动不使用它们。

## 离线回归

```bash
.venv/bin/python -m pip install pytest==9.1.1
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 .venv/bin/python -m pytest -q web/tests
.venv/bin/python -m unittest web.test_manifest_contract
node --check web/static/app.js
node --check web/static/rules.js
```

测试使用临时数据和模拟响应；本次提取不使用真实账号、不提交真实订单。
Qt 桌面测试需要另外安装 requirements-dev.txt，并具备相应图形环境。

## 提取验证记录

2026-10-05：全新虚拟环境安装 requirements.txt 成功，pip check 通过。
11项原有Web pytest测试和1项manifest unittest通过，前端JS和启动脚本语法检查通过。
独立临时数据目录的一键启动成功；首页、就绪探测、状态、站点及静态资源返回200。
浏览器初始页面与账号管理页面未出现脚本错误，截图保存在docs/images。
对照源目录，Web、票务引擎、桌面程序和原有测试文件均未改动。
未进行真实账号扫码、查票或下单，未构建Windows桌面发行包。
