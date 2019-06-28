'''
Projeto: Chatbot Personalizado
O que é?: Criação de um chatbot que possibilite o usuário a criar perguntas/respostas de maneira intuitiva e simples.
Versão: 1.0
Nome: Natan Pereira Barbosa
'''

import estruturas 

print('\n-----------CHATBOT------------')
print('[DIGITE O COMANDO QUE DESEJA]\n')

while True:
    #menu
    print('[0]: ENCERRAR \n[1]: CRIAR\n[2]: ATUALIZAR ou LER')
    print('[3]: DELETAR \n[4]: USAR CHATBOT \n')
    c = int(input('Digite o comando que deseja de 0 a 4: '))

    #switch menu
    if c == 0:
        print('[PROGRAMA ENCERRADO]')
        break
    elif c == 1: #create()
        '''
        > Função create(): criação do bot, uso do bot nas outras funções e 
        estabelece os logic adapters (integrado com MongoDB)
        '''
        print()
        print('[COMANDO CRIAR CHATBOT ATIVADO]') 
        estruturas.create()
        print('\n[BOT CRIADO COM SUCESSO]\n')
    elif c == 2: #update_read()
        '''
        > Função update_read(): adição e leitura das categorias, perguntas, respostas (respostas e perguntas integradas com MongoDB).
        '''
        print('[COMANDO ATUALIZAR ou LER ATIVADO]')
        estruturas.update_read(estruturas.create())
    elif c == 3: #delete() 

        '''
        > Função delete(): deleta todos os dados do banco (drop() integrado com MongoDB)
        '''
        print('[COMANDO DELETAR ATIVADO]') 
        estruturas.delete(estruturas.create())
    elif c == 4: #usar_chatbot(estruturas.create())
        '''
        > Função usar_chatbot(): possibilita a conversa com o chatbot
        '''
        print('[COMANDO USAR CHATBOT ATIVADO]')
        estruturas.usar_chatbot(estruturas.create())
    else: #invalidez
        print('\n[Numero invalido, digite novamente]\n')

