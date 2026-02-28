from torchvision.datasets import FashionMNIST
from torchvision.transforms import ToTensor

FashionMNIST(
    root="data", #download dir
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=None,
)

FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
    target_transform=None
)