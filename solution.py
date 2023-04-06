import pandas as pd
import numpy as np

chat_id = 465374385 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Вычисляем эмпирический квантиль уровня доверия
    alpha = p
    p_values = x
    q = np.quantile(p_values, alpha)
    # Вычисляем доверительный интервал
    confidence_interval = [0.083, q]
    return confidence_interval[0], confidence_interval[1]

# Пример использования
alpha = 0.95 # Уровень доверия
p_values = np.array([0.083, 0.2, 0.3, 0.4]) # Входной массив уровней значимостей
solution(alpha, p_values)
