from torchvision.datasets import FashionMNIST
from torchvision.transforms import ToTensor

l_data=FashionMNIST(
    root="data", #download dir
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=None,
)

t_data=FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
    target_transform=None
)