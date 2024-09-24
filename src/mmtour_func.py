import pandas as pd


def juntar_planilhas(excel_file):
    # Carregar todas as planilhas do arquivo Excel
    xls = pd.ExcelFile(excel_file)

    # Lista para armazenar os DataFrames
    df_list = []

    # Iterar por cada nome de planilha e armazenar os dados em um DataFrame
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name, header=1, usecols="B:I")
        df["Data"] = sheet_name  # Adicionar o nome da planilha em uma nova coluna
        df["Data"] = df["Data"].astype(str) + "/3"
        df = df.dropna(subset=["Passageiro"])

        mover_data = df.pop("Data")
        df.insert(0, "Data", mover_data)
        df["Empresa"] = df["Empresa"].fillna("nao informado")
        df["Motorista"] = df["Motorista"].fillna("nao informado")

        df_list.append(df)

    # Concatenar todos os DataFrames em um único DataFrame
    df_concatenado = pd.concat(df_list, ignore_index=True)
    df_geral = df_concatenado.to_excel("geral/geral.xlsx")

    return df_concatenado


def separar_empresas_por_planilha(df, nome_coluna, caminho_pasta):
    # Obtendo os valores únicos da coluna "Empresa"
    empresas_unicas = df[nome_coluna].unique()

    # Iterando sobre cada empresa única
    for empresa in empresas_unicas:
        # Filtrando o DataFrame apenas para a empresa atua
        df_empresa = df[df[nome_coluna] == empresa]

        # Criando um nome de arquivo para a planilha
        nome_arquivo = f"{caminho_pasta}/{empresa}.xlsx"

        # Salvando o DataFrame filtrado em uma planilha Excel
        df_empresa.to_excel(nome_arquivo, index=False)
        print(f"Planilha para {empresa} salva em {nome_arquivo}")


def compara_rota_internato(url,nome_pasta, descricao_cidades):
    arquivo = pd.read_excel(url,sheet_name=nome_pasta, header=3)
    arquivo = arquivo[["Destino"]]

    cidades_parametro = set(descricao_cidades.split('>'))

    for index, row in arquivo.iterrows():
        if row.isnull().any():
            print(f"Na pasta {nome_pasta} valor nulo encontrado na linha {index + 5}. Encerrando a função.")
            return 
        # Transforma as cidades do DataFrame em um conjunto
        cidades_df = set(row["Destino"].split('>'))

        # Verifica se todas as cidades do parâmetro estão contidas nas cidades da linha
        if cidades_parametro == cidades_df:
            print(f'Na pasta {nome_pasta} está contida na linha {index + 5}')
    
    return index + 5

