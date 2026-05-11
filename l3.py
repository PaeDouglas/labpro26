def input_int(msg):
    return int(input(msg))

def input_float(msg):
    return float(input(msg))

# 1. 1 até 100
def q1():
    for i in range(1, 101):
        print(i, end=" ")
    print()

# 2. Pares de 100 até 1
def q2():
    for i in range(100, 0, -2):
        print(i, end=" ")
    print()

# 3. Múltiplos de 5 até 500
def q3():
    for i in range(5, 501, 5):
        print(i, end=" ")
    print()

# 4. Filtro de 20 pessoas (Masc > 21)
def q4():
    for i in range(20):
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").upper()
        if sexo == 'M' and idade > 21:
            print(f"-> {nome}")

# 5. Produto via somas sucessivas
def q5():
    n1 = int(input("N1: "))
    n2 = int(input("N2: "))
    produto = 0
    for _ in range(n2):
        produto += n1
    print(f"Produto: {produto}")

# 6. Fibonacci 20 termos
def q6():
    a, b = 1, 1
    for _ in range(20):
        print(a, end=" ")
        a, b = b, a + b
    print()

# 7. Médias de 15 alunos e geral
def q7():
    soma_geral = 0
    for i in range(15):
        nome = input(f"Nome Aluno {i+1}: ")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        media = (n1 + n2) / 2
        soma_geral += media
        print(f"{nome} - Média: {media:.2(f)}")
    print(f"Média Geral da Turma: {soma_geral/15:.2f}")

# 8. IRPF de 10 pessoas
def q8():
    for _ in range(10):
        nome = input("Nome: ")
        sal = float(input("Salário Bruto: "))
        if sal < 1300:
            taxa = 0
        elif sal < 2300:
            taxa = 0.10
        else:
            taxa = 0.15
        print(f"{nome} - Imposto: R$ {sal * taxa:.2f}")

# 9. Pesquisa Cinema (20 pessoas)
def q9():
    soma_idade_ex = 0
    cont_ex = 0
    cont_reg = 0
    cont_bom = 0
    for _ in range(20):
        idade = int(input("Idade: "))
        op = int(input("Opinião (3-Exc, 2-Bom, 1-Reg): "))
        if op == 3:
            soma_idade_ex += idade
            cont_ex += 1
        elif op == 1:
            cont_reg += 1
        elif op == 2:
            cont_bom += 1
    
    media_ex = soma_idade_ex / cont_ex if cont_ex > 0 else 0
    print(f"Média idade Excelente: {media_ex:.1f}")
    print(f"Quantidade Regular: {cont_reg}")
    print(f"Percentual Bom: {(cont_bom/20)*100}%")

# 11. Contador entre 100 e 200 (Sentinela 0)
def q11():
    cont = 0
    while True:
        n = int(input("Digite um número (0 p/ sair): "))
        if n == 0: break
        if 100 <= n <= 200:
            cont += 1
    print(f"Total entre 100 e 200: {cont}")

# 12. Crescimento populacional
def q12():
    popA, taxaA = 5000000, 0.03
    popB, taxaB = 7000000, 0.02
    anos = 0
    while popA <= popB:
        popA += popA * taxaA
        popB += popB * taxaB
        anos += 1
    print(f"Tempo necessário: {anos} anos.")

# 13. Conta de Luz (Sentinela 0)
def q13():
    total_1 = total_2 = total_3 = cont_1_2 = soma_1_2 = 0
    while True:
        num = int(input("Consumidor (0 p/ sair): "))
        if num == 0: break
        kwh = float(input("kWh: "))
        tipo = int(input("Tipo (1-Res, 2-Com, 3-Ind): "))
        precos = {1: 0.3, 2: 0.5, 3: 0.7}
        custo = kwh * precos.get(tipo, 0)
        print(f"Custo total: R$ {custo:.2f}")
        
        if tipo == 1: total_1 += kwh
        elif tipo == 2: total_2 += kwh
        elif tipo == 3: total_3 += kwh
        
        if tipo in [1, 2]:
            soma_1_2 += kwh
            cont_1_2 += 1
            
    print(f"Consumo Total - Res: {total_1}, Com: {total_2}, Ind: {total_3}")
    if cont_1_2 > 0: print(f"Média Consumo (1 e 2): {soma_1_2/cont_1_2:.2f}")

# 14. Fatorial de vários números
def q14():
    import math
    while True:
        n = int(input("Fatorial de (n < 1 p/ sair): "))
        if n < 1: break
        print(f"{n}! = {math.factorial(n)}")

# 16. Resto da divisão via subtrações
def q16():
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    quociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
    print(f"Quociente: {quociente}, Resto: {dividendo}")

# 18. Pousada
def q18():
    total_faturado = 0
    while True:
        conta = int(input("Nº Conta (0 p/ sair): "))
        if conta == 0: break
        nome = input("Nome cliente: ")
        dias = int(input("Qtd dias: "))
        taxa = 15 if dias < 10 else 8
        valor = (30 + taxa) * dias
        total_faturado += valor
        print(f"Cliente: {nome} | Conta: {conta} | Total: R$ {valor:.2f}")
    print(f"Total Faturado Pousada: R$ {total_faturado:.2f}")

# 23. Olimpíada (Sentinela @)
def q23():
    f_mais_alta = ["", 0]
    m_mais_pesado = ["", 0]
    soma_idade = cont = 0
    while True:
        nome = input("Nome (@ p/ sair): ")
        if nome == "@": break
        sexo = input("Sexo (M/F): ").upper()
        idade = int(input("Idade: "))
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        
        soma_idade += idade
        cont += 1
        
        if sexo == 'F' and altura > f_mais_alta[1]:
            f_mais_alta = [nome, altura]
        if sexo == 'M' and peso > m_mais_pesado[1]:
            m_mais_pesado = [nome, peso]
            
    print(f"Mulher mais alta: {f_mais_alta[0]} ({f_mais_alta[1]}m)")
    print(f"Homem mais pesado: {m_mais_pesado[0]} ({m_mais_pesado[1]}kg)")
    if cont > 0: print(f"Média idade: {soma_idade/cont:.1f} anos")

# 30. Estado Civil (Idade < 0 p/ sair)
def q30():
    casados = solteiros = viúvos = soma_idade_v = desquitados = total = 0
    while True:
        idade = int(input("Idade (negativo p/ sair): "))
        if idade < 0: break
        ec = input("Estado Civil (C, S, V, D): ").upper()
        total += 1
        if ec == 'C': casados += 1
        elif ec == 'S': solteiros += 1
        elif ec == 'V':
            viúvos += 1
            soma_idade_v += idade
        elif ec == 'D': desquitados += 1
        
    print(f"Casados: {casados}, Solteiros: {solteiros}")
    if viúvos > 0: print(f"Média idade viúvos: {soma_idade_v/viúvos:.1f}")
    if total > 0: print(f"% Desquitados: {(desquitados/total)*100:.1f}%")