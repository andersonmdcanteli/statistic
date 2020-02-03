#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###########################
### The puZZle in a Mug ###
###########################

# importing the libraries
import scipy.stats as stats

# Adding the data
y = [1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 3.15435, 2.61826, 1.98492, 1.42738, 1.99568]

# Calculating the Shapiro-Wilk test
shapiro_stat, shapiro_p_valor = stats.shapiro(y)

language = "portugues"    
language = "english"  

# Conclusion
if language == "english":
    print("The calculated value for the Shapiro-Wilk test is = " + str(shapiro_stat))
    print("The calculated p-value of the Shapiro-Wilk test is = " + str(shapiro_p_valor))
    # Conclusion
    if shapiro_p_valor >= 0.05:
        print("At 95% confidence level, we have NO evidence to reject the hypothesis of data normality, according to the Shapiro-Wilk test")
    else:
        print("At 95% confidence level, we have evidence to reject the hypothesis of data normality, according to the Shapiro-Wilk test")
        
elif language == "portugues":
    print("O valor calculado do teste de Shapiro-Wilk eh de = " + str(shapiro_stat))
    print("O p-valor calculado para o teste de Shapiro-Wilk eh de = " + str(shapiro_p_valor))
    # Conclusion
    if shapiro_p_valor >= 0.05:
        print("Com 95% de confianca, não temos evidências para rejeitar a hipótese de normalidade dos dados, segundo o teste de Shapiro-Wilk")
    else:
        print("Com 95% de confianca, temos evidências para rejeitar a hipótese de normalidade dos dados, segundo o teste de Shapiro-Wilk")
else:
    print("Unsupported language")

