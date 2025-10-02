# Título: Quais insights pode-se extrair sobre os dados referentes a mortalidade e renda?

# Link para o dataset utilizado: https://www.kaggle.com/datasets/mikhail1681/adult-mortality-rate-2019-2021

# Importa as bibliotecas necessárias
import pandas as pd                # Para manipulação de dados
import matplotlib.pyplot as plt    # Para criar gráficos

# Faz a leitura do arquivo com os dados
df = pd.read_csv("C:/Users/elber/OneDrive/Documentos/Trabalho programação/Adult mortality rate (2019-2021).csv")

# Converte colunas numéricas de texto para float
for col in ["Average_GDP_per_capita($)", "Average_HEXP($)", 
            "AMR_male(per_1000_male_adults)", "AMR_female(per_1000_female_adults)", "Average_CDR"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 1. Gera um histograma com a distribuição da taxa de mortalidade geral (CDR)
plt.figure(figsize=(10,5))
df["Average_CDR"].hist(bins=30, color="skyblue", edgecolor="black")
plt.title("Distribuição da Taxa de Mortalidade Média (CDR)")
plt.xlabel("Mortes por 1000 habitantes")
plt.ylabel("Número de países")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Cria um gráfico de dispersão entre PIB per capita e mortalidade masculina
plt.figure(figsize=(8,6))
plt.scatter(df["Average_GDP_per_capita($)"], df["AMR_male(per_1000_male_adults)"], alpha=0.6, color="green")
plt.title("Renda per capita vs Mortalidade masculina")
plt.xlabel("PIB per capita ($)")
plt.ylabel("Taxa de mortalidade masculina (por 1000)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Gráfico de dispersão entre gasto em saúde e mortalidade feminina
plt.figure(figsize=(8,6))
plt.scatter(df["Average_HEXP($)"], df["AMR_female(per_1000_female_adults)"], alpha=0.6, color="purple")
plt.title("Gasto em saúde vs Mortalidade feminina")
plt.xlabel("Gasto em saúde per capita ($)")
plt.ylabel("Taxa de mortalidade feminina (por 1000)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Filtra os países com mortalidade masculina semelhante à do Brasil (diferença < 5)
brasil_amr = df[df["Countries"] == "Brazil"]["AMR_male(per_1000_male_adults)"].values[0]
semelhantes = df[abs(df["AMR_male(per_1000_male_adults)"] - brasil_amr) < 5]

# Exibe esses países em forma de tabela
print(f"Países com mortalidade masculina parecida com a do Brasil ({brasil_amr:.2f}):")
print(semelhantes[["Countries", "AMR_male(per_1000_male_adults)", 
                   "Average_GDP_per_capita($)", "Average_HEXP($)"]])

# 5. Gráfico de barras horizontais da mortalidade masculina desses países
semelhantes = semelhantes.sort_values("AMR_male(per_1000_male_adults)")
cores = ["red" if pais == "Brazil" else "steelblue" for pais in semelhantes["Countries"]]

plt.figure(figsize=(10,6))
plt.barh(semelhantes["Countries"], semelhantes["AMR_male(per_1000_male_adults)"], color=cores)
plt.title("Países com mortalidade masculina semelhante à do Brasil")
plt.xlabel("Mortalidade masculina (por 1000 adultos)")
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# 6. Gráfico de barras com o gasto em saúde desses mesmos países
semelhantes = semelhantes.sort_values("Average_HEXP($)")
cores_gasto = ["red" if pais == "Brazil" else "steelblue" for pais in semelhantes["Countries"]]

plt.figure(figsize=(10,6))
plt.barh(semelhantes["Countries"], semelhantes["Average_HEXP($)"], color=cores_gasto)
plt.axvline(semelhantes[semelhantes["Countries"] == "Brazil"]["Average_HEXP($)"].values[0],
            color="gray", linestyle="--")  # Linha de referência para o gasto do Brasil
plt.title("Gasto em Saúde per capita\n(Países com mortalidade masculina semelhante ao Brasil)")
plt.xlabel("Gasto em saúde per capita ($)")
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# Conclusões:
    # A maior parte dos países apresenta uma taxa de mortalidade geral entre 5 e 10 mortes por 1000 habitantes, com poucos casos extremos acima de 15.
    # Existe uma tendência inversa: países com maior PIB per capita tendem a apresentar menor mortalidade masculina.
    # O padrão se repete: países que gastam mais em saúde por pessoa geralmente têm menor mortalidade entre mulheres.
    # O Brasil tem uma taxa de mortalidade masculina adulta de 189,60 por 1000 adultos, alguns possuem renda per capita muito menor, indicando que o Brasil pode ter espaço para melhorar seus indicadores sociais com os recursos que possui.
    # Outros países gastam menos que o Brasil em saúde, mas apresentam desempenho parecido, o que sugere a necessidade de revisar a eficiência dos investimentos públicos em saúde.