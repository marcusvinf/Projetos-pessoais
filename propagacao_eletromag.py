import math
from time import sleep
from os import system, name


def clear():
    #windows
    if name == 'nt':
        _ = system('cls')

        # linux e mac
    else:
        _ = system('clear')


def main():
    print("-------------------------------------")
    print(" ")
    print("Programa de Progação Eletrogmanética")
    print("Feito pelo aluno Marcus Vinícius de Souza Feitosa")
    print(" ")
    print("-------------------------------------")
    print(" ")
    frequencia = float(input("Digite a frequencia em MHz: "))
    condutividade = float(input("Digite a condutividade em mS/m: "))
    epsilon_rel = float(input("Digite a constante dieletrica: "))
    d1 = float(input("Digite a distancia d1 em km: "))
    Eo=float(input("Digite o campo elétrico em mV/m: "))

    x= (18 *condutividade)/frequencia
    b_linha = math.degrees(math.atan((epsilon_rel-1)/x))
    b_2linha = math.degrees(math.atan((epsilon_rel)/x))
    b = 2*b_2linha - b_linha

    p = (0.5817*(frequencia**2) *d1*((math.cos(math.radians(b_2linha)))**2))/(condutividade*math.cos(math.radians(b_linha)))

    A = (2+0.3*p)/(2+p+0.6*(p**2))
    At = A-(math.sqrt(p/2)*math.exp(((-1)*5*p)/8)*math.sin(math.radians(b)))

    E=((Eo*At)/(d1*1000.0))*(10**6)
    Edbu= 20*math.log10(E)



    print("")
    print("")
    print('x: {}'.format(x))
    print('b_linha: {}º'.format(b_linha))
    print('b_2linha: {}º'.format(b_2linha))
    print('b: {}º'.format(b))
    print('p: {}'.format(p))
    print('A1: {}'.format(A))
    print('At: {}'.format(At))
    print('E: {} uV/m'.format(E))
    print('Edbu: {} dBu'.format(Edbu))

    print("")
    print("")



main()

while True:
    escolha = input("Digite 'nov' para calcular novamente ou qualquer coisa para sair: ")
    if escolha == 'nov':
        clear()
        main()

    else:
        print("MUITO OBRIGADO POR UTILIZAR O SOFTWARE :) !")
        sleep(3)
        break



