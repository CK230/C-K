import numpy as np
import matplotlib.pyplot as plt

# TODO 1: 补全膜电位更新公式
def lif_step(v_prev, input_current, tau_m, dt, R=1.0, v_rest=0.0):
    # 根据公式: u(t+dt) = u(t) + (dt/tau_m) * (-(u(t)-v_rest) + R*I(t))
    return v_prev + (dt / tau_m) * (-(v_prev - v_rest) + R * input_current)

def simulate_lif_constant(current_value, tau_m=10.0, v_rest=0.0, v_reset=0.0, v_th=15.0, R=1.0, dt=0.05, time_window=100.0):
    time = np.arange(0, time_window + dt, dt)
    current = np.full_like(time, current_value)
    voltage = np.zeros_like(time)
    spikes = np.zeros_like(time)
    
    v = v_rest
    for i in range(1, len(time)):
        # 更新膜电位
        v = lif_step(v, current[i], tau_m, dt, R, v_rest)
        
        # TODO 2: 补全阈值判断逻辑
        if v >= v_th:
            spikes[i] = 1
            voltage[i] = v_th # 绘图时拉高到阈值线，体现脉冲发放
            v = v_reset       # 状态重置
        else:
            voltage[i] = v
            
    return time, current, voltage, spikes

# 实验参数
I_const = 20.0
tau_m = 10.0
V_th = 15.0
R = 2.0
dt = 0.05
time_window = 100.0

time, current, voltage, spikes = simulate_lif_constant(
    current_value=I_const, tau_m=tau_m, v_th=V_th, R=R, dt=dt, time_window=time_window
)

# 绘图
fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
axes[0].plot(time, current, color="tab:orange")
axes[0].set_title("Constant Input Current")
axes[0].set_ylabel("I(t)")
axes[0].grid(alpha=0.3)

axes[1].plot(time, voltage, color="tab:blue", label="membrane potential")
axes[1].axhline(V_th, color="tab:red", linestyle="--", label="threshold")
axes[1].set_title("LIF Membrane Potential under Constant Input")
axes[1].set_xlabel("Time (ms)")
axes[1].set_ylabel("V_m (mV)")
axes[1].grid(alpha=0.3)
axes[1].legend()

plt.tight_layout()
plt.show()