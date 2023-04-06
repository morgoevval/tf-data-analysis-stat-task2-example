import pandas as pd
import numpy as np

chat_id = 465374385 # Ваш chat ID, не меняйте название переменной
def solution(alpha, p_values):
    # Вычисляем эмпирический квантиль уровня доверия
    q = np.quantile(p_values, alpha)
    # Вычисляем доверительный интервал
    confidence_interval = [0.083, q]
    return confidence_interval[0], confidence_interval[1]
