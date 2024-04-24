import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.integrate import quad

def load_data():
    file1 = 'inter_date_num.txt'
    data1 = pd.read_csv(file1, delimiter=' ', header=None, names=['X', 'Y'])
    sub_time = [int(x) for x in data1['X']]
    sub_cnt = [int(y) for y in data1['Y']]
    file2 = 'date_type.txt'
    data2 = pd.read_csv(file2, delimiter=',', header=None, names=['X', 'Y'])
    event_time = [int(x) for x in data2['X']]
    event_type = [int(y) for y in data2['Y']]
    return sub_time, sub_cnt, event_time, event_type

def pharmacokinetic_model(t, K0, V_abs, V_el):
    if abs(V_el - V_abs) <= 0.01:
        return 0
    return K0 * (V_abs / (V_el - V_abs)) * (np.exp(-V_abs * t) - np.exp(-V_el * t))

def get_parameters():
    sub_time, sub_cnt, event_time, event_type = load_data()
    num_event_types = len(set(event_type))
    initial_params = np.random.rand(num_event_types * 3)
    initial_params[:num_event_types] *= 100
    initial_params[num_event_types:2*num_event_types] *= 1.7
    initial_params[num_event_types:2*num_event_types] += 0.3
    initial_params[2*num_event_types:] *= 1.85
    initial_params[2*num_event_types:] += 0.15
    bounds = [(0, 100)] * num_event_types + [(0.3, 2)] * num_event_types + [(0.15, 2)] * num_event_types

    def loss_function(params):
        K0s = params[:num_event_types]
        V_abss = params[num_event_types:2*num_event_types]
        V_els = params[2*num_event_types:3*num_event_types]
        total_subscribers = np.zeros(len(sub_time)) + sub_cnt[0]

        start = sub_time[0]
        for i, sub_day in enumerate(sub_time):
            total_effect = 0
            for j, (ed, et) in enumerate(zip(event_time, event_type)):
                if ed < start:
                    continue
                K0 = K0s[et - 1]
                V_abs = V_abss[et - 1]
                V_el = V_els[et - 1]
                if sub_day >= ed:
                    effect = pharmacokinetic_model((sub_day - ed)//86400, K0, V_abs, V_el)
                    #effect, error = quad(
                        #lambda t, K0=K0, V_abs=V_abs, V_el=V_el: pharmacokinetic_model(t, K0, V_abs, V_el), 0,(sub_day - ed)//86400)
                    total_effect += effect
            total_subscribers[i] += total_effect
        return np.sum((total_subscribers - sub_cnt) ** 2)

    result = minimize(loss_function, initial_params, method='TNC', bounds=bounds)
    return result.x[:num_event_types], result.x[num_event_types:2*num_event_types], result.x[2*num_event_types:], sub_time, event_time, event_type

K0_params, V_abs_params, V_el_params, sub_time, event_time, event_type = get_parameters()
print("Optimized parameters for each event type:")
for i in range(len(K0_params)):
    print(f"Event type {i+1}: K0 = {K0_params[i]:.2f}, V_abs = {V_abs_params[i]:.2f}, V_el = {V_el_params[i]:.2f}")

integrals = []
for i in range(len(K0_params)):
    integral, error = quad(lambda t, K0=K0_params[i], V_abs=V_abs_params[i], V_el=V_el_params[i]: pharmacokinetic_model(t, K0, V_abs, V_el), 0, np.inf)
    integrals.append((i + 1, integral))

for idx, val in integrals:
    print(f"Integral for event type {idx}: {val:.2f}")

def get_coefficients():
    return integrals
