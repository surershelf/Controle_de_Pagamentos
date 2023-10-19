def leiaInt(msg):
    while True:
        try:
            n= int(input(msg))
        except (ValueError,TypeError):
            print('\n\033[31mERRO!!! Por favor digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mERRO!!! Usúario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def Linha (tam=42) :
    return '-' * tam


def cabecalho (txt):
    print(Linha())
    print(f'{txt.center(42)}')
    print(Linha())



def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(Linha())
    opc= leiaInt('Sua Opção: ')
    return opc