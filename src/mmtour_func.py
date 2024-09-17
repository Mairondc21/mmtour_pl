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

if __name__ == '__main__':
   pass 