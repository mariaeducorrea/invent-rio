#função para exibir o menu inicial
def menu():
    print('\nMenu:')
    print('1. Adicionar um item.')
    print('2. Listar itens.')
    print('3. Buscar item.')
    print('4. Sair')
    print()

#inventário iniciando sem itens
inventario = {}

#flag para controlar se o loop vai rodar
continuar = True

#iniciando o loop
while continuar:
    menu()

    escolha = input("Escolha uma opção: ")

    #Adicionar item
    if escolha == '1':
        try:
            #criar ID para item 
            id_item = int(input('Digite o ID do item: '))
            if id_item in inventario:
                print('ID já existe no inventário.')
            else:
                nome = input('Digite o nome do item: ')
                quantidade = int(input('Digite a quantidade: '))  
                inventario[id_item] = (nome,quantidade)       
                print(f'Item {nome} adicionado com sucesso.')
        except ValueError:
            print('Erro: ID e quantidade devem ser números inteiros.')

    #Listar itens
    elif escolha == '2':
        if not inventario:
            print('inventário vazio.')
        else:
            print('\nItens no Inventário: ')
            for id_item, (nome, quantidade) in inventario.items():
                print(f'ID: {id_item}, Nome: {nome}, Quantidade: {quantidade}')
            
    #Buscar item
    elif escolha == '3':
        try:
            id_busca = int(input('Digite o ID do item.'))
            if id_busca in inventario:
                nome, quantidade = inventario[id_item]
                print(f'Nome: {nome}, Quantidade: {quantidade}')
        except ValueError:
            print('ERRO: ID não encontrao.')

    #Sair gerenciador de inventario
    elif escolha == '4':
        print('Encerrando...')
        continuar = False

print('Programa encerrrado.')


'''
Como funcionar o gerenciador de nventário.

> Inicia com o menu paresentando 4 funcionalidade
1. adicionar 
2. listar
3. buscar
4. sair 

> adicionar item
    - solicita ao usuario o ID do item
        - verifica se id já esta no inventario e exibe mensagem se sim
    - caso contrário, prossegue para solicitar o nome e a quantidade do item
        - solicita nome
        - solicita quantidade
        - exibe mensagem com item adicionado

> listar
    - se inventario vazio
        - mensagem de que inventario está vazio
    - caso contrario 
        - mostra para cada id um nome e quantidade no inventario
 
> buscar
    - solicita ID do item a ser buscado
        - se item estiver no inventario 
            - exite nome + quantidade
        - caso contrario
            - item não encontrado

> Sair 
    - Encerra loop
        - exibe mensagem que programa será encerrado.


'''