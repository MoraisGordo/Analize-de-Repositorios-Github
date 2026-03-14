import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dadosRepo = pd.read_csv("repositorios_com_metricas.csv", sep=";")
dadosRepo.columns = dadosRepo.columns.str.strip()

#GRAFICO 1
plt.figure()
plt.hist(dadosRepo["idade_anos"], bins=20)
plt.title("Distribuição da idade dos repositórios populares")
plt.xlabel("Idade (anos)")
plt.ylabel("Quantidade de repositórios")
plt.savefig("grafico 1.png")

#GRAFICO 2
plt.figure()
plt.hist(dadosRepo["merged_pr"], bins=30)
plt.title("Distribuição de Pull Requests Aceitos")
plt.xlabel("Pull Requests Aceitos")
plt.ylabel("Quantidade de Repositórios")
plt.tight_layout()
plt.savefig("grafico 2.png")

#GRAFICO 3
plt.figure()
plt.hist(dadosRepo["releases"], bins=30)
plt.title("Distribuição de Releases")
plt.xlabel("Número de Releases")
plt.ylabel("Quantidade de Repositórios")
plt.tight_layout()
plt.savefig("grafico 3.png")

#GRAFICO 4
plt.figure()
plt.scatter(dadosRepo["merged_pr"], dadosRepo["stars"])
plt.title("Relação entre Pull Requests e Popularidade")
plt.xlabel("Pull Requests mesclados")
plt.ylabel("Estrelas")
plt.savefig("grafico 4.png")

#GRAFICO 5
dadosLinguagens = pd.read_csv("linguagens_populares.csv", sep=";")
dadosLinguagens = dadosLinguagens.sort_values(by="quantidade", ascending=False)
top10 = dadosLinguagens.head(10)
plt.figure()
plt.bar(top10["linguagem"], top10["quantidade"])
plt.title("Top 10 Linguagens em Repositórios Populares")
plt.xlabel("Linguagem")
plt.ylabel("Quantidade de Repositórios")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico 5.png")

#GRAFICO 6
plt.figure()
plt.hist(dadosRepo["taxa_issues_fechadas"], bins=20)
plt.title("Distribuição da taxa de issues fechadas")
plt.xlabel("Taxa de resolução")
plt.ylabel("Quantidade")
plt.savefig("grafico 6.png")
