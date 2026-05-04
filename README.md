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

## git

### Create .gitignore file

Add to .gitignore

```shell
# .conda
.conda/

# secrets.toml
secrets.toml
```

### Using git

```shell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/BenZHONG/interview-tool.git
git push -u origin main
```

## Deploying the Streamlit App

[https://share.streamlit.io/](https://share.streamlit.io/)
