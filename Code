from Funcoes.format import *
from Funcoes.arquivos import *
import datetime

arq='Clientes.txt'
if not ArquivoExiste(arq):
    CriarArquivo(arq)

# fazer uma função que veja se os clientes pagaram o mes recorrente e mostre os que não pagaram,
data_atual = datetime.date.today()
mes = data_atual.month
ano = data_atual.year


arq_mes = f'Clientes Pagos - Mês {mes} Ano {ano}.txt'
if not ArquivoExiste(arq_mes):
    CriarArquivo(arq_mes)

while True:
    resposta = menu(['Cadastrar Nova Pessoa','Atualizar Cadastro','Deletar Cadastro','Pagadores do Mês','Ver Pessoas Cadastradas','Ver Vencimentos Próximos','Pagamentos Atrasados','Sair do Sistema'])

    if resposta==1:
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        tipo_pag=str(input('Qual o tipo do pagamento (Apartamento, Casa, Terreno, Etc.): '))
        data = int(input('Data de Vencimento: '))
        telefone = input('Telefone: ')
        valor_parcela = float(input('Valor da parcela: R$'))
        cadastrar(arq, nome,tipo_pag,data,telefone,valor_parcela)

    elif resposta == 2:
        cabecalho('ATUALIZAR CADASTRO')
        chave_busca = input('Digite o nome da pessoa a ser atualizada: ').title()
        novos_dados = input('Digite os novos dados (no formato: Nome, Tipo, Data, Telefone, Valor): ')
        atualizar(arq, chave_busca, novos_dados)

    elif resposta == 3:
        cabecalho('EXCLUIR CADASTRO')
        chave_busca = input('Digite o nome da pessoa a ser excluída: ')
        excluir(arq, chave_busca)

    elif resposta == 4:
        cabecalho('ADICIONAR PAGADOR')
        nome=str(input('Nome: ')).title()
        Pagadores_Mes(arq,arq_mes,nome)

    elif resposta==5:
        #opção de listar o conteudo de um arquivo
        LerArquivo(arq)

    elif resposta == 6:
        cabecalho('VENCIMENTOS PRÓXIMOS')
        DiaPag(arq)

    elif resposta == 7:
        PagamentoAtrasado(arq,arq_mes)

    elif resposta == 8:
        cabecalho('Saindo do sistema... Até mais!')
        break

    else:
        print('ERRO! Digite uma opção válida!')
    print(Linha())
    a=str(input('Digite qualquer tecla para dar continuidade: '))
