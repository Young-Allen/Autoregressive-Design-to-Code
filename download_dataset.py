from huggingface_hub import snapshot_download

target_dir = "/mnt/d/datasets/WebSight"  # 你想放的目录（仓库文件会在这里可见）

snapshot_download(
    repo_id="HuggingFaceM4/WebSight",
    repo_type="dataset",
    local_dir=target_dir,
    local_dir_use_symlinks=False,  # 重要：确保是真实文件复制到目标目录，而不是指向cache的软链接
)
print("Downloaded to:", target_dir)