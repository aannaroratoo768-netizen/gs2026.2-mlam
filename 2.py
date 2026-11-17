taxas_desemprego_ibge = [11.2, 10.5, 9.8, 8.9, 8.0, 7.5, 7.1, 7.4, 7.8, 8.1, 7.6, 6.9]

var_estudo = pd.Series(taxas_desemprego_ibge) 

media_var, desvio_var, mediana_var = var_estudo.mean(), var_estudo.std(), var_estudo.median()

print(f'Média: {media_var:.2f}% | Desvio Padrão: {desvio_var:.2f}% | Mediana: {mediana_var:.2f}%')

prob_menor_media = stats.norm.cdf(media_var, loc=media_var, scale=desvio_var)
print(f'Probabilidade (Taxa < média): {prob_menor_media:.4f}')

prob_maior_mediana = 1 - stats.norm.cdf(mediana_var, loc=media_var, scale=desvio_var)
print(f'Probabilidade (Taxa > mediana): {prob_maior_mediana:.4f}')
