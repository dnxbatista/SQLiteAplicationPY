import data.database as db

def start():
    while 1:
        print('-----------------------')
        print('1 - Visualizar Banco De Dados')
        print('2 - Adicionar Novas Informacoes Ao Banco De Dados')
        print('3 - Atualizar Informacoes Do Banco De Dados')
        print('4 - Remover Informacoes Do Banco De Dados')
        print('5 - Fechar Aplicativo')
        print('-----------------------')
        command = int(input('Oque Voce Deseja: '))

        if(command == 1):
            db.show_all()

        if(command == 2):
            print('\n')
            firstname = input('Qual Primeiro Nome Do Cliente: ')
            lastname = input('Qual Segundo Nome Do Cliente: ')
            age = int(input('Qual Idade Do Cliente: '))
            email = input('Qual Email Do Cliente: ')
            db.addNewItens(firstname,lastname,age,email)

        if(command == 3):
            print('\n')
            id = int(input('Qual Cliente Deseja Alterar (ID DO CLIENTE): '))
            print('-----------------------')
            print('Oque voce deseja alterar?')
            print('1 - Primero Nome')
            print('2 - Segundo Nome')
            print('3 - Idade')
            print('4 - Email')
            print('5 - Cancelar')
            updateItem = int(input('Digite o numero correspondente ao item: '))             
            if(updateItem == 1):
                updateValue = input('Digite o novo valor desse item: ')      
                db.updateItens('first_name',updateValue,id)
            if(updateItem == 2):
                updateValue = input('Digite o novo valor desse item: ')      
                db.updateItens('last_name',updateValue,id)
            if(updateItem == 3):
                updateValue = input('Digite o novo valor desse item: ')      
                db.updateItens('age',updateValue,id)
            if(updateItem == 4):
                updateValue = input('Digite o novo valor desse item: ')      
                db.updateItens('email',updateValue,id)
            if(updateItem == 5):
                return start()
            

        if(command == 5):
            db.disconnect()
            quit()
            
start()

