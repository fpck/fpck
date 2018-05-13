import torch

x = torch.randn(5, 5)
y = torch.randn(5, 5)
z = torch.randn((5, 5), requires_grad=True)
a = x + y
b = a + z
print(x)
print(type(x))
print(type(y))
print(type(a))
print(type(b))
print(x.requires_grad)
print(z.requires_grad)
print(b.requires_grad)
