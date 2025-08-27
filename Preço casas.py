# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport
pd.options.display.float_format = '{:,.2f}'.format
%matplotlib inline

base = pd.read_csv("melb_data.csv")

# Tratamento de Dados
# Exclusão de colunas que tiverem uma alta cardinalidade
base = base.drop(["Suburb","Address","SellerG","Date"],axis=1)
# Exclusão de  colunas com mais de 20% de valores nulos
base = base.drop(["BuildingArea","YearBuilt"],axis=1)

# Correlação de Variáveis
plt.figure(figsize=(13,8))
sns.heatmap(base.corr(),annot=True,cmap="YlGnBu")
plt.show()

# Correlação mais alta e Landsize pois retiramos o BuildingArea
base1 = base[["Price","Rooms","Bathroom","Bedroom2","Car","Landsize"]]

# TrataExclusão de valores nulos
base1 = base1.dropna(axis=0)

# Treino e Teste
Y = base1.Price
X = base1.drop('Price', axis=1)

from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(X,Y)

# Escolha do modelo

# Regressão Linear
from sklearn.linear_model import LinearRegression
modelo_regressao = LinearRegression()
modelo_regressao.fit(x_treino,y_treino)
y_regressao = modelo_regressao.predict(x_teste)

# Análise de Resultados
from sklearn.metrics import r2_score
r2_regressao = r2_score(y_teste,y_regressao)
print(r2_regressao)

from sklearn.metrics import mean_squared_error
erro_quadratico_regressao = mean_squared_error(y_teste,y_regressao)
print(erro_quadratico_regressao)

# Random Forest
from sklearn.tree import DecisionTreeRegressor
modelo_arvore_decisao = DecisionTreeRegressor()
modelo_arvore_decisao.fit(x_treino,y_treino)
y_arvore_decisao = modelo_arvore_decisao.predict(x_teste)

# Análise de Resultados
erro_quadratico_arvore_decisao = mean_squared_error(y_teste,y_arvore_decisao)
print(erro_quadratico_arvore_decisao)

r2_arvore_decisao = r2_score(y_teste,y_arvore_decisao)
print(r2_arvore_decisao)

# Resumo de Resultados
print('Regressão Linear')
print('Erro quadrático médio: ' + str(round(erro_quadratico_regressao,2)))
print('R quadrado: '+ str(round(r2_regressao,4)))
print('-----------------------------------------')
print('Árvore de Decisão')
print('Erro quadrático médio: ' + str(round(erro_quadratico_arvore_decisao,2)))
print('R quadrado: '+ str(round(r2_arvore_decisao,4)))
