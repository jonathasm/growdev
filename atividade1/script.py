#%%
# 1 - Conversão de graus Celsius para Fahrenheit – Crie um programa que converta graus
# Celsius em Fahrenheit. A fórmula é a seguinte: F = C * 1.8 + 32.
# O programa deve solicitar ao usuário que insira uma temperatura em graus Celsius e, em
# seguida, exiba a temperatura convertida em Fahrenheit. Após construir esse programa,
# modifique-o para que converta graus Fahrenheit em graus Celsius.
def celsius_to_fahrenheit():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    return celsius * 1.8 + 32


def fahrenheit_to_celsius():
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    return (fahrenheit - 32) / 1.8


#%%
# 2- Escreva um programa que receba um número e escreva “Par” caso esse número seja par
# e escreva “Impar” caso esse número seja impar.

def even_odd(number):
    return print("Par") if number % 2 == 0 else print("Impar")


#%%
def evaluate():
    """
     3 - Escreva um programa que receba dois números, exiba as opções:
     1 - adição
     2 - subtração
     Então peça ao usuário para escolher uma das opções. Caso escolha a opção 1 o programa
     deve realizar a soma dos dois números lidos e exibir. Caso escolha a opção 2 o programa
     deve realizar a subtração dos dois números lidos e exibir.
    """
    num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
    opcao = input("Escolha uma opção (1 - adição, 2 - subtração): ")
    print(f"Resultado: {num1 + num2 if opcao == '1' else num1 - num2 if opcao == '2' else 'Opção inválida.'}")


#%%
def student_status():
    """
     4 - Numa determinada escola, os critérios de aprovação são os seguintes:
     - O aluno deve ter, no máximo, 25% de faltas;
     - A nota final deve ser igual ou superior a 7,00.
     Construa um programa para ler as notas que um aluno tirou nos 4 bimestres, o número total
     de aulas e o número de faltas, mostrando ao final a situação do aluno como sendo
     “Aprovado”, “Reprovado por Faltas” e “Reprovado por média”, considerando que a
     reprovação por faltas se sobrepõe a reprovação por nota.
    """
    notas = [float(input(f"Digite a nota do {i + 1}º bimestre: ")) for i in range(4)]
    total_aulas, faltas = int(input("Digite o número total de aulas: ")), int(input("Digite o número de faltas: "))
    print("Reprovado por Faltas" if (faltas /
                                     total_aulas) > 0.25 else "Reprovado por média" if (sum(notas) /
                                                                                        len(notas)) < 7 else "Aprovado")


#%%
def student_status_variant_a():
    """
     5 - Após construir o programa anterior, crie mais duas versões dele para prever as seguintes
     situações:
     - Um aluno pode ficar em recuperação se possuir frequência suficiente (superior a
     75%) e média superior a 5 mas inferior a 7;
    """
    notas = [float(input(f"Digite a nota do {i + 1}º bimestre: ")) for i in range(4)]
    total_aulas, faltas = int(input("Digite o número total de aulas: ")), int(input("Digite o número de faltas: "))
    media = sum(notas) / len(notas)
    frequencia = (total_aulas - faltas) / total_aulas

    print("Reprovado por Média e Faltas"
          if frequencia < 0.75 and media < 7
          else "Reprovado por Faltas"
    if frequencia < 0.75
    else "Recuperação"
    if 5 <= media < 7
    else "Reprovado por média"
    if media < 7
    else "Aprovado")


def student_status_variant_b():
    """
     5 - Após construir o programa anterior, crie mais duas versões dele para prever as seguintes
     situações:
     - Caso um aluno reprove por média e faltas, sua situação deve ser “Reprovado por
     Média e Faltas” (ao invés de simplesmente “Reprovado por Faltas” como antes).
    """
    notas = [float(input(f"Digite a nota do {i + 1}º bimestre: ")) for i in range(4)]
    total_aulas, faltas = int(input("Digite o número total de aulas: ")), int(input("Digite o número de faltas: "))
    media = sum(notas) / len(notas)
    frequencia = (faltas / total_aulas)

    print("Reprovado por Média e Faltas"
          if frequencia > 0.25 and media < 7
          else "Reprovado por Faltas" if frequencia > 0.25
    else "Reprovado por média" if media < 7 else "Aprovado")


