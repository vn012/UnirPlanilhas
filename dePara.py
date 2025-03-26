import pandas as pd
from thefuzz import process, fuzz

#Leitura e tratamento da planilha de produtos
materialDe = './Planilhas/Demandas_Material.xlsx'
materialAlmx = './Planilhas/saldo_almox.xlsx'
dfMaterialDe = pd.read_excel(materialDe)
dfMaterialAlmx = pd.read_excel(materialAlmx)
df_MaterialAlmx_nome = dfMaterialAlmx['Descricao']
df_MaterialDe_nome = dfMaterialDe['DsVenda']

# Vamos comparar o primeiro valor de xProd de dfMaterialA com os 10 primeiros valores de xProd de dfMaterialB
for prod in df_MaterialAlmx_nome.head(1): 
    prod = "CONDULETE C 2"
    results = process.extract(prod, df_MaterialDe_nome.head(5000), limit=8, scorer=fuzz.token_sort_ratio)

    print(f"Produto A: {prod}")
    print("Melhores correspondências em Material B:")
    print(f"🔍 Melhores matches para \"{prod}\":")
    for match in results:
        print(f"  - {match[0]} (Similaridade: {match[1]}%)")
    print("-" * 50)