##########################################################
#---------------> EXERCISE 1.1
def sub2(x, y):
    res = x - y
    print(res)
sub2(5,7)

#---------------> EXERCISE 1.2
def soma3(x=0, y=0, z=0):
    res = x + y +z
    print(res)
soma3(1,2,3)
soma3(1,2)
soma3(1)
soma3()

#---------------> EXERCISE 2.1 / ESCOPO
def comida():
    print(ovos)

    ovos = 12
    comida()

#---------------> EXERCISE 2.2 / ESCOPO
def comida():
    ovos = 12
    bacon()
    print(ovos)

    def bacon ():
        ovos = 6

    comida()

#---------------> EXERCISE 2.3 / ESCOPO
def comida():
    ovos = 'variavel local de comida'
    print(ovos)

def bacon():
    ovos = 'variavel local de bacon'
    print(ovos)
    comida()
    print(ovos)

ovos = 'variavel global'
bacon()
print(ovos)

#---------------> EXERCISE 2.4 / ESCOPO

def comida():
    global ovos
    ovos = 'comida'

ovos = 'global'
comida()
print(ovos)

#---------------> EXERCISE 3.1 / RETORNO

def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return  res

retornando = soma3(1,2,3)
print(retornando)
print(soma3(2,2))

retornando1 = soma3(1,2,3)
retornando2 = soma3(1,2)
retornando3 = soma3()
print('Somatorio: {}, {} e {}.'.format(retornando1, retornando2, retornando3))

#---------------> EXERCISE 3.2 / RETORNO

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
        return s1
x = valida_string('Digite uma string: ', 10, 30)
print('Voçê digitou a string: {}. \n Dado válido. encerrando o programa'.format(x))

#---------------> EXERCISE 4.1 / TRY

x = int(input('Por favor digite um número: '))
while true:
    try:
        x  = int(input('Por favor digite um número'))
        break

    except ValueError:
        print('Oops! Número invalido. tente novamente.....')

#---------------> EXERCISE 4.2 / TRY

def div():
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite um número: "))
        res = num1 / num2

    except ZeroDivisionError:
        print("Oops! Erro de divisão por zero.....")
    except:
        print("Algo de errado aconteceu.......")
    else:
        return res
    finally:
        print("Executa sempre!")

print(div())

#---------------> EXERCISE 4.2 / FUNÇÂO DENTRO DE FUNÇÃO & LAMBDA

def imprime_com_condicao(num, fcond):
    if fcond(num):
        print(num)

    def par (x):
        return x % 2 == 0
    def impar(x):
        return  not par(x)

    imprime_com_condicao(5, par)