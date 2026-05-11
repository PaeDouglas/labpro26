import random
import math

# 1. Busca em lista de 15 números
def q1():
    lista = [random.randint(1, 50) for _ in range(15)]
    print(f"Lista gerada: {lista}")
    busca = int(input("Digite um número para buscar: "))
    if busca in lista:
        print(f"Encontrado na posição: {lista.index(busca)}")
    else:
        print("Nao encontrado!")

# 2. Listagem numerada ASCII 65-90 (A-Z)
def q2():
    letras = [chr(random.randint(65, 90)) for _ in range(10)]
    for i, letra in enumerate(letras):
        print(f"{i+1}: {letra}")

# 2.1 Gerador de senha (ASCII 40-126)
def q2_1():
    qtde = int(input("Quantidade de caracteres para a senha: "))
    senha = "".join(chr(random.randint(40, 126)) for _ in range(qtde))
    print(f"Senha sugerida: {senha}")

# 3. Par ou Ímpar com listagem numerada
def q3():
    numeros = [random.randint(1, 100) for _ in range(15)]
    for i, n in enumerate(numeros):
        status = "par" if n % 2 == 0 else "ímpar"
        print(f"{i+1}. {n} é {status}")

# 4. Múltiplos de seis
def q4():
    lista = [random.randint(1, 100) for _ in range(8)]
    print(f"Números: {lista}")
    multiplos = [n for n in lista if n % 6 == 0]
    print(f"Total de múltiplos de seis: {len(multiplos)}")

# 5. Notas e situação dos alunos (Tabulado)
def q5():
    alunos = []
    for i in range(15):
        p1 = round(random.uniform(0, 10), 1)
        p2 = round(random.uniform(0, 10), 1)
        media = round((p1 + p2) / 2)
        situacao = "Aprovado" if media >= 6 else "Reprovado"
        alunos.append([p1, p2, media, situacao])
    
    print(f"{'P1':<6} {'P2':<6} {'Média':<8} {'Situação'}")
    for a in alunos:
        print(f"{a[0]:<6} {a[1]:<6} {a[2]:<8} {a[3]}")

# 6. Reajuste salarial de 8%
def q6():
    salarios = [round(random.uniform(1412, 5000), 2) for _ in range(20)]
    novos_salarios = [round(s * 1.08, 2) for s in salarios]
    for i in range(20):
        print(f"{i+1}. Antigo: R${salarios[i]:.2f} | Novo: R${novos_salarios[i]:.2f}")

# 7. Lucro de mercadorias
def q7():
    compra = [random.uniform(10, 100) for _ in range(100)]
    venda = [c * random.uniform(1.0, 1.4) for c in compra]
    l1, l2, l3 = 0, 0, 0
    for c, v in zip(compra, venda):
        lucro = ((v - c) / c) * 100
        if lucro < 10: l1 += 1
        elif lucro <= 20: l2 += 1
        else: l3 += 1
    print(f"Lucro < 10%: {l1}\n10% <= Lucro <= 20%: {l2}\nLucro > 20%: {l3}")

# 8. Dicionário de produtos
def q8():
    estoque = {}
    for i in range(1, 31):
        estoque[i] = {"qtd": random.randint(1, 50), "v_compra": 10.0, "v_venda": 15.0}
    
    op = int(input("Digite o código do produto (1-30) ou 0 para listar todos: "))
    if op == 0:
        for k, v in estoque.items(): print(f"Cód {k}: {v}")
    elif op in estoque:
        print(f"Produto {op}: {estoque[op]}")
    else:
        print("Produto não cadastrado.")

# 9. Elementos comuns entre dois conjuntos
def q9():
    set1 = {random.randint(1, 20) for _ in range(10)}
    set2 = {random.randint(1, 20) for _ in range(10)}
    print(f"Conjunto 1: {set1}\nConjunto 2: {set2}")
    print(f"Comuns: {set1.intersection(set2)}")

# 10 e 11. Fatoriais e Estatísticas
def q10():
    lista = [random.randint(1, 10) for _ in range(10)]
    fatoriais = [math.factorial(n) for n in lista]
    print(f"Original: {lista}\nFatoriais: {fatoriais}")
    q11(fatoriais)

