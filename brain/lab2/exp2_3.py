import numpy as np
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False     # 解决保存图像是负号'-'显示为方块的问题

def add_wave(response, wave, start_time):
    for k, value in enumerate(wave):
        if start_time + k < len(response):
            response[start_time + k] += value


T = 20
time = np.arange(T)

# 可以自行修改的参数
epsp = np.array([0.8, 0.4, 0.2])
ipsp = np.array([-0.7, -0.4, -0.2])
threshold = 0.7

# 输入时刻
exc_times = [2, 6, 7, 12, 13]
inh_times = [13]

response = np.zeros(T)

for t0 in exc_times:
    add_wave(response, epsp, t0)

for t0 in inh_times:
    add_wave(response, ipsp, t0)

output = (response >= threshold).astype(int)

exc_idx = np.array(exc_times)
inh_idx = np.array(inh_times)
tick_positions = np.arange(0, T, 2)

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

axes[0].stem(
    exc_idx,
    np.ones(len(exc_idx)),
    linefmt="tab:blue",
    markerfmt="bo",
    basefmt=" ",
)
if len(inh_idx) > 0:
    axes[0].stem(
        inh_idx,
        -np.ones(len(inh_idx)),
        linefmt="tab:red",
        markerfmt="ro",
        basefmt=" ",
    )
axes[0].set_title("输入事件时刻（蓝色为兴奋输入，红色为抑制输入）")
axes[0].set_ylabel("event")
axes[0].grid(alpha=0.3)

axes[1].plot(time, response, marker="o", label="总响应 response", color="tab:purple")
axes[1].axhline(threshold, color="tab:green", linestyle="--", label="threshold")
axes[1].step(time, output, where="mid", label="二值输出 output", color="tab:orange")
axes[1].set_title("EPSP/IPSP 叠加后的总响应")
axes[1].set_xlabel("time step")
axes[1].set_ylabel("response")
axes[1].set_xticks(tick_positions)
axes[1].set_xlim(-0.5, T - 0.5)
axes[1].grid(alpha=0.3)
axes[1].legend()

plt.tight_layout()
plt.show()
