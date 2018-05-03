import torch


def test_grad():
    x = torch.tensor([[1, 1], [1, 1]], requires_grad=True)
    y = x + 1
    z = x + y
    s = z.sum()
    s.backward()
    print(y.grad)
    print(x.grad)
