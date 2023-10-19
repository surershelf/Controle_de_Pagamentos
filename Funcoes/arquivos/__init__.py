from Funcoes.format import *
import datetime


def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(',')
            nome = dado[0].strip()
            tipo_pag = dado[1].strip()
            data = dado[2].strip()
            telefone = dado[3].strip()
            valor_parcela = dado[4].strip()
            print(f'Nome: {nome}')
            print(f'Tipo: {tipo_pag}')
            print(f'Data de Vencimento: {data}')
            print(f'Telefone: {telefone}')
            print(f'Valor da Parcela: R${valor_parcela}')
            print(Linha())
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', tipo_pag='desconhecido', data=00, telefone='0', valor_parcela=0.00):
    try:
        with open(arq, 'a') as a:
            nome_str = str(nome).strip()
            tipo_pag_str = str(tipo_pag).strip()
            data_str = str(data).strip()
            telefone_str = str(telefone).strip()
            valor_parcela_str = f'{valor_parcela:.2f}'
            a.write(f'{nome_str.title()}, {tipo_pag_str.title()}, {data_str}, {telefone_str}, {valor_parcela_str}\n')
        print(f'Novo registro de {nome_str.title()} adicionado')
    except Exception as e:
        print(f'Houve um ERRO na hora de escrever os dados: {e}')

def atualizar(arq, chave_busca, novo_dado):
    try:
        with open(arq, 'r') as arquivo_orig:
            linhas = arquivo_orig.readlines()

        chave_encontrada = False  # Variável para verificar se a chave de busca foi encontrada

        with open(arq, 'w') as arquivo_atualizado:
            for linha in linhas:
                if chave_busca in linha:
                    linha_atualizada = linha.replace(chave_busca, novo_dado)
                    arquivo_atualizado.write(linha_atualizada)
                    chave_encontrada = True  # Marca a chave como encontrada
                else:
                    arquivo_atualizado.write(linha.title())

        if chave_encontrada:
            print("Dado atualizado com sucesso!")
        else:
            print(f"Chave de busca '{chave_busca}' não encontrada no arquivo. Nenhum registro foi atualizado.")

    except FileNotFoundError:
        print(f"Arquivo '{arq}' não encontrado.")
    except Exception as e:
        print(f"Erro ao atualizar o arquivo: {e}")



def excluir(arq, nome):
    try:
        with open(arq, 'r') as arquivo_orig:
            linhas = arquivo_orig.readlines()

        chave_encontrada = False  # Variável para verificar se o nome foi encontrado

        with open(arq, 'w') as arquivo_atualizado:
            for linha in linhas:
                if not chave_encontrada and nome.lower() == linha.split(',')[0].strip().lower():
                    chave_encontrada = True
                else:
                    arquivo_atualizado.write(linha)

        if chave_encontrada:
            print(f"Registro de '{nome}' excluído com sucesso!")
        else:
            print(f"Nome '{nome}' não encontrado no arquivo. Nenhum registro foi excluído.")

    except FileNotFoundError:
        print(f"Arquivo '{arq}' não encontrado.")
    except Exception as e:
        print(f"Erro ao excluir o registro: {e}")


def DiaPag (arq):
    try:
        with open(arq, 'r') as arquivo_orig:
            linhas = arquivo_orig.readlines()
            data_atual = datetime.date.today()
            dia_atual = data_atual.day
            dias_proximos = dia_atual + 7
            for linha in linhas:
                dado = linha.split(',')
                nome = dado[0].strip()
                data_text = dado[2].strip()
                data= int(data_text)
                telefone = dado[3].strip()
                if data >= dia_atual and data <= dias_proximos:
                    print(f'Nome: {nome} - Vencimento Dia: {data} - Telefone:{telefone}\t')


    except FileNotFoundError:
        print(f"Arquivo '{arq}' não encontrado.")

def Pagadores_Mes(arq1,arq2,chave_busca):
    try:
        with open(arq1, 'r') as arquivo_orig:
            linhas = arquivo_orig.readlines()

        chave_encontrada = False  # Variável para verificar se a chave de busca foi encontrada

        with open(arq1, 'r'):
            for linha in linhas:
                if chave_busca in linha:
                    with open(arq2, 'a') as pago:
                        pago.write(linha)
                        chave_encontrada = True  # Marca a chave como encontrada
        if chave_encontrada:
            print("Dado atualizado com sucesso!")
        else:
            print(f"Chave de busca '{chave_busca}' não encontrada no arquivo. Nenhum registro foi atualizado.")

    except FileNotFoundError:
        print(f"Arquivo '{arq1}' ou '{arq2}' não encontrados.")

    except Exception as e:
        print(f"Erro ao atualizar o arquivo: {e}")


def PagamentoAtrasado(arq, arq1):
    try:
        with open(arq, 'r') as arquivo_orig:
            linhas = arquivo_orig.readlines()
        with open(arq1, 'r') as arquivo_orig1:
            linhas1 = arquivo_orig1.readlines()

        pessoas_em_arq1 = set()
        data_atual = datetime.date.today()
        dia_atual = data_atual.day

        for linha1 in linhas1:
            dado1 = linha1.split(',')
            if len(dado1) >= 5:
                nome1 = dado1[0].strip()
                pessoas_em_arq1.add(nome1)

        cabecalho('PESSOAS QUE NÃO PAGARAM ESTE MÊS')
        for linha in linhas:
            dado = linha.split(',')
            if len(dado) >= 5:
                nome = dado[0].strip()
                data = int(dado[2])
                if dia_atual > data:
                    if nome not in pessoas_em_arq1:  # Verifica se o nome não está em arq1
                        tipo_pag = dado[1].strip()
                        telefone = dado[3].strip()
                        valor_parcela = dado[4].strip()

                        print(f'Nome: {nome}')
                        print(f'Tipo: {tipo_pag}')
                        print(f'Data de Vencimento: {data}')
                        print(f'Telefone: {telefone}')
                        print(f'Valor da Parcela: R${valor_parcela}')
                        print(Linha())

    except FileNotFoundError:
        print(f"Arquivo '{arq}' ou '{arq1}' não encontrado.")
    except Exception as e:
        print(f"Erro!!! {e}")

