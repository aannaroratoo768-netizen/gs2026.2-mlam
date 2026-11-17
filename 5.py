# 05. REGRESSÃO LINEAR MÚLTIPLA E LOGÍSTICA BINÁRIA
# Regressão Múltipla
X_mult = pd.DataFrame({'3790': np.random.rand(100), '37,5%': np.random.rand(100)})
X_mult_sm = sm.add_constant(X_mult)
modelo_rlm = sm.OLS(Y_simples, X_mult_sm).fit()
print(modelo_rlm.summary())

# Regressão Logística
Y_binario = np.where(Y_simples > Y_simples.median(), 1, 0)
X_train, X_test, Y_train, Y_test = train_test_split(X_mult, Y_binario, test_size=0.3, random_state=42)

modelo_log = LogisticRegression().fit(X_train, Y_train)
Y_pred = modelo_log.predict(X_test)
print(f'\nAcurácia da Classificação: {accuracy_score(Y_test, Y_pred):.4f}')
