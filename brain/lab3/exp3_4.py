import numpy as np
import matplotlib.pyplot as plt

def lif_step(v_prev, input_current, tau_m, dt, R=1.0, v_rest=0.0):
    return v_prev + dt / tau_m * (-(v_prev - v_rest) + R * input_current)

def simulate_lif_periodic(base_current=15.0, amplitude=5.0, cycle_ms=20.0, tau_m=10.0, v_rest=0.0, v_reset=0.0, v_th=15.0, R=1.0, dt=0.1, time_window=100.0):
    time = np.arange(0, time_window + dt, dt)
    # 周期输入电流公式
    current = base_current + amplitude * np.cos(2 * np.pi * time / cycle_ms)
    voltage = np.zeros_like(time)
    
    v = v_rest
    for i in range(1, len(time)):
        v = lif_step(v, current[i], tau_m, dt, R, v_rest)
        if v >= v_th:
            voltage[i] = v_th
            v = v_reset
        else:
            voltage[i] = v
    return time, current, voltage

# 实验参数
# 注意：这里的键名必须与函数定义中的参数名完全一致（区分大小写）
params = {
    'base_current': 15.0,
    'amplitude': 5.0,
    'cycle_ms': 15.0,
    'v_th': 15.0,       # 已将 V_th 修改为 v_th 以匹配函数定义
    'time_window': 100.0
}

time, current, voltage = simulate_lif_periodic(**params)

# 绘图
fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
axes[0].plot(time, current, color="tab:orange")
axes[0].set_title("Periodic Input Current")
axes[0].set_ylabel("I(t)")
axes[0].grid(alpha=0.3)

axes[1].plot(time, voltage, color="tab:blue", label="membrane potential")
axes[1].axhline(params['v_th'], color="tab:red", linestyle="--", label="threshold")
axes[1].set_title("LIF Membrane Potential under Periodic Input")
axes[1].set_xlabel("Time (ms)")
axes[1].set_ylabel("V_m (mV)")
axes[1].grid(alpha=0.3)
axes[1].legend()

plt.tight_layout()
plt.show()