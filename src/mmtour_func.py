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

<<<<<<< HEAD
    cidades_parametro = list(descricao_cidades.split('>'))

    for index, row in arquivo.iterrows():
        if row.isnull().any():
            print(f"Na pasta {nome_pasta} valor nulo encontrado na linha {index + 5}. Encerrando a função.")
            return 
        # Transforma as cidades do DataFrame em um conjunto
        cidades_df = list(row["Destino"].split('>'))

        # Verifica se todas as cidades do parâmetro estão contidas nas cidades da linha
        if cidades_parametro == cidades_df:
            print(f'Na pasta {nome_pasta} está contida na linha {index + 5}')
    
    return print(f'TESTE {cidades_parametro}')
=======
    cidades_parametro = set(descricao_cidades.split('>'))
    
    for index, row in arquivo.iterrows():
        if row.isnull().any():
            print(f"Valor nulo encontrado na linha {index + 5}. Encerrando a função.")
            return
        # Transforma as cidades do DataFrame em um conjunto
        cidades_df = set(row["Destino"].split('>'))

        # Verifica se todas as cidades do parâmetro estão contidas nas cidades da linha
        if cidades_parametro == cidades_df:
            print(f"As cidades {cidades_parametro} estão contidas na linha {index + 5}: {row["Destino"]}")
    
    return cidades_df
>>>>>>> 2994ced87316e6b75912acea70a89c010e537d10

def existe_rota(arquivo_rotas_internato,arquivo_extraido_do_mes):
    rotas_internato = r'E:\Rotas Professores Internato.xlsx'
    arquivo_mensal = pd.read_excel(arquivo_extraido_do_mes)
    rotas_internato = pd.ExcelFile(arquivo_rotas_internato)

    #pegando numeros unicos das rotas para comparar com o sheetname de cada planilha da rota_internato
    passageiro_lista = arquivo_mensal['Passageiro'].str.extract('(\d+)', expand=False).tolist()
    #passageiro_lista = list((dict.fromkeys(passageiro_lista)))

    for i, nome in enumerate(passageiro_lista):
        # Exemplo de condição para renomear
        if "02" in nome:
            passageiro_lista[i] = nome.replace("02", "Emanuel")
        elif "03" in nome:
            passageiro_lista[i] = nome.replace("03", "Max")
        elif "04" in nome:
            passageiro_lista[i] = nome.replace("04", "Gabriel")
        elif "06" in nome:
            passageiro_lista[i] = nome.replace("06", "Shirlei")    
        elif "09" in nome:
            passageiro_lista[i] = nome.replace("09", "Gustavo")
        elif "10" in nome:
            passageiro_lista[i] = nome.replace("10", "Ana Maria")
        elif "13" in nome:
            passageiro_lista[i] = nome.replace("13", "Edna")    

    arquivo_destino = arquivo_mensal['Destino']
<<<<<<< HEAD
=======

    for nome in passageiro_lista:
        encontrou_rota = False
        for destino in arquivo_destino:
            if compara_rota_internato(rotas_internato, nome, destino):
                encontrou_rota = True
                break  # Interrompe o loop interno assim que a condição é satisfeita
        
    if encontrou_rota:
        continue

    return print()


    """ planilhas_rotas = {}
>>>>>>> 2994ced87316e6b75912acea70a89c010e537d10

    pares_unicos = set()
    pares_pernoite = []
    index = 2
    
    par_anterior = [None,None]
    
   
    for nome, destino in zip(passageiro_lista, arquivo_destino):
        par_atual = (nome, destino, index)
        
       
        if par_atual == par_anterior or par_atual[1] == par_anterior[1]:
            pares_pernoite.append(par_atual)
            index += 1
        
        elif par_atual not in pares_unicos:
            pares_unicos.add(par_atual)
            compara_rota_internato(rotas_internato, nome, destino)
            index += 1
        
        par_anterior = par_atual
    
    return print(f'pares unicos:{list(pares_unicos)[2]}, PARES PERNOITE{pares_pernoite[2]} no index {0}')

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

<<<<<<< HEAD
    rotas_internato = r'D:\Rotas Professores Internato.xlsx'
=======
    rotas_internato = r'E:\Rotas Professores Internato.xlsx'
>>>>>>> 2994ced87316e6b75912acea70a89c010e537d10
    arquivo_mensal_internato = './empresa/Internato.xlsx'

    print(existe_rota(rotas_internato,arquivo_mensal_internato))
    #print(compara_rota_internato(rotas_internato,'Lidia','Divinópolis>São Franscisco de Paula> Boa Esperança>Cristais'))