def existe_rota(arquivo_rotas_internato,arquivo_extraido_do_mes):
    arquivo_mensal = pd.read_excel(arquivo_extraido_do_mes)
    
    df_novo = arquivo_mensal[['Passageiro','Destino']]
    print(df_novo)

    #pegando numeros unicos das rotas para comparar com o sheetname de cada planilha da rota_internato
    df_novo['Passageiro_tratado'] = df_novo['Passageiro'].str.extract('(\d+)', expand=False)
    #passageiro_lista = list((dict.fromkeys(passageiro_lista)))
    print(df_novo[['Passageiro_tratado','Destino']])

    passageiro_lista = df_novo['Passageiro_tratado'].tolist()  # Convertendo a coluna 'Passageiro_tratado' para lista
    destino_lista = df_novo['Destino'].tolist()  # Convertendo a coluna 'Destino' para lista

    # Criando novas listas para armazenar os valores não repetidos consecutivamente
    nova_passageiro_lista = [passageiro_lista[0]]
    nova_destino_lista = [destino_lista[0]]

    # Percorrendo a lista de 'Passageiro_tratado' e 'Destino' e aplicando a condição
    for i in range(1, len(passageiro_lista)):
        if passageiro_lista[i] != passageiro_lista[i - 1]:  # Comparando passageiro com o anterior
            nova_passageiro_lista.append(passageiro_lista[i])
            nova_destino_lista.append(destino_lista[i])

    # Criando um novo DataFrame com os valores únicos de Passageiro_tratado e Destino
    

    

    for i, nome in enumerate(nova_passageiro_lista):
        # Exemplo de condição para renomear
        if "02" in nome:
            nova_passageiro_lista[i] = nome.replace("02", "Emanuel")
        elif "03" in nome:
            nova_passageiro_lista[i] = nome.replace("03", "Max")
        elif "04" in nome:
            nova_passageiro_lista[i] = nome.replace("04", "Gabriel")
        elif "06" in nome:
            nova_passageiro_lista[i] = nome.replace("06", "Shirlei")    
        elif "09" in nome:
            nova_passageiro_lista[i] = nome.replace("09", "Gustavo")
        elif "10" in nome:
            nova_passageiro_lista[i] = nome.replace("10", "Ana Maria")
        elif "13" in nome:
            nova_passageiro_lista[i] = nome.replace("13", "Edna")    

   
    pares_unicos = []
    pares_pernoite = []
    index_planilha_mensal = 2
    index_planilha_internato = None
    
    par_anterior = [None,None,None,None]
    
   
    for nome, destino in zip(nova_passageiro_lista, nova_destino_lista):
        par_atual = (nome, destino, index_planilha_mensal,index_planilha_internato)
        par_anterior
        if par_atual not in pares_unicos:
            
            arquivo = pd.read_excel(arquivo_rotas_internato,sheet_name=nome, header=3)
            arquivo = arquivo[["Destino"]]

            cidades_df_anterior = None 
            cidades_parametro = set(destino.split('>'))

            for index_planilha_internato, row in arquivo.iterrows():
                if row.isnull().any():
                    print(f"Na pasta {nome} valor nulo encontrado na linha {index_planilha_internato + 5}. Encerrando a função.")
                    break  # sai do loop atual e passa para o próximo item na lista `zip(passageiro_lista, arquivo_destino)`
                
                 
                cidades_df = set(row["Destino"].split('>'))

                if cidades_parametro == cidades_df:
                    print(f'Na pasta {nome} a rota está contida na linha {index_planilha_internato + 5}')
                    # Verifica se todas as cidades do parâmetro estão contidas nas cidades da linha
                    if cidades_df == cidades_df_anterior:
                        pares_pernoite.append([nome,destino, index_planilha_mensal + 1,index_planilha_internato + 5])
                    else:
                        pares_unicos.append([nome,destino, index_planilha_mensal + 1,index_planilha_internato + 5])
                    
                    # Atualiza cidades_df_anterior para ser a atual cidades_df
                    cidades_df_anterior = cidades_df   
            index_planilha_mensal += 1
            
        par_anterior = par_atual

    return print(f'\n\nLINHAS JA CONTIDAS = {pares_unicos} \n\nPERNOITES = {pares_pernoite} ')


    """ planilhas_rotas = {}
    for nome in passageiro_lista:
        if nome in rotas_internato.sheet_names:  # Verifica se o nome existe como planilha
            # Lê a planilha e armazena no dicionário
            planilhas_rotas[nome] = pd.read_excel(rotas_internato, sheet_name=nome)
            print(f"Planilha {nome} carregada com sucesso!")
            
        else:
             print(f"A planilha {nome} não existe no arquivo.")
    
    print(planilhas_rotas) """

if __name__ == '__main__':

    rotas_internato = r'D:\Rotas Professores Internato.xlsx'
    arquivo_mensal_internato = './empresa/Internato.xlsx'
    #ordem 1ª nome da pasts, 2ªdestino, 3ª index da planilha mensal, 4ª index da planilha rotas_internato
    print(existe_rota(rotas_internato,arquivo_mensal_internato))
    #print(compara_rota_internato(rotas_internato,'Lidia','Divinópolis>São Franscisco de Paula> Boa Esperança>Cristais'))