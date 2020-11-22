# 나쁜 구현 예
import numpy as np
import matplotlib.pyplot as plt


def numerical_diff(f, x):
    h = 10e-50
    return (f(x+h) - f(x)) / h


def numerical_diff(f, x):
    h = 1e-4  # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)


def function_1(x):
    return 0.01*x**2 + 0.1*x


x = np.arange(0.0, 20.0, 0.1)  # 0에서 20까지 0.1간격의 배열 x를 만든다(20은 미포함).
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
# plt.show()

print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))
