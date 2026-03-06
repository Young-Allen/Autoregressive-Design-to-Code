import os

# 设置环境变量
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# 下载模型
os.system('huggingface-cli download --resume-download Qwen/Qwen3-Coder-30B-A3B-Instruct --local-dir /mnt/d/models/Qwen3-Coder-30B-A3B-Instruct')