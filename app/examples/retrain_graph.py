import torch
a = torch.ones((1, 4), requires_grad=True)
b = a**2
c = b*2
d = c.mean()
e = c.sum()
f = d + e

d.backward(retain_graph=True)
print(a.grad)
a.grad.zero_()
e.backward(retain_graph=True)
print(a.grad)
a.grad.zero_()
e.backward()
print(a.grad)
