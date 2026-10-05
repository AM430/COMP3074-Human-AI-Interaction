# COMP3074 Human-AI Interaction

独立 Python 3.12 环境，练习代码放在 `lab0/`。

在 VS Code 打开这个文件夹，按 Ctrl+Shift+P，选择 Python: Select Interpreter，选择 `.venv/Scripts/python.exe`。该设置文件提供默认路径，但已有 interpreter 选择可能需要手动更新。

## 创建环境的命令与目的

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install nltk beautifulsoup4
```

第一行建立 virtual environment；第二行用该环境的 Python 安装库。`python -m pip` 能确保安装目标和运行代码的 interpreter 一致。无需 activation 也能运行下面的命令。

## 验证与运行

```powershell
.\.venv\Scripts\python.exe check_environment.py
.\.venv\Scripts\python.exe lab0\exercise01.py
```

验证输出的 Interpreter 应位于本项目 `.venv` 内，Virtual environment 应为 True。

可选 activation：` .\.venv\Scripts\Activate.ps1 `。如果 PowerShell 阻止该脚本，直接使用上面的完整 Python 路径即可。

NLTK 库和 NLTK 数据资源是两回事。当前验证使用不需额外资源的 tokenizer。后续遇到 LookupError 时，按报错中的资源名称单独下载。spaCy 留到扩展练习需要时安装。

Exercise 1 的提示：`s[start:stop]` 包含 start，但不包含 stop；负索引从字符串末尾计数。先预测结果，再运行观察。只用切片与拼接完成转换，不用 replace 或正则表达式。

题目依据：用户提供的 COMP3074_Lab0__2025_.pdf，第 12 页；该材料标注 2025。
