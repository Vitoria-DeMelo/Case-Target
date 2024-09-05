import pandas as pd

df = pd.read_json(r"C:\Users\guilh\Downloads\dados.json")

soma = df['valor'].sum()
contagem = df['dia'].count()
media = soma / contagem

valor_maior_media = df['valor'] > media
dias_acima_media = valor_maior_media.sum()

minimo = df['valor'].min()
maximo = df['valor'].max()

print(f'o valor mínimo é {minimo}')
print(f'o valor máximo é {maximo}')
print(f'a valor da média é {media}')
print(f'O número de dias que as vendas foram maiores que a média é de: {dias_acima_media}')