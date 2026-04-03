import numpy as np
import matplotlib.pyplot as plt

def lif_step(v_prev, input_current, tau_m, dt, R=1.0, v_rest=0.0):
    return v_prev + dt / tau_m * (-(v_prev - v_rest) + R * input_current)

def simulate_lif_constant(current_value, tau_m=10.0, v_rest=0.0, v_reset=0.0, v_th=15.0, R=1.0, dt=0.02, time_window=1000.0):
    time = np.arange(0, time_window + dt, dt)
    spike_count = 0
    v = v_rest
    for i in range(1, len(time)):
        v = lif_step(v, current_value, tau_m, dt, R, v_rest)
        if v >= v_th:
            spike_count += 1
            v = v_reset
    # 计算平均发放频率 (Hz) = 发放次数 / (总时长/1000)
    return spike_count / (time_window / 1000.0)

# TODO 3: 补全理论发放频率函数
def theoretical_firing_rate(I, tau_m=10.0, v_th=15.0, R=1.0):
    # 1. 判断是否能够达到阈值 (RI > V_th)
    if R * I <= v_th:
        return 0.0
    # 2. 计算周期 T = tau_m * ln(RI / (RI - V_th))
    T = tau_m * np.log((R * I) / (R * I - v_th))
    # 3. 计算频率 f = 1000 / T (单位 Hz)
    return 1000.0 / T

# 实验参数
tau_m, V_th, R, dt = 10.0, 15.0, 1.0, 0.02
I_values = np.arange(10, 31, 2)
time_window = 1000.0

theory_rates = [theoretical_firing_rate(I, tau_m, V_th, R) for I in I_values]
sim_rates = [simulate_lif_constant(I, tau_m=tau_m, v_th=V_th, R=R, dt=dt, time_window=time_window) for I in I_values]

# 绘图对照
plt.figure(figsize=(8, 5))
plt.plot(I_values, theory_rates, marker="o", label="theory")
plt.plot(I_values, sim_rates, marker="s", linestyle="--", label="simulation")
plt.xlabel("Input Current I")
plt.ylabel("Firing Rate (Hz)")
plt.title("Theoretical vs Simulated Firing Rate of LIF")
plt.grid(alpha=0.3)
plt.legend()
plt.show()