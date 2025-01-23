import os


restaurantes = []

def exibir_nome_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')    

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')


def opcao_invalida():
    print('opcao_invalida! \n')  
    input("Digite uma tecla para voltar ao menu principal: ")  
    main()



def Cadastrar_novo_Restaurante():
    os.system('cls')
    print('Cadastro de novos Restaurantes\n ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso ')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = input('Escolha uma Opção: ')
        opcao_escolhida = int(opcao_escolhida) 

        if opcao_escolhida == 1:
            Cadastrar_novo_Restaurante()
        elif opcao_escolhida == 2:
            print('Listar Restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            print('Finalizar app')
        else:
            opcao_invalida()
    except:
            opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

    