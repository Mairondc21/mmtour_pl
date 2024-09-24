from mmtour_func import juntar_planilhas, separar_empresas_por_planilha


if __name__ == "__main__":
    #exemplo
    url = "./dados/03_MAR.xls"
    caminho_empresas = r"C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\meus projetos\mmtour_pl\empresa"
    caminho_motoristas = r"C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\meus projetos\mmtour_pl\motorista"
    df_unificado = juntar_planilhas(url)

    tratar_empresas = separar_empresas_por_planilha(
        df_unificado, "Empresa", caminho_empresas
    )
    tratar_motoristas = separar_empresas_por_planilha(
        df_unificado, "Motorista", caminho_motoristas
    )
    
    print(tratar_empresas)
    #print(tratar_motoristas)