#%%
def is_valid_date():
    """
     6 - Escreva um programa que peça ao usuário para fornecer um dia, mês e o ano arbitrários
     e determine se esses dados correspondem a uma data válida. Não deixe de considerar que
     existem meses com 30 e 31 dias, e que fevereiro pode ter 28 ou 29 dias, dependendo se o
     ano for bissexto. Considere que um ano é bissexto quando for divisível por 4.
    """
    day, month, year = map(int, input("Digita a data dd/mm/yyyy ").split("/"))

    if month < 1 or month > 12 or day < 1 or day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2:
        if year % 4 == 0 and day > 29:
            return False
        elif year % 4 != 0 and day > 28:
            return False

    return True


#%%

def next_day():
    """
     7- Construa um programa que leia uma data qualquer (dia, mês e ano) e calcule a data do
     próximo dia. Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias. Lembre-se
     que um ano é bissexto quando for divisível por 4.
    """
    day, month, year = map(int, input("Digita a data dd/mm/yyyy ").split("/"))
    days_in_month = [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day += 1
    if day > days_in_month[month - 1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"0{day}/0{month}/{year}" if (day <
                                         10 and month <
                                         10) else f"0{day}/{month}/{year}" if (day <
                                                                               10) else f"{day}/0{month}/{year}" if (
            month <
            10) else f"{day}/{month}/{year}"


#%%
def get_concept():
    """
     8 - Faça um programa que leia as duas notas parciais obtidas por um aluno numa
     disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos
     obedece à tabela abaixo:
     Média de Aproveitamento
     - Entre 9.0 e 10.0 Conceito - A
     - Entre 7.5 e 8.9 - B
     - Entre 6.0 e 7.4 - C
     - Entre 4.0 e 5.9 - D
     - Entre 0 e 3.9 - E
     O programa deve mostrar na tela as notas, a média, o conceito correspondente e a
     mensagem:
     APROVADO se o conceito for A, B ou C.
     REPROVADO se o conceito for D ou E.
    """
    nota1, nota2 = float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    conceito = 'E' if media < 4 else 'D' if media < 6 else 'C' if media < 7.5 else 'B' if media < 9 else 'A'
    status = 'APROVADO' if conceito in ['A', 'B', 'C'] else 'REPROVADO'
    print(f"Notas: {nota1}, {nota2}\nMédia: {media}\nConceito: {conceito}\nStatus: {status}")
#%%
def calculate_salary_increase():
    """
     9 - As Organizações XTC resolveram dar um aumento de salário aos seus colaboradores e
     lhe contrataram para desenvolver o programa que calcula os reajustes. Faça um programa
     que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
     no salário atual:
     - salários até R$ 280,00 (incluindo): aumento de 20%
     - salários entre R$ 280,00 e R$ 700,00: aumento de 15%
     - salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
     - salários de R$ 1500,00 em diante: aumento de 5%
     Após o aumento ser realizado informe na tela:
     - o salário antes do reajuste;
     - o percentual de aumento aplicado;
     - o valor do aumento;
     - o novo salário, após o aumento.
    """
    salary = float(input("Digite o salário atual: "))
    increase_percentage = 20 if salary <= 280 else 15 if salary <= 700 else 10 if salary <= 1500 else 5
    increase_value = salary * increase_percentage / 100
    new_salary = salary + increase_value
    print(f"Salário antes do reajuste: R$ {salary}")
    print(f"Percentual de aumento aplicado: {increase_percentage}%")
    print(f"Valor do aumento: R$ {increase_value}")
    print(f"Novo salário, após o aumento: R$ {new_salary}")
