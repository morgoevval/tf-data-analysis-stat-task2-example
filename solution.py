import pandas as pd
import numpy as np
import scipy as scipy

from scipy.stats import norm


chat_id = 465374385 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = p
    p_values = x
    loc = x.mean()
    b_max = np.max(p_values)
    z = 0
    if alpha > 0 and alpha < 1:
        z = np.abs(np.round(scipy.stats.norm.ppf((1 - alpha) / 2), 2))
    left_bound = b_max
    right_bound = b_max + z * ((b_max - 0.083) / 2)
    return left_bound, right_bound
