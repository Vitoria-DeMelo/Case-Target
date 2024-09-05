import pandas as pd

dados = [
    {'Estado': 'SP', 'Faturamento': 67836.43},
    {'Estado': 'RJ', 'Faturamento': 36678.66},
    {'Estado': 'MG', 'Faturamento': 29229.88},
    {'Estado': 'ES', 'Faturamento': 27165.48},
    {'Estado': 'Outros', 'Faturamento': 19849.53}
]

df = pd.DataFrame(dados)

faturamento_total = df['Faturamento'].sum()

df['Percentual'] = (df['Faturamento'] / faturamento_total) * 100
df['Percentual'] = df['Percentual'].map('{:.2f}%'.format)

print(df)