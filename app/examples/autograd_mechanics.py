import torch

x = torch.randn(5, 5)
y = torch.randn(5, 5)
z = torch.randn((5, 5), requires_grad=True)
print(x)
print(x.requires_grad)
print(z.requires_grad)
