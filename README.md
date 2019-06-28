# chatbot
Futura atualização (versão 2.0):

//STATEMENTS (mongodb integrado as categorias criadas)
Uso do statements será prioridade na próxima versão, pois o código e o mongodb será
totalmente integrado e, dessa forma, não será preciso a utilização de listas e dicionários
pra fazer o uso do read() e delete().

-> Utilizar o uso do statements pra categorizar os inputs do chatbot.
-> Com o uso do statements, update e read poderão ser inclusas em funções distintas.
-> Read() poderá ser feito por categorias. Por exemplo, caso o usuário queira apenas ler
as perguntas e respostas de uma categoria desejada (*linha 76 e 77)
-> Da mesma forma, a função delete() poderá ser criada de maneira mais efetiva,
pois terá a opção de excluir categorias inteiras.
-> Poder selecionar a categoria que desejar pra adicionar perguntas e respostas

//CLASSES
Utilizar o uso de classes pra estabelecer diferentes collections pra vários clientes. Assim, será
possível separar todas as categorias, perguntas e respostas pra cada cliente.
-> Criação da classe Cliente
-> Determinar atributos pra cada cliente. Nome do usuário/empresa, cpf/cnpj e etc

//MODULARIZAÇÃO
Melhoras a modularização do programa, facilitando a leitura e as próximas alterações
-> Estudar melhor formas de modularizar
-> Analisar o código e ver formas de modularizar da melhor forma

//CREATE()
Possibilitar o usuário a criar várias collections(ou banco de dados) a partir da função create()
-> Interligar o create() com as classes e poder integrar diferentes clientes para diferentes
collections (ou banco de dados)

//ERROS
Quando o programa é resetado, não dá pra captar os dados armazenados previamente, pois ele não analisa
os dados armazenados no MongoDB. Não é possível adicionar perguntas e respostas em uma categoria já existente
ou pré selecionada.
-> Fazer a analise da existência de uma categoria diretamente do MongoDB
-> Com o uso do MongoDB e categorização de cada cluster, a adição será possível de maneira mais simples

//REDUNDÂNCIAS
Função usar_chatbot() possui pergunta recorrente de uso. Na versão 2.0, otimizar o uso do bot com
conversas mais longas e sem tantas interrupções.
-> Aumentar o tempo de de conversa do chatbot sem interrupção.




