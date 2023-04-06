import pandas as pd
import numpy as np

chat_id = 465374385 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    confidence_level = p
    alpha_values = x
    
    quantiles = np.quantile(alpha_values, [1 - confidence_level, confidence_level])
    # Определение левой и правой границы доверительного интервала
    left_boundary = 2 * alpha_values.max() - quantiles[0]
    right_boundary = quantiles[1]
    return right_boundary, left_boundary
