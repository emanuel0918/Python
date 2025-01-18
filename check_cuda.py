import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print("GPU detected!")
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Version: {torch.version.cuda}")
else:
    print("No GPU detected. Using CPU.")

# Check PyTorch version
print(f"PyTorch Version: {torch.__version__}")
