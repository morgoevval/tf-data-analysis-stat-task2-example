import pandas as pd
import numpy as np

chat_id = 465374385 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = p
    p_values = x
    q = np.quantile(p_values, alpha)
    confidence_interval = [0.083, q]
    return confidence_interval[0], confidence_interval[1]
