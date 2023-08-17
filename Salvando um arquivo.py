import pandas as pd

#adicionar pasta1
pasta1 = pd.read_excel("Pasta1.xlsx")

#adiciona pasta2
pasta2 = pd.read_excel("Pasta2.xlsx")

#atualiza a pasta1 com as informações da pasta2
pasta1 = pasta1._append(pasta2)

print(lista)

#salvar
salvar = pd.ExcelWriter("pasta_salvar/lista13.xlsx")
pasta1.to_excel(salvar, "pasta_salvar", index=False)
salvar._save()
