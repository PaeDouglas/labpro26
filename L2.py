import random
from datetime import datetime

# --- Exercícios Restantes ---

# 5. Divisível por 3 e por 7
def q5():
    num = inputint('Digite um número: ')
    if num % 3 == 0 and num % 7 == 0:
        print(f'{num} é divisível por 3 e por 7')
    else:
        print(f'{num} não é divisível por ambos simultaneamente')

# 6. Linha de crédito (30% do salário)
def q6():
    salario = inputfloat("Salário bruto: ")
    prestacao = inputfloat("Valor da prestação: ")
    limite = salario * 0.30
    if prestacao <= limite:
        print("Empréstimo pode ser concedido.")
    else:
        print(f"Empréstimo negado. Prestação máxima permitida: R${limite:.2f}")

# 7. Compreendido entre 20 e 50
def q7():
    num = inputint("Digite um número: ")
    if 20 <= num <= 50:
        print(f"O número {num} está entre 20 e 50.")
    else:
        print(f"O número {num} NÃO está entre 20 e 50.")

# 8. Comparação com 20
def q8():
    num = inputint("Digite um número: ")
    if num > 20:
        print("Maior do que 20")
    elif num == 20:
        print("Igual a 20")
    else:
        print("Menor do que 20")

# 9. Idade e validação de nascimento
def q9():
    ano_nasc = inputint("Ano de nascimento: ")
    ano_atual = datetime.now().year
    if 1900 <= ano_nasc <= ano_atual:
        print(f"A idade é {ano_atual - ano_nasc} anos.")
    else:
        print("Ano de nascimento inválido!")

# 10. Três números em ordem crescente
def q10():
    nums = []
    for i in range(3):
        nums.append(inputint(f"Digite o {i+1}º número: "))
    nums.sort()
    print(f"Ordem crescente: {nums}")

# 11. Maior de três números
def q11():
    n1 = inputint("N1: ")
    n2 = inputint("N2: ")
    n3 = inputint("N3: ")
    print(f"O maior número é: {max(n1, n2, n3)}")

# 12. Faixas de idade
def q12():
    idade = inputint("Idade: ")
    if idade >= 65:
        print("Maior de 65 anos")
    elif idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

# 13. Média escolar e situação
def q13():
    nome = input("Nome do aluno: ")
    p1 = inputfloat("Nota Prova 1: ")
    p2 = inputfloat("Nota Prova 2: ")
    media = (p1 + p2) / 2
    print(f"Aluno: {nome} | Média: {media:.1f}")
    if media >= 7:
        print("Situação: Aprovado")
    elif media < 3:
        print("Situação: Reprovado")
    else:
        print("Situação: Em Prova Final")

# 14. Desconto INSS
def q14():
    salario = inputfloat("Salário: ")
    if salario <= 600:
        print("Isento de INSS")
    elif salario <= 1200:
        print(f"Desconto 20%: R${salario * 0.20:.2f}")
    elif salario <= 2000:
        print(f"Desconto 25%: R${salario * 0.25:.2f}")
    else:
        print(f"Desconto 30%: R${salario * 0.30:.2f}")

# 15. Lucro do comerciante
def q15():
    compra = inputfloat("Valor da compra: ")
    if compra < 20:
        venda = compra * 1.45 # 45% de lucro
    else:
        venda = compra * 1.30 # 30% de lucro
    print(f"Valor de venda: R${venda:.2f}")

# 16. Categorias de natação
def q16():
    idade = inputint("Idade do nadador: ")
    if 5 <= idade <= 7: print("Infantil A")
    elif 8 <= idade <= 10: print("Infantil B")
    elif 11 <= idade <= 13: print("Juvenil A")
    elif 14 <= idade <= 17: print("Juvenil B")
    elif idade >= 18: print("Sênior")
    else: print("Idade fora das categorias competitivas.")

