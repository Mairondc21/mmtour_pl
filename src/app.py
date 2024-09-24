from mmtour_func import juntar_planilhas, separar_empresas_por_planilha

<<<<<<< HEAD

if __name__ == "__main__":
    #exemplo
    url = "./dados/03_MAR.xls"
    caminho_empresas = r"C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\meus projetos\mmtour_pl\empresa"
=======
if __name__ == "__main__":
    #exemplo
    url = "./dados/03_MAR.xls"
    caminho_empresas = r"D:\Projetos_Programação\mmtour\mmtour_pl\empresa"
>>>>>>> 2994ced87316e6b75912acea70a89c010e537d10
    caminho_motoristas = r"C:\Users\mairon.costa\OneDrive - Expertise Inteligência e Pesquisa de Mercado\expertise_mairon\2024\meus projetos\mmtour_pl\motorista"
    df_unificado = juntar_planilhas(url)

    tratar_empresas = separar_empresas_por_planilha(
        df_unificado, "Empresa", caminho_empresas
    )
    tratar_motoristas = separar_empresas_por_planilha(
        df_unificado, "Motorista", caminho_motoristas
    )
<<<<<<< HEAD
    
    print(tratar_empresas)
    #print(tratar_motoristas)
=======
   
    print(tratar_empresas)
    print(tratar_motoristas)
>>>>>>> 2994ced87316e6b75912acea70a89c010e537d10
