import pandas as pd

df = pd.read_csv("github_top1000.csv")

df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])

hoje = pd.Timestamp.now(tz="UTC")

df["idade_dias"] = (hoje - df["created_at"]).dt.days
df["idade_anos"] = (df["idade_dias"] / 365).round(2)

df["dias_desde_update"] = (hoje - df["updated_at"]).dt.total_seconds() / 86400
df["dias_desde_update"] = df["dias_desde_update"].round(2)
df["taxa_issues_fechadas"] = df["closed_issues"] / df["total_issues"].replace(0, 1)

print("\nRESULTADOS DAS RQs\n")
print("RQ01 mediana idade (anos):", df["idade_anos"].median())
print("RQ02 mediana pull requests:", df["merged_pr"].median())
print("RQ03 mediana releases:", df["releases"].median())
print("RQ04 mediana dias desde update:", df["dias_desde_update"].median())

linguagens = df["language"].value_counts().reset_index()
linguagens.columns = ["linguagem", "quantidade"]

print("\nTOP LINGUAGENS\n")
print(linguagens.head(10))

df.to_csv("repositorios_com_metricas.csv", sep=";", index=False)
linguagens.to_csv("linguagens_populares.csv", sep=";", index=False)

print("Porcentagem issues fechadas:", (df["merged_pr"].sum() / (df["merged_pr"].sum() + df["releases"].sum()) * 100).round(2), "%")

print("\nArquivos gerados com sucesso!")