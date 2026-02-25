import math

def q1():
    print('douglas')

def q2():
   print(30*27)
    

def q3():
    soma = 5+8+12
    media = soma/3
    print(f'(5+8+12)/3 ={media}')


def q4():
    num = int(input('digite um numero: '))
    print(num)


def q5():
    num1 = float(input('digite um numero: '))
    num2 = float(input('digite um numero: '))
    print(num1)
    print(num2)



def q6():
    num = int(input('digite um numero inteiro: '))
    print(f' O antecessor de:{num} é {num-1}')
    print(f' O sucessor de:[num] é {num+1}')



def q7(): 
    nome = input('Digite seu nome: '). title().strip()
    endereço = input('Digite seu endereço: ') 
    telefone = input('digite seu telefone: ') 
    print(f'\nNome: {nome}\nEndereço: {endereço}/nTelefone: {telefone}')
    print('NOME\t\tEND\tFONE') #\t é tabulaçao (TAB e\n é newline (quebra de linha) )
    print (f'{nome}\t{endereço}\t{telefone}')



def q8():
    num1 = int(input('digite o primeiro numero: '))
    num2 = int(input(' digite o segundo numero: '))
    print (f' {num1}-{num2} = {num1-num2}') 
  


def q9():
    num = float(input('digite um numero real: '))
    print (F'1/4 DO NUMERO {num}: {num/4}')



def q10():
    num1 = float(input('Digite o primeiro numero real: '))
    num2 = float(input('digite o segundo numero real: '))
    num3 = float(input('digite o terceiro numero real: '))

    soma = num1 + num2 + num3
    media = soma/3 
    print(f'\nSubtracao de {num1} e {num2}: {num1 - num2}' )
    #prin(f'media de {num1}, {num2} e {num3} é igual a {media:.2f}') 



def q11():
    num1 = float(input('digite o 1 numero real'))
    num2 = float(input('digite o 2 numero real'))
    print (f'Adiçao: {num1+num2}')
    print (f'subtraçao: {num1 -num2}')
    print (f'multiplicaçãõ: {num1*num2}')
    print (f'divisão: {num1/num2:.2f}')



def q12():
    num = float(input('digite um numero real: '))
    print(f' o quadrado de{num:.2F} = {num*num}')#não reco9mendado 
    print(f'math.pow({num},2) = {math.pow(num,2)}') #para float este é indicado
    print(f'{num}**2 = {num**2}')# recomendado para int



def q13():
    saldo = round(float(input('digite o saldo da conta: r$ ' )),2)
    saldo = round(saldo, 2) # arredonda o valor para 2 casas decimais
    print(f' saldo de {saldo:.2f} +2% = R$ { saldo*0.02}')



def q14():
    base = float(input('digite a base doretangulo: '))
    altura = float (input ('digite a altura do triangulo')) 
    print(f'perimetro = {base*2 +altura*2}')
    print(f'area: { base*altura}')

def q15():
    valor = round(float(input('valor do produto: R$ ')),2)
    desconto_desejado = float(input(' % do desconto desejado: '))
    valor_desconto = valor*desconto_desejado/100
    print(f' valor do descontop: R${valor_desconto}')
    print(f'valor final do produto: R$ {valor-valor_desconto}')

def q16():
    salario_atual = float(input('informe o valor do salario: '))
    percentual_reajuste = float(input('informe o percentual de reajuste: '))
    novo_salario = salario_atual + (salario_atual*(percentual_reajuste/100))
    print(f'')


questao = input('digite a questão a ser executada: ')
eval(f'q{questao}()') # eval transforma iam string (texto em comando python)
