# README

## Conda environment

### Create environment

```shell
conda create --prefix ./.conda python=3.13.9
```

### List environment

```shell
conda env list
```

### Remove environment

```shell
conda deactivate
conda env remove -p ./.conda
conda env remove -p D:\dev\ai\Complete_AI_Engineer_Bootcamp\LLMEngineering\.conda
```

### Activate environment

```shell
conda activate ./.conda
```

### Install packages

```shell
pip install streamlit
```

```shell
pip freeze > requirements.txt
```

## Settings

### vscode

`.\.vscode\settings.json`

```json
{
    "editor.fontSize": 20,
    "python.defaultInterpreterPath": "${env:CONDA_PREFIX}\\python.exe",
    "python.condaPath": "C:\\Users\\zhili\\anaconda3\\Scripts\\conda.exe", // 确认此路径正确
    "python.terminal.activateEnvironment": true,
    "python.terminal.activateEnvInCurrentTerminal": true,
    // 修正终端配置（适配大多数 Windows 环境的 Conda）
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "args": [
                "-ExecutionPolicy",
                "ByPass",
                "-NoExit",
                "-Command",
                "& '${env:USERPROFILE}\\miniconda3\\Scripts\\Activate.ps1'",
                "; conda activate '${env:CONDA_PREFIX}'"
            ]
        },
        "Command Prompt": {
            "path": [
                "${env:windir}\\Sysnative\\cmd.exe",
                "${env:windir}\\System32\\cmd.exe"
            ],
            "args": [
                "/k",
                "C:\\Users\\zhili\\miniconda3\\Scripts\\activate.bat",
                "${env:CONDA_PREFIX}"
            ]
        }
    },
    "terminal.integrated.defaultProfile.windows": "Command Prompt", // 推荐先用 cmd 测试
    // 其他保持不变
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true
}
```

## git

### Create .gitignore file

Add to .gitignore
```shell
# .conda
.conda/

# secrets.toml
secrets.toml
```

```shell
git init
git add .

```
