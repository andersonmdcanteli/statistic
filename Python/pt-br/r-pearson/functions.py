import numpy as np
from scipy.stats import norm

def pearson_test(r_pearson, size, rho=0.0, alfa=0.05):
    """Verifica se o coeficiente de correlação (r de Pearson) é igual a um valor pré-estabelecido.

    Parameters
    ----------
    r_pearson : `float`
        O coeficiente de correlação de Pearson
    size : `int`
        O número de amostras utilizadas para estimar `r_pearson`
    rho : `int`r `float`, default = `0.0`
        O valor esperado para o coeficient de correlação populacional
    alfa : `float`
        O nível de signficiância adotado

    Returns
    -------
    Z_0 : `float`
        A estatística do teste
    z_critical : `float`
        O valor crítico bilateral da distribuição Normal para alfa
    result : `str`
        A descrição do resultado do teste
    alfa : `float`
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
    >>> alfa = 0.05
    >>> result = pearson_test(0.96, 30, rho=0, alfa=0.05)
    >>> print(result)
    
    (2.7519325239534744,
     1.959963984540054,
     'Rejeita H0, e o coeficiente de Pearson é diferente de 0 (com 95.0% de confiança).',
     0.05)

    """
    # calculando a estatística do teste
    Z_0 = (np.arctanh(r_pearson) - np.arctanh(rho))*np.sqrt((n_size - 3))
    # calculando o valor crítico
    z_critical = norm.ppf(1 - alfa/2)
    # concluindo o teste
    if np.abs(Z_0) > z_critical:
        result = f"Rejeita H0, e o coeficiente de Pearson é diferente de {rho} (com {100*(1-alfa)}% de confiança)."
    else:
        result = f"Falhar em rejeitar H0, e o coeficiente de Pearson é igual a {rho} (com {100*(1-alfa)}% de confiança)."


    return Z_0, z_critical, result, alfa



