#importando as biblitecas
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys

#utlizando a biblioteca requests para se conectar e extrair em uma variavel o html do site
url='https://www.tempo.com/sao-paulo.htm'
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
Page = requests.get(url,headers=headers)

#Realizando a validação se a conexão com o site deu certo
if Page.status_code == 200: #função .status_code retorna uma codificação de acordo com o tipo de retorno, no caso queremos que seja igual a 200 que significa que a requisição foi um sucesso.
    Page = Page.text
    print("Requisição bem-sucedida!")
    # Aqui você pode adicionar código para processar o conteúdo, como usar BeautifulSoup
else: #caso de errado será apresentando na tela que ocorreu uma falha e tambem o codigo. Irá finalizar o programa sem a necessidade de executar as demais linhas
    print(f"Falha na requisição. Status code: {Page.status_code}")
    sys.exit()


Soup =BeautifulSoup(Page, "html.parser")# transforma a variavel Page em um objeto onde podemos navegar e encontrar as informaçoes.

#Coletando as informações
Dia_hoje = Soup.find("li", class_="grid-item dia d1 activo")#função para extrair toda a linha do codigo
Data= Dia_hoje.find("span", class_= "subtitle-m").get_text()#extraindo com base em uma subclasse
Temp_max = Dia_hoje.find("span", class_="max changeUnitT").get_text().replace("°","")#estamos coletando o texto da classe e retirando o simbolo de temperatura que nos proximos passos não serão utilizados.
Temp_min = Dia_hoje.find("span", class_="min changeUnitT").get_text().replace("°","")
Data_coleta = datetime.now()
Form_data_coleta =str(Data_coleta.strftime("%d-%m-%Y %H:%M:%S"))#formata a data e hora para o padrão BR

#salva todos os dados coletados em uma lista
Consulta = [
    [Data,Temp_max,Temp_min,Form_data_coleta]
  
]
#imprimindo o resultado final
print(Consulta)