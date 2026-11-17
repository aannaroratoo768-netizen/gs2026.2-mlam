# 03. TESTES DE HIPÓTESES PARA A MÉDIA
amostra_20 = var_estudo.sample(n=20, random_state=42)
t_stat_a, p_valor_a = stats.ttest_1samp(amostra_20, popmean=media_var, alternative='less')
print(f'Teste A (6% sig, n=20) - p-valor: {p_valor_a:.4f}')

amostra_25 = var_estudo.sample(n=25, random_state=42)
t_stat_b, p_valor_b = stats.ttest_1samp(amostra_25, popmean=media_var, alternative='greater')
print(f'Teste B (9% sig, n=25) - p-valor: {p_valor_b:.4f}')
