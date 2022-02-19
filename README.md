# Conversor para CSV do dicionário de CBOs fornecido em formato PDF #

## Por que? ##
O Ministério da Economia fornece um arquivo com os CBOs (Classificação Brasileira de Ocupações) oficiais de todas ocupações. O problema é que tal arquivo está em formato PDF, o que dificulta a utilização com softwares estatísticos e de planilha. Ainda, essa classificação é revisada com frequência. O objetivo aqui é uma forma automatizada de converter esse PDF para um arquivo CSV.

Para maior comodidade, e para fins de exemplo, no diretório já há um arquivo convertido em 02/2022.
## Como utilizar ##
O script é em python e utiliza apenas três bibliotecas:
```
tika
re
pandas
```
Para a excecução, primeiro é preciso baixar o PDF para a conversão no site do [MTE](http://www.mtecbo.gov.br/cbosite/pages/downloads.jsf). Esse arquivo deve estar no mesmo diretório do programa.

Para excecutar, é só exceutar convert.py.
```
python convert.py
```
