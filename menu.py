""" Trabalho de criptografia para conclusão semestral - Interface """

import getpass as gp
import criptograffia_descriptografia as cd

lista_cifra = []
ixibir = []
i = 0

def menu (mensagem='continue', chave='continue', id_='pass', key_='continue'):
    ''' Exibe o menu com as mensagens criptografadas e a mensagem descriptografada '''
    str_clean = ''
    if mensagem != 'continue':
        lista_criptografia = cd.Criptografar(mensagem, chave).realizar_criptografia()
        lista_cifra.append(lista_criptografia)
        ixibir.clear()
        ixibir.append([{id_+1: {cifra}} for id_, cifra in enumerate(lista_cifra)])
    if id_ != 'pass':
        str_clean = cd.Descriptografar(lista_cifra[id_-1], key_).entregar_descriptografia()

    meneu = f'''
    -----------------------------------------------------------------------------------------
    =========================================================================================
    =================================   BEM VINDO   =========================================
    ================= APS - ATIVIDADE PRATICA SUPERVISIONADA - UNIP =========================
    =======================    AS TÉCNICAS CRIPTOGRÁFICAS   =================================
    =========================================================================================
    ===========================    CRIPTOGRAFIA SIMÉTRICA    ================================
    =========================================================================================
    Criptografia simétrica depende de uma chave para criptografar e a mesma para descriptogra-
    far
    -----------------------------------------------------------------------------------------
    PARA CRIPTOGRFAR UMA MENSAGEM = [1]                 PARA DESCRIPTOGRFAR UMA MENSAGEM = [2]
    
    MENSAGENS CRIPTOGRADAS:
    {ixibir}
    
    SELECIONE O NÚMERO DE IDENTIFICAÇÃO E ENTRE COM A CHAVE QUE USOU PARA GERAR-LA
    
    MENSAGEM DESCRIPTOGRAFADA:
    {str_clean}
    
    LIMPAR MENSAGEMS CRIPTOGRADAS = [3]                                            SAIR = [4]'''
    return print(meneu)

while True:
    if i == 0:
        menu()
        i+=1

    try:
        select_option = int(input("SELECIONE UMA OPÇÃO: "))
        if select_option == 1:
            txt = input(">>> Digite um texto para criptografar: ")
            key = gp.getpass('>>> Sua chave: ')
            menu(mensagem=txt, chave=key)
        elif select_option == 2 :
            print("Selecione qual mensagem criptografada você quer descriptografar")
            select_cifra = int(input('>>> Selecione o ID que está na frente da cifra: '))
            try:
                if select_cifra in ixibir[0][select_cifra-1]:
                    key_descri = gp.getpass('>>> Usar a mesma senha usada para criptografar a cifra: ')
                    menu(id_=select_cifra, key_=key_descri)
                else:
                    print('ID não encontrado \nTente novamente!')
            except IndexError:
                print('Intex erro')
        elif select_option == 3:
            lista_cifra.clear()
            ixibir.clear()
            menu()
        elif select_option == 4:
            break
        else:
            print('COMANDO INVÁLIDO')
    except ValueError:
        print('Somente números!!')
