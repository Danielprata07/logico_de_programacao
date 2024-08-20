#Tipos de concetenação
#Concatenação com sinal +
num = int(input('Digite um numero inteiro: '))

# não possivel concatenar numero inteiro usando esse metodo,a menos que 
# converta o numero inteiro em uma string 
print('Ola, '+ str(num) +', Seja bem-vindo!')
print(type(num))

# Concatenação com a (,)
print('O numero digitado é: ',num)

# Concatenação com fstring (f)
print(f'O numero digitado é: {num} usando a concatenação "f"')

div = num/3
#Usando format para formatação númerica
#Limitando a quantidade de casas decimais
print(f'O resultado da divisao é: {div:.2f}') 

 