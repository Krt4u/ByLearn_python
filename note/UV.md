https://uv.doczh.com/getting-started/installation/#cargo

uv工具包的基本使用

简单介绍：因为在python中，不同项目以来的库可能不同，或版本不同，若每个库都装在全局依赖中，会导致冲突，因此出现了uv

uv可以为每个工作区创建虚拟环境，在虚拟环境中安装依赖包，不影响其他工作区，以此来隔离各项目之间的依赖

配置并使用了虚拟环境后，系统默认还是使用python运行py文件，需要 .\.venv\Scripts\activate 更改为优先使用虚拟环境中的

使用：
uv 更新：pip install --upgrade uv
从系统中卸载uv：
uv cache clean
rm -r "$(uv python dir)"
rm -r "$(uv tool dir)"
$ rm $HOME\.local\bin\uv.exe
$ rm $HOME\.local\bin\uvx.exe
项目管理
创建和开发带有 pyproject.toml 的 Python 项目。
uv init: 创建新 Python 项目
uv add: 为项目添加依赖 --dev 参数指定该下载的包在项目打包时忽略
uv remove: 从项目移除依赖
uv sync: 同步项目依赖到环境
uv lock: 为项目依赖创建锁文件
uv run: 在项目环境中运行命令
uv tree: 查看项目依赖树
uv build: 构建项目为分发包
uv publish: 发布项目到包索引
参考 项目管理指南 开始使用。
工具
运行和安装发布到 Python 包索引的工具，例如 ruff 或 black。，不是项目的一部分，。不参与打包
uvx / uv tool run: 在临时环境中运行工具
uv tool install: 为用户全局安装工具
uv tool uninstall: 卸载工具
uv tool list: 列出已安装的工具
uv tool update-shell: 更新 shell 以包含工具可执行文件
实用工具
管理和检查 uv 的状态，例如缓存、存储目录或执行自我更新：
uv cache clean: 清除缓存条目
uv cache prune: 清除过期的缓存条目
uv cache dir: 显示 uv 缓存目录路径
uv tool dir: 显示 uv 工具目录路径
uv python dir: 显示 uv 安装的 Python 版本路径
uv self update: 将 uv 更新至最新版本