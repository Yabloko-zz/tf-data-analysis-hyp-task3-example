import pandas as pd
import numpy as np


chat_id = 38897891 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    
    from scipy.stats import mannwhitneyu
    _, pval = mannwhitneyu(x, y, alternative='two-sided')
    res = pval < 0.03
    return res
