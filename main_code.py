import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("email_data.csv")

print(df.head())

G = nx.from_pandas_edgelist(df, source='Sender', target='Receiver')

plt.figure(figsize=(8,6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=2500, font_size=8, edge_color='gray')
plt.title("Email Communication Network")
plt.show()

degree_centrality = nx.degree_centrality(G)
print("\nDegree Centrality:")
for node, value in degree_centrality.items():
    print(f"{node}: {value:.2f}")

betweenness_centrality = nx.betweenness_centrality(G)
print("\nBetweenness Centrality:")
for node, value in betweenness_centrality.items():
    print(f"{node}: {value:.2f}")
