"""Obtenha dados da altura e o gênero (Masculino ou Feminino) de 15 pessoas e apresente os seguintes resultados:

- A maior e a menor altura do grupo;
- A média de altura das pessoas do gênero Masculino;
- O número de pessoas do gênero Feminino.

Para o desenvolvimento da atividade, o aluno deve utilizar a linguagem de programação que desejar."""







dados = {}

maioraltura = 0
menoraltura = 3
totalfeminino = 0
totalmasculino = 0
somamasculino = 0

for i in range(15):
    nome = input("Digite o seu nome: ")
    genero = input("Digite F ou M para determinar se seu gênero é masculino ou feminino:  ")
    altura = float(input("Digite a sua altura: "))

while altura <= 0 or altura >= 3:
    print("Altura inválida! O valor deve ser em até no máximo 3m. ")
    altura = float(input("Digite a sua altura novamente: "))


dados[nome] = {"altura": altura, "genero": genero}

if altura > maioraltura:
    maioraltura = altura
elif altura < menoraltura:
    menoraltura = altura

if genero == "F" or genero == "f":
    totalfeminino = totalfeminino + 1
if genero == "M" or genero == "m":
    somamasculino = somamasculino + altura
    totalmasculino = totalmasculino + 1



if totalmasculino > 0:
    mediaaltura = somamasculino / totalmasculino
else:
    mediaaltura = 0

print(f"Estatísticas das 15 pessoas:\n Maior altura: {maioraltura};\n Menor altura: 
{menoraltura};\n Total de mulheres: {totalfeminino};\n Média das alturas masculinas: {mediaaltura}  ")


