def q11(lista=None):
    if lista is None: lista = [random.randint(1, 100) for _ in range(10)]
    maior = menor = lista[0]
    pares = 0
    soma = 0
    for n in lista:
        if n > maior: maior = n
        if n < menor: menor = n
        if n % 2 == 0: pares += 1
        soma += n
    print(f"Maior: {maior} | Menor: {menor}")
    print(f"Pares: {(pares/len(lista))*100}% | Média: {soma/len(lista)}")

# 12. Reserva de mesas (30 mesas, 5 lugares)
def q12():
    mesas = [5] * 30
    total_ocupado = 0
    while total_ocupado < 150:
        cod = int(input("Código da mesa (1-30) ou 0 p/ sair: "))
        if cod == 0: break
        if 1 <= cod <= 30:
            lugares = int(input(f"Lugares desejados (Disponível: {mesas[cod-1]}): "))
            if mesas[cod-1] >= lugares:
                mesas[cod-1] -= lugares
                total_ocupado += lugares
                print("Reserva confirmada!")
            else:
                print("Não há lugares suficientes nesta mesa.")
        else:
            print("Mesa inválida.")
    print("Sistema encerrado.")

# 13. Reserva de Voos
def q13():
    voos = {i: random.randint(0, 10) for i in range(1, 11)}
    print(f"Voos disponíveis e vagas: {voos}")
    while True:
        v_desejado = int(input("Número do voo (1-10) ou 0 para sair: "))
        if v_desejado == 0: break
        id_cliente = input("Identidade do cliente: ")
        if voos.get(v_desejado, 0) > 0:
            voos[v_desejado] -= 1
            print(f"Reserva OK! Cliente: {id_cliente}, Voo: {v_desejado}")
        else:
            print("Voo lotado ou inexistente.")

# 14. Quadrado dos elementos
def q14():
    l1 = [random.randint(1, 20) for _ in range(50)]
    l2 = [n**2 for n in l1]
    print(f"Originais: {l1[:10]}...") # Mostrando apenas parte
    print(f"Quadrados: {l2[:10]}...")

# 15. Contagem de números iguais ao último
def q15():
    lista = []
    while len(lista) < 100:
        n = int(input("Digite um número (0 para parar): "))
        if n == 0: break
        lista.append(n)
    if lista:
        ultimo = lista[-1]
        print(f"O último número foi {ultimo}, ele apareceu {lista.count(ultimo)} vezes.")

# 16. Estatísticas de 100 números reais
def q16():
    lista = [round(random.uniform(10, 50), 1) for _ in range(100)]
    media = sum(lista) / 100
    iguais_30 = lista.count(30.0)
    maior_media = len([n for n in lista if n > media])
    igual_media = len([n for n in lista if n == media])
    print(f"Média: {media:.2f}")
    print(f"Iguais a 30: {iguais_30} | Maiores que média: {maior_media} | Iguais à média: {igual_media}")

# 17. Inverso de 30 valores
def q17():
    lista = [random.randint(1, 100) for _ in range(30)]
    print(f"Original: {lista}")
    print(f"Invertida: {lista[::-1]}")

# 18. Únicos e ordenados
def q18():
    lista = [random.randint(1, 15) for _ in range(20)]
    print(f"Original: {lista}")
    ordenada_unica = sorted(list(set(lista)))
    print(f"Únicos e Ordenados: {ordenada_unica}")

# 19. Busca código e telefone
def q19():
    contatos = {i: f"9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}" for i in range(101, 131)}
    busca = int(input("Digite o código para buscar telefone: "))
    print(f"Telefone: {contatos.get(busca, 'Não encontrado')}")

# 20. Ordenação de alunos por nota
def q20():
    alunos = [[i, round(random.uniform(0, 10), 1)] for i in range(1, 101)]
    # Ordena pela média (index 1) de forma decrescente
    alunos.sort(key=lambda x: x[1], reverse=True)
    print(f"{'Matrícula':<12} {'Média'}")
    for matricula, media in alunos:
        print(f"{matricula:<12} {media}")

# --- DISPATCHER ---
try:
    questao = int(input('Questão a ser executada (1-20): '))
    if questao == 21: # Para o caso do 2.1
        q2_1()
    else:
        eval(f'q{questao}()')
except NameError:
    print("Essa questão ainda não foi implementada ou o número é inválido.")
except Exception as e:
    print(f"Erro ao executar: {e}")