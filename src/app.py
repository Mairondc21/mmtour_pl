from mmtour_func import juntar_planilhas, separar_empresas_por_planilha
#exemplo
url = "./dados/03_MAR.xls"
caminho_empresas = r"D:\Projetos_Programação\mmtour\empresas"
caminho_motoristas = r"D:\Projetos_Programação\mmtour\motoristas"
df_unificado = juntar_planilhas(url)

tratar_empresas = separar_empresas_por_planilha(
    df_unificado, "Empresa", caminho_empresas
)
tratar_motoristas = separar_empresas_por_planilha(
    df_unificado, "Motorista", caminho_motoristas
)
   
print(tratar_empresas)
print(tratar_motoristas)