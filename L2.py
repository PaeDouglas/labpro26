import random
from datetime import datetime
from util impot inputint, inputfloat
#datetime.now()

def q1():
    num1 = int(input('digite um numero'))
    num2 = int(input('digite um numero'))
    adicao = num1 + num2
    if adicao > 10 :
        print (f'{num1}+{num2} + {adicao}')

def q2():

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    num = int(input('digite um numero inteiro: '))
    if num % 3 == 0: # se o resto da divisao é zero 
        print(f'{num} é multiplo de 3')
    else:
        print(f'{num} nao é multiplo de 3')

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
 def q4():

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
    num1 =int(input('digite um numero inteiro :'))
    if num % 3 == 0 and num% 7 == 0: ): # se o resto da divisão é zero 
    print (f'{num} é divisivel poe 3 e 7')
    else:
        print(f"{num} não é divisivl por 3 e 7")


#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto.
#   Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q6():
    num1 = int(input(" salario bruto: "))
    num2 = int(input('valor das parcelas: '))
    # if num1 > % 30 num2
    if (num1 % 30) > num2:
        print (f'o valor da prestaçao é: {(num1 % 30) > num2} ') 
    else: (num2 % 30) < num1:
        print ('não pode ser concedido')
    
#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7():
    num1 = int(input('digite qualquer numero: '))
    if num1 >= 20 and <= 50
        print (f'{num1} O numero esta contido entre 20 e 50 ')
   # else: print (f"o numero não esta contido entre 20 e 50")

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
num1 = int(input('digite qualquer numero: '))
    if num1 >= 20 and < 20
        print (f'{num1} é maior ou igual a 20 ')
    else: print (f'{num1} é menor que 20 ')  
    
#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q9():
    try
    ano_de_nascimento = int(input("digite o ano de nascimento"))
    #ano_atual = datetime.now().year
    ano_atual = int(input('digite o ano atual'))
    idade=(ano_de_nascimento - ano_atual)
     print (f' a idade é: ')
     except ValueError:
     print('digite apenas o ano ')

#nascimento = int(input(' ano de nascimento; '))
#if 1900<= nascimento <= datetime.now().year
#idade = datetime.now().year - nascimento 
#print (f'a pessoa tem {idade} naos !')
#else:
#print ('ano de nascimento invalido! ')



#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    a = inputint('digite um numero inteiro')
    b = inputint('digite um numero inteiro')
    c = inputint('digite um numero inteiro')
    resultado =''
    resultado += f'{a} {b} {c}' if  a<b<c else ""
    resultado += f'{a} {b} {c}' if  a<c<b else ""
    resultado += f'{a} {b} {c}' if  b<a<c else ""
    resultado += f'{a} {b} {c}' if  b<c<a else ""
    resultado += f'{a} {b} {c}' if  c<a<b else ""
    resultado += f'{a} {b} {c}' if  c<b<a else ""
    print(resultado)


#11. Faça um programa que leia 3 números e imprima o maior deles.
 def q11():
    maior = inputint('digite um numero inteiro:')
    numero = inputint('digite um segundo numero:')
    if numero > maior:
        maior = numero
    numero = inputint('digite um terceiro numero:')
    if numero > maior:
        maior = numero
    print(f'o maior numero informado é {maior}')

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

try:

    opcao = int(input('Digite o número da questão: '))
    if opcao < 1 or opcao > 25:
        raise exception('questao invalida, escolha de 1 a 25')
    eval('f' q{opcao}()')

    eval(f'q{opcao}()')

