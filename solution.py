import pandas as pd
import numpy as np


chat_id = 38897891 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    
    from scipy.stats import ttest_ind
    st, pval = ttest_ind(a=x, b=y, equal_var=True)
    res = pval <= 0.05
    return res
