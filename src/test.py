from mmtour_func import juntar_planilhas,separar_empresas_por_planilha
from app import caminho_empresas



if __name__ == "__main__":
    url = "./dados/03_MAR.xls"
    df_unificado = juntar_planilhas(url)


    tratar_empresas = separar_empresas_por_planilha(
    df_unificado, "Empresa", caminho_empresas
)