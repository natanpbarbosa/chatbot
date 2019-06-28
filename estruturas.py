from chatterbot import ChatBot #lib pra criação do bot
from chatterbot.trainers import ListTrainer #lib pra treinamento
from pymongo import MongoClient #integrando servidor do MongoDB
import pprint #caso queira um pprint direto do banco de dados (versão 2.0)
import time

'''
Funcionamento do chatbot: 
-> A lib chatterbot utiliza listas pra manejar o chatbot. 
Por exemplo: [oi, olá, tchau, adeus]
Caso o usuário digite "oi", o chatbot responderá "olá".
'''

client = MongoClient('localhost', 27017) #criação do servidor mongo
db = client['chatterbot-database'] #nome do BD: chatterbot-database 
statements = db['statements'] #nome da collection: statements

def create(): #1
    bot = ChatBot(
        'chat', #Nome do chatbot = chat
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter', #Adaptador pra o MongoDB
        logic_adapters = ['chatterbot.logic.BestMatch'] #Melhora o reconhecimento das mensagens
    )
    return bot #Retorna toda a configuração do bot pra as outras funções

def update_read(bot): #2
    cluster = {} #Criação do cluster vazio
    vetor_cluster = [] #Criação da lista vazio
    continuar = 'n' 
    trainer = ListTrainer(bot) #Instância que treina o bot
    i = 0
    while True:
        c = int(input('\n[0] Atualizar\n[1] Ler os dados \n[2] Encerrar\nDigite o comando que deseja: '))
        print()
        if c == 0:
            while True:
                #atualizar o bot
                condicao = str(input('Deseja adicionar uma categoria? [S/N]: ')).lower().strip()
                if condicao == 's' or len(vetor_cluster) ==  0: #Se não tiver nenhuma categoria
                    categoria = str(input('Digite a categoria que deseja adicionar: '))
                else:
                    print('[Atualização do bot encerrada]')
                    break
                '''
                -> [ERRO]: Não é possível adicionar perguntas e respostas em um cluster específico
                 elif condicao == 'n' and len(vetor_cluster) > 0: #Se tiver alguma categoria adicionada + categoria > 0
                     print(f'Categoria "{vetor_cluster[len(vetor_cluster)-1]}" selecionada.') #Seleciona a última categoria
                     categoria = vetor_cluster[len(vetor_cluster)-1] #A categoria passa a ser a última da lista 
                 else:
                     print(f'Comando inválido. Categoria "{vetor_cluster[len(vetor_cluster)]}" selecionada.') #Se o usuário não digitar S ou N
                     categoria = vetor_cluster[len(vetor_cluster)] #Seleciona a última categoria
                '''
                print('[MODELAGEM DO CHATBOT]')
                cluster[categoria] = [] #Adiciona uma lista vazia nos atributos da categoria do dicionário Cluster
                #Ou seja, o dicionário passa a ser: {'<categoria>': []}

                #input da pergunta
                question = input(str('Digite a pergunta que deseja: '))
                cluster[categoria].append(question) #Seleciona a categoria e adiciona uma pergunta
                #Ou seja, o dicionário passa a ser: {'<categoria>': [<question>]}

                #input da resposta
                answer = input(str('Digite a resposta que deseja: '))
                cluster[categoria].append(answer) #Seleciona a categoria e adiciona uma resposta
                #Ou seja, o dicionário passa a ser: {'<categoria>': [<question>, <answer>]}

                vetor_cluster.append(categoria) #Adiciona uma categoria na lista vetor_cluster
                #Ou seja, o vetor_cluster passa a ser: vetor_cluster[<categoria>]
                print('Treinando o chatbot...')
                time.sleep(2)
                trainer.train(cluster[vetor_cluster[i]]) 
                print('[Treinamento executado com sucesso]')
                '''
                >> Treinamento  do chatbot
                - A alocação do 'i' determinará o espaço a ser selecionado na lista 'vetor_cluster'.
                Por exemplo, <categoria> = saudações // <pergunta> = oi // <reposta> = olá // vetor_cluster[0] = saudações //
                cluster[vetor_cluster[0]] = cluster[saudações] = [oi, olá].
                - Assim, já que o bot funciona por meio de uma lista, o programa tem por objetivo devolver o treinamento
                por meio de uma lista. Nesse caso, [oi, olá].
                '''
                i += 1 #Incrementa 1 pra o treinamento da próxima categoria seja efetivada da próxima vez 
                continuar = str(input('Deseja continuar? [S/N]: ')).lower().strip()
                if continuar == 'n':
                    break
        elif c == 1: #Faz a leitura dos dados 
            for y in range (0, len(vetor_cluster)): #O 'for' irá de 0 até o tamanho máximo do vetor_cluster
                print(f'{vetor_cluster[y]}: {cluster[vetor_cluster[y]]}') #vetor_cluster e cluster será totalmente varrido
                #Esse tipo de Read poderá ser melhorado na próxima versão. Com o uso do statements
        elif c == 2: #Encerra o while
            break
        else: #Invalidez
            print('Comando inválido. ')

def delete(bot): #4
    #versão 2.0: o delete() poderá ser categorizado por 
    opcao = str(input('Você deseja deletar tudo? [S/N]: ')).lower()
    if opcao == 's':
        db.statements.delete_many({}) #deleta todos os dados do banco

def usar_chatbot(bot): #5
    cont = 's'
    while True:
        mensagem = str(input('Digite o que deseja: '))
        print(bot.get_response(mensagem)) #get_response: input da mensagem e output de resposta, por meio da conexão do banco.
        #Essas ações ocorrem por meio do uso de listas. Como é explicado nas linhas 7-10.
        cont = str(input('Deseja continuar? [S/N]')).strip().lower()
        if cont == 'n':
            break