# 17. Plano de Saúde
def q17():
    nome = input("Nome: ")
    idade = inputint("Idade: ")
    if idade <= 10: valor = 30
    elif idade <= 29: valor = 60
    elif idade <= 45: valor = 120
    elif idade <= 59: valor = 150
    elif idade <= 65: valor = 250
    else: valor = 400
    print(f"{nome}, o valor do seu plano é R${valor:.2f}")

# 18. Mês correspondente
def q18():
    meses = [None, "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    num = inputint("Número do mês (1-12): ")
    if 1 <= num <= 12:
        print(f"O mês {num} é {meses[num]}")
    else:
        print("Não existe mês com este número.")

# 19. Arco-e-flecha
def q19():
    p = [inputint(f"Pontos Arqueiro {i+1}: ") for i in range(3)]
    p.sort(reverse=True)
    print(f"Pontos em ordem decrescente: {p}")
    soma = sum(p)
    if soma > 100:
        print(f"Equipe Classificada! Média: {soma/3:.2f}")
    else:
        print("Equipe desclassificada.")

# 20. Crédito Bancário
def q20():
    saldo = inputfloat("Saldo Médio: ")
    if saldo <= 500: cred = 0
    elif saldo <= 1000: cred = saldo * 0.3
    elif saldo <= 3000: cred = saldo * 0.4
    else: cred = saldo * 0.5
    print(f"Saldo Médio: R${saldo:.2f} | Crédito: R${cred:.2f}")

# 21. Biblioteca
def q21():
    livro = input("Nome do livro: ")
    tipo = input("Tipo (professor/aluno): ").lower()
    dias = 10 if tipo == 'professor' else 3
    print("-" * 20)
    print(f"RECIBO\nLivro: {livro}\nUsuário: {tipo}\nDevolução em: {dias} dias")

# 22. Consumo de Combustível
def q22():
    dist = inputfloat("Distância (km): ")
    tipo = input("Tipo do carro (A, B ou C): ").upper()
    match tipo:
        case 'A': print(f"Estimativa: {dist/12:.2f} litros")
        case 'B': print(f"Estimativa: {dist/9:.2f} litros")
        case 'C': print(f"Estimativa: {dist/8:.2f} litros")
        case _: print("Tipo de carro inválido.")

# 23. Contador de Calorias
def q23():
    # Simplificado usando dicionários para mapear escolhas
    pratos = {1: 180, 2: 230, 3: 250, 4: 350} # Vegetariano, Peixe, Frango, Carne
    sobremesas = {1: 75, 2: 110, 3: 170, 4: 200}
    bebidas = {1: 20, 2: 70, 3: 100, 4: 65}
    
    print("Escolha: 1-Veg/Abacaxi/Chá, 2-Peixe/Sorvete/SucoL, 3-Frango/MousseD/SucoM, 4-Carne/MousseC/RefriD")
    p = inputint("Prato: ")
    s = inputint("Sobremesa: ")
    b = inputint("Bebida: ")
    
    total = pratos.get(p, 0) + sobremesas.get(s, 0) + bebidas.get(b, 0)
    print(f"Total de calorias da refeição: {total}cal")

# 24. Renovação DUT (Placa)
def q24():
    placa = input("Digite a placa do carro: ")
    ultimo = int(placa[-1]) # Pega o último caractere e converte em int
    meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 
             6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 0: "Outubro"}
    print(f"Renovação em: {meses[ultimo]}")

# 25. Índice de Poluição
def q25():
    indice = inputfloat("Índice de poluição: ")
    if indice >= 0.5:
        print("Intimação: Indústrias do 1º, 2º e 3º grupos devem suspender atividades.")
    elif indice >= 0.4:
        print("Intimação: Indústrias do 1º e 2º grupos devem suspender atividades.")
    elif indice >= 0.3:
        print("Intimação: Indústrias do 1º grupo devem suspender atividades.")
    else:
        print("Níveis de poluição aceitáveis.")