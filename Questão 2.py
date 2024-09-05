def dentro_do_fibonacci(numero):
    a = 0 
    b = 1
    while b < numero:
        a, b = b, a + b
    return b == numero

numero = int(input("Digite um número: "))

if dentro_do_fibonacci(numero):
    print(f"O número {numero} faz parte da sequência de fibonacci")
else:
    print(f"O número {numero} não faz parte da sequência de fibonacci")