import requests
import pandas as pd
import time

TOKEN = "TOKEN"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "python-script"
}   

query = """
query ($cursor: String) {
  search(query: "stars:>1 sort:stars-desc", type: REPOSITORY, first: 15, after: $cursor) {
    pageInfo {
      endCursor
      hasNextPage
    }
    nodes {
      ... on Repository {
        name
        createdAt
        updatedAt
        stargazerCount
        primaryLanguage {
          name
        }
        releases {
          totalCount
        }
        pullRequests(states: MERGED) {
          totalCount
        }
      }
    }
  }
}
"""

url = "https://api.github.com/graphql"

cursor = None
repos = []

while len(repos) < 1000:

    variables = {"cursor": cursor}

    # retry automático
    for tentativa in range(5):
        response = requests.post(
            url,
            json={"query": query, "variables": variables},
            headers=headers
        )

        if response.status_code == 200:
            break

        print(f"Erro {response.status_code}, tentando novamente...")
        time.sleep(2)

    if response.status_code != 200:
        print("Falha permanente:", response.text)
        break

    data = response.json()

    nodes = data["data"]["search"]["nodes"]

    for repo in nodes:

        repos.append({
            "name": repo["name"],
            "created_at": repo["createdAt"],
            "updated_at": repo["updatedAt"],
            "stars": repo["stargazerCount"],
            "language": repo["primaryLanguage"]["name"] if repo["primaryLanguage"] else None,
            "releases": repo["releases"]["totalCount"],
            "merged_pr": repo["pullRequests"]["totalCount"],
        })

        if len(repos) >= 1000:
            break

    page_info = data["data"]["search"]["pageInfo"]
    cursor = page_info["endCursor"]

    print(f"{len(repos)} repositórios coletados")

    time.sleep(2)

df = pd.DataFrame(repos)
df.to_csv("github_top1000.csv", index=False)

print("CSV gerado com sucesso!")