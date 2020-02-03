#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###########################
### The puZZle in a Mug ###
###########################

# importing the libraries
import scipy.stats as stats
import numpy as np

# Adding the data
y = np.array([1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568])

# Calculating the required values
media = np.mean(y)
std = np.std(y, ddof=1)

# Checking the critical value of the Kolmogorov-Smirnov test
def kolmogorov_smirnov_critico(n):
    # table of critical values for the kolmogorov-smirnov test - 95% confidence
    # Source: https://www.soest.hawaii.edu/GG/FACULTY/ITO/GG413/K_S_Table_one_Sample.pdf
    # Source: http://www.real-statistics.com/statistics-tables/kolmogorov-smirnov-table/
    # alpha = 0.05 (95% confidential level)
    
    if n <= 40:
        # valores entre 1 e 40
        kolmogorov_critico = [0.97500, 0.84189, 0.70760, 0.62394, 0.56328, 0.51926, 0.48342, 0.45427, 0.43001, 0.40925, 
                      0.39122, 0.37543, 0.36143, 0.34890, 0.33760, 0.32733, 0.31796, 0.30936, 0.30143, 0.29408, 
                      0.28724, 0.28087, 0.27490, 0.26931, 0.26404, 0.25907, 0.25438, 0.24993, 0.24571, 0.24170, 
                      0.23788, 0.23424, 0.23076, 0.22743, 0.22425, 0.22119, 0.21826, 0.21544, 0.21273, 0.21012]
        ks_critico = kolmogorov_critico[n - 1]
    elif n > 40:
        # valores acima de 40:
        kolmogorov_critico = 1.36/(np.sqrt(n))
        ks_critico = kolmogorov_critico
    else:
        pass            
            
    return ks_critico

ks_critico = kolmogorov_smirnov_critico(len(y))

# Calculating the value of the Kolmogorov-Smirnov statistic for the data
ks_stat, ks_p_valor = stats.kstest(y, cdf='norm', args=(media, std), N = len(y))

language = "portugues"    
language = "english"  
    
if language == "english":
    print("The mean of the data is = " + str(media))    
    print("The standard deviation of the data is = " + str(std))    
    print("At 95% confidence level, the critical value of the Kolmogorov-Smirnov test is = " + str(ks_critico))
    print("The calculated value of the Kolmogorov-Smirnov test is = " + str(ks_stat))
    # Conclusion
    if ks_critico >= ks_stat:
        print("At 95% confidence level, we have NO evidence to reject the hypothesis of data normality, according to the Kolmogorov-Smirnov test")
    else:
        print("At 95% confidence level, we have evidence to reject the hypothesis of data normality, according to the Kolmogorov-Smirnov test")
        
elif language == "portugues":
    print("A media dos dados eh = " + str(media))    
    print("O desvio padrao dos dados eh = " + str(std))    
    print("Com 95% de confianca, o valor critico do teste de Kolmogorov-Smirnov eh de = " + str(ks_critico))
    print("O valor calculado do teste de Kolmogorov-Smirnov eh de = " + str(ks_stat))
    # Conclusion
    if ks_critico >= ks_stat:
        print("Com 95% de confianca, não temos evidências para rejeitar a hipótese de normalidade dos dados, segundo o teste de Kolmogorov-Smirnov")
    else:
        print("Com 95% de confianca, temos evidências para rejeitar a hipótese de normalidade dos dados, segundo o teste de Kolmogorov-Smirnov")
else:
    print("Unsupported language")

