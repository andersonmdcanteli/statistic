import numpy as np
from scipy import stats

def pearson_r_test(r_pearson, size, rho=0.0, alpha=0.05):
    """Verifica se o coeficiente de correlação (r de Pearson) é igual a um valor pré-estabelecido.

    Parameters
    ----------
    r_pearson : `float`
        O coeficiente de correlação de Pearson
    size : `int`
        O número de amostras utilizadas para estimar `r_pearson`
    rho : `int`r `float`, default = `0.0`
        O valor esperado para o coeficient de correlação populacional
    alpha : `float`
        O nível de signficiância adotado

    Returns
    -------
    Z_0 : `float`
        A estatística do teste
    z_critical : `float`
        O valor crítico bilateral da distribuição Normal para alpha
    result : `str`
        A descrição do resultado do teste
    alpha : `float`
        O nível de significância adotado

    Notes
    -----

    A estatística do teste pode ser estimada da seguinte forma:

    .. math::

        Z_0 = (arctanh \\; (r) - arctanh \\; (\\rho_0)) \\sqrt{n-3}

    onde :math:`\\rho_0` é o valor esperado para o coeficiente de correlação. As hipóteses para este caso são:



    .. admonition:: \u2615

       :math:`H_0: \\; \\rho = \\rho_0`;

       :math:`H_1: \\; \\rho  \\neq \\rho_0`.

    Os valores críticos são obtidos da distribuição Normal padrão bilateral :math:`Z_{1-\\alpha/2}`, utilizando a função `stats.norm.ppf()`. Podemos então concluir o teste da seguinte forma:


    .. admonition:: \u2615

       Se :math:`|Z_0| > Z_{1-\\alpha/2}`, temos evidências para rejeitar a hipótese nula, e :math:`\\rho \\neq \\rho_0`;

       Se :math:`|Z_0| \\leq Z_{1-\\alpha/2}`, não temos evidências para rejeitar a hipótese nula, e :math:`\\rho = \\rho_0`;

       :math:`H_1: \\; \\rho  \\neq \\rho_0`.


    Examples
    --------

    >>> import numpy as np
    >>> from scipy import stats
    >>> r_pearson = 0.960
    >>> size = 30
    >>> alpha = 0.05
    >>> result = pearson_test(0.96, 30, rho=0, alpha=0.05)
    >>> print(result)
    
    (2.7519325239534744,
     1.959963984540054,
     'Rejeita H0, e o coeficiente de Pearson é diferente de 0 (com 95.0% de confiança).',
     0.05)

    """
    # calculando a estatística do teste
    Z_0 = (np.arctanh(r_pearson) - np.arctanh(rho))*np.sqrt((n_size - 3))
    # calculando o valor crítico
    z_critical = stats.norm.ppf(1 - alpha/2)
    # concluindo o teste
    if np.abs(Z_0) > z_critical:
        result = f"Rejeita H0, e o coeficiente de Pearson é diferente de {rho} (com {100*(1-alpha)}% de confiança)."
    else:
        result = f"Falhar em rejeitar H0, e o coeficiente de Pearson é igual a {rho} (com {100*(1-alpha)}% de confiança)."


    return Z_0, z_critical, result, alpha





def pearson_r_ci(r_pearson, n_size, alpha=0.05):
    """Estima o intervalo de confiança do coeficiente de correlação (r de Pearson).

    Parameters
    ----------
    r_pearson : `float`
        O coeficiente de correlação de Pearson
    size : `int`
        O número de amostras utilizadas para estimar `r_pearson`
    alpha : `float`
        O nível de signficiância adotado

    Returns
    -------
    result : `str`
        O resultado textual do intervalo de confiança estimado
    ci_lower : `float`
        O limite inferior do coeficiente de correlação
    r_pearson : `float`
        O o coeficiente de correlação fornecido
    ci_uper : `str`
        O limite superior do coeficiente de correlação
    alpha : `float`
        O nível de significância adotado


     Notes
    -----

    Os limites de confiança são estimados utilizando a transformação `Fisher z-transformation`. O intervalo é estimado na variável transformada, admitindo distribuição Normal, e então transformado de volta para a escala original.

    O limite inferior é estimado através da seguinte relação:
    
    .. math::

        LI_{pearson} = \\tanh{\\left(arctahnh \\; \\left(r_{pearson}\\right) - \\frac{Z_{1-\\alpha/2 }}{\\sqrt{n-3}}\\right)}
        
    O limite superior é estimado através da relação:
    
    .. math::
    
        LS_{pearson} = \\tanh{\\left(arctahnh \\; \\left(r_{pearson}\\right) + \\frac{Z_{1-\\alpha/2 }}{\\sqrt{n-3}}\\right)}

    
    onde :math:`Z_{1-\\alpha/2}` é o valor crítico da distribuição Normal padrão bilateral, que é obtido da função `stats.norm.ppf()`.


    Examples
    --------

    >>> import numpy as np
    >>> from scipy import stats
    >>> result = pearson_r_ci(r_pearson=0.960, n_size=30, alpha=0.05)
    >>> print(result)
    
    ('0.9168 <= 0.96 <= 0.981 (com 95.0% de confiança).',
     0.9168211081976101,
     0.96,
     0.980986684724545,
     0.05)   
       
       

    """
    
    # obtendo a média do r-pearson na escala transformada
    r_pearson_z_scale = np.arctanh(r_pearson)
    
    # critical value
    ic_z_scale = stats.norm.ppf(1 - alpha/2)/np.sqrt(n_size-3)
    
    # ic values in z scale
    ic_lower_z_scale = r_pearson_z_scale - ic_z_scale
    ic_upper_z_scale = r_pearson_z_scale + ic_z_scale
    
    # transformando para a escala original
    ci_lower = np.tanh(ic_lower_z_scale)
    ci_upper = np.tanh(ic_upper_z_scale)
    
    result = f"{round(ci_lower, 4)} <= {round(r_pearson, 4)} <= {round(ci_upper, 4)} (com {100*(1-alpha)}% de confiança)."
    
    return result, ci_lower, r_pearson, ci_upper, alpha