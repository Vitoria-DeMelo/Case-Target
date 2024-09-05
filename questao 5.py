
def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

palavra = input("Digite a palavra que você deseja inverter: ")

# Chamando a função para inverter a palavra
palavra_invertida = inverter_string(palavra)

# Imprimindo o resultado
print("A palavra invertida é:", palavra_invertida)