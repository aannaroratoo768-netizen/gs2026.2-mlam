# 04. ANÁLISE BIVARIADA E REGRESSÃO LINEAR SIMPLES
taxa_de_inflacao = pd.Series(np.random.rand(100) * 100)
variacao_do_pib_trimestral = 2 * taxa_de_inflacao + np.random.normal(0, 10, 100)

plt.figure(figsize=(6,4))
sns.scatterplot(x=taxa_de_inflacao, y=variacao_do_pib_trimestral)
plt.title('Dispersão X vs Y')
plt.show()

taxa_de_inflacao_sm = sm.add_constant(taxa_de_inflacao)
modelo_rls = sm.OLS(variacao_do_pib_trimestral, taxa_de_inflacao_sm).fit()
print(modelo_rls.summary())
