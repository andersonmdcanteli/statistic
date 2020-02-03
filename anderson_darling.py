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

# Calculating the Anderson-Darling test
ad_stat, ad_critico, ad_teorico = stats.anderson(y, 'norm')

language = "portugues"    
language = "english"  

# Conclusion
if language == "english":
    print("At " + str(100 - ad_teorico[2]) + "% confidence level, the statistic value of the Anderson-Darling test is = " + str(ad_critico[2]))
    print("The statistic value calculated for the Anderson-Darling test is = " + str(ad_stat))
    if ad_stat < ad_critico[2]:
        print("At " + str(100 - ad_teorico[2]) + "% confidence level, we have NO evidence to reject the hypothesis of data normality, according to the Anderson-Darling test")
    else:
        print("At " + str(100 - ad_teorico[2]) + "% confidence level, we have evidence to reject the hypothesis of data normality, according to the Anderson-Darling test")

elif language == "portugues":
    print("Com " + str(100 - ad_teorico[2]) + "% de confianca, o valor teorico do teste de Anderson-Darling eh = " + str(ad_critico[2]))
    print("O valor calculado para a estatistica do teste de Anderson-Darling eh = " + str(ad_stat))
    if ad_stat < ad_critico[2]:
        print("Com " + str(100 - ad_teorico[2]) + "% de confianca, não temos evidências para rejeitar a hipótese de normalidade dos dados, segundo o teste de Anderson-Darling")
    else:
        print("Com " + str(100 - ad_teorico[2]) + "% de confianca, temos evidências para rejeitar a hipótese de normalidade dos dados, segundo o teste de Anderson-Darling")        
else:
    print("Unsupported language")

