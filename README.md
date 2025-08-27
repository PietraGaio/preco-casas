# Predição de Preços de Imóveis -- Melbourne Housing Dataset 🏡
Este projeto utiliza o **Melbourne Housing Dataset** para prever o preço
de imóveis com base em variáveis como número de quartos, banheiros,
vagas de garagem e tamanho do terreno.

## 🔎 Etapas do Projeto

1.  **Exploração e tratamento dos dados**
    -   Remoção de colunas irrelevantes (alta cardinalidade ou muitos
        valores nulos).\
    -   Análise de correlação entre variáveis para entender a relação
        com o preço.
2.  **Modelagem**\
    Foram testados dois algoritmos de regressão:
    -   **Regressão Linear**\
    -   **Árvore de Decisão (Decision Tree Regressor)**
3.  **Avaliação de desempenho**\
    As métricas utilizadas foram:
    -   **Erro Quadrático Médio (MSE)**\
    -   **R² (coeficiente de determinação)**

## 📊 Resultados

-   **Regressão Linear**
    -   Erro Quadrático Médio: `278.042.756.554,86`\
    -   R²: `0,3023`
-   **Árvore de Decisão**
    -   Erro Quadrático Médio: `192.918.637.177,59`\
    -   R²: `0,5366`

➡️ Os resultados indicam que a **Árvore de Decisão** apresentou melhor
desempenho, explicando cerca de **53% da variação dos preços** contra
apenas 30% da Regressão Linear.

## 🚀 Conclusão

O modelo de **Árvore de Decisão** é mais adequado para este problema,
mas ainda apresenta margem para melhorias, como:\
- Testar **Random Forest** e **XGBoost**.\
- Realizar **otimização de hiperparâmetros**.\
- Criar novas features que capturem melhor o comportamento do mercado.
