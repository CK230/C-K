import numpy as np


def mp_neuron(inputs, weights, threshold):
    weighted_sum = np.dot(inputs, weights)
    output = 1 if weighted_sum >= threshold else 0
    return weighted_sum, output


# 可以自行修改的参数 
weights = np.array([0.7, 0.6, -0.5]) 
threshold = 2.0

# 样例 1：可以超过阈值
inputs_a = np.array([1.0, 1.0, 0.0])

# 样例 2：不能超过阈值
inputs_b = np.array([1.0, 0.0, 1.0])

sum_a, output_a = mp_neuron(inputs_a, weights, threshold)
sum_b, output_b = mp_neuron(inputs_b, weights, threshold)

print("------ M-P 神经元实验 ------")
print("权重:", weights)
print("阈值:", threshold)
print()

print("样例 1输入:", inputs_a)
print("样例 1加权和:", round(sum_a, 3))
print("样例 1输出:", output_a)
print()

print("样例 2输入:", inputs_b)
print("样例 2加权和:", round(sum_b, 3))
print("样例 2输出:", output_b)
