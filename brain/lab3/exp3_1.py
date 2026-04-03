import numpy as np
import matplotlib.pyplot as plt

# HH 模型常用参数
C_m = 1.0
g_Na, g_K, g_L = 120.0, 36.0, 0.3
E_Na, E_K, E_L = 50.0, -77.0, -54.387
V_rest = -65.0

# 门控变量速率函数
def alpha_n(V):
    x = V + 55.0
    return 0.01 * x / (1 - np.exp(-x / 10)) if abs(x) > 1e-6 else 0.1

def beta_n(V):
    return 0.125 * np.exp(-(V + 65.0) / 80)

def alpha_m(V):
    x = V + 40.0
    return 0.1 * x / (1 - np.exp(-x / 10)) if abs(x) > 1e-6 else 1.0

def beta_m(V):
    return 4.0 * np.exp(-(V + 65.0) / 18)

def alpha_h(V):
    return 0.07 * np.exp(-(V + 65.0) / 20)

def beta_h(V):
    return 1.0 / (1 + np.exp(-(V + 35.0) / 10))

def external_current(t, amplitude=10.0, start=10.0, end=40.0):
    return amplitude if start <= t <= end else 0.0

# 实验参数 (根据PDF要求设置默认值)
stim_amplitude = 10.0   # 可修改：尝试 5.0, 10.0, 20.0
stim_start = 10.0
stim_end = 40.0
dt = 0.02
time_window = 60.0

# 初始值
m0 = alpha_m(V_rest) / (alpha_m(V_rest) + beta_m(V_rest))
h0 = alpha_h(V_rest) / (alpha_h(V_rest) + beta_h(V_rest))
n0 = alpha_n(V_rest) / (alpha_n(V_rest) + beta_n(V_rest))

time = np.arange(0, time_window + dt, dt)
current = np.array([external_current(t, stim_amplitude, stim_start, stim_end) for t in time])
voltage = np.zeros_like(time)
m_values, h_values, n_values = np.zeros_like(time), np.zeros_like(time), np.zeros_like(time)

voltage[0], m_values[0], h_values[0], n_values[0] = V_rest, m0, h0, n0

# 显式欧拉法仿真
for i in range(1, len(time)):
    V_prev = voltage[i - 1]
    m_prev, h_prev, n_prev = m_values[i-1], h_values[i-1], n_values[i-1]
    I_ext = current[i - 1]
    
    # 计算通道电流
    I_Na = g_Na * (m_prev ** 3) * h_prev * (V_prev - E_Na)
    I_K = g_K * (n_prev ** 4) * (V_prev - E_K)
    I_L = g_L * (V_prev - E_L)
    
    # 变量导数
    dVdt = (I_ext - I_Na - I_K - I_L) / C_m
    dmdt = alpha_m(V_prev) * (1 - m_prev) - beta_m(V_prev) * m_prev
    dhdt = alpha_h(V_prev) * (1 - h_prev) - beta_h(V_prev) * h_prev
    dndt = alpha_n(V_prev) * (1 - n_prev) - beta_n(V_prev) * n_prev
    
    # 更新
    voltage[i] = V_prev + dt * dVdt
    m_values[i] = m_prev + dt * dmdt
    h_values[i] = h_prev + dt * dhdt
    n_values[i] = n_prev + dt * dndt

# 绘图
fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
axes[0].plot(time, current, color="tab:orange")
axes[0].set_title("Input Current of HH Model")
axes[0].set_ylabel("I_ext (uA/cm2)")
axes[0].grid(alpha=0.3)

axes[1].plot(time, voltage, color="tab:blue")
axes[1].axhline(0.0, color="gray", linestyle="--", alpha=0.7, label="0 mV reference")
axes[1].set_title("Membrane Potential of HH Model")
axes[1].set_xlabel("Time (ms)")
axes[1].set_ylabel("V_m (mV)")
axes[1].grid(alpha=0.3)
axes[1].legend()

plt.tight_layout()
plt.show()