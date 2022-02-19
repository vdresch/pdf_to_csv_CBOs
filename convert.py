from tika import parser
import re
import pandas as pd

#Nome do arquivo baixado
pdf = "CBO2002_LISTA.PDF"

#Converte de PDF para texto
raw = parser.from_file(pdf)

#Série de expressões regulares que modificam o texto e encontram as CBOs, colocando em um DataFrame
pdf_string = re.sub('\n', ' ', raw['content'])
pdf_string = re.sub('Ocupação', 'Sinônimo', pdf_string)
pdf_string = re.sub('Sinônimo', '!!!Sinônimo', pdf_string)
pdf_string = re.sub(r'(?<=\d)-(?=\d)', '', pdf_string)
ocupacoes = re.findall(r'(?<=Sinônimo).*?(?=!!!)', pdf_string)

#DataFrame que será salvo
cbos = pd.DataFrame(ocupacoes, columns = ['CBO'])
cbos[['CBO', 'Nome']] = cbos['CBO'].str.split(' ', 1, expand=True)

#Salva DataFrame
cbos.to_csv("lista_cbos.csv", index=False)