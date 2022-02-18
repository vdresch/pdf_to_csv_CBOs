from tika import parser
import re
import pandas as pd


pdf = "CBO2002_LISTA.PDF"

raw = parser.from_file(pdf)


pdf_string = re.sub('\n', ' ', raw['content'])
pdf_string = re.sub('Ocupação', 'Sinônimo', pdf_string)
pdf_string = re.sub('Sinônimo', '!!!Sinônimo', pdf_string)
pdf_string = re.sub(r'(?<=\d)-(?=\d)', '', pdf_string)
ocupacoes = re.findall(r'(?<=Sinônimo).*?(?=!!!)', pdf_string)


cbos = pd.DataFrame(ocupacoes, columns = ['CBO'])
cbos[['CBO', 'Nome']] = cbos['CBO'].str.split(' ', 1, expand=True)

cbos.to_csv("lista_cbos.csv", index=False)