from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


navegador = webdriver.Chrome(r'C:\PYTHON\MeusProgramas\programas.py\chromedriver.exe')

l_temperatura = []
guardar_noticias = []
contatos = ['O mais', 'Geeh']
def buscar_temp():
    navegador.get('https://www.google.com.br/')
    barra_pesquisa = navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    barra_pesquisa.click()
    barra_pesquisa.send_keys('Temperatura sp-franco da rocha')
    sleep(2)
    barra_pesquisa.send_keys(Keys.ENTER)
    sleep(5)
    #Pegando temperatura
    temperatura = navegador.find_element_by_xpath('//*[@id="wob_tm"]')
    l_temperatura.append(temperatura.text)
    sleep(2)


def buscando_noticias():
    navegador.get('https://g1.globo.com/sp/sao-paulo/')
    sleep(2)
    noticias = navegador.find_element_by_class_name('_b')
    guardar_noticias.append(noticias.text)
    for noticias in guardar_noticias:
        return f'Noticias G1\n\n{noticias}'


def buscar_contato(contato):
    navegador.get('https://web.whatsapp.com')
    sleep(30)
    campo_pesquisa = navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    sleep(4)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(2)
    

def enviar_mensagem(*mensagem):
    campo_mensagem = navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]') 
    campo_mensagem.click()
    sleep(3)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)
    

mensagens = []
def chama_funcoes():
    buscar_temp()
    noticia = buscando_noticias()
    mensagem = f'TEMPERATURA: {l_temperatura[0]}ºC Não esqueça de tomar água :)'
    mensagens.append(noticia)
    mensagens.append(mensagem)
    
    
    for contato in contatos:
        buscar_contato(contato)
        for mens in mensagens:
            enviar_mensagem(mens)
            sleep(5)
            try:
                alerta = navegador.switch_to.alert
                alerta.accept()
            except:
                continue
cont = 0
while True:
    chama_funcoes()
    cont += 1
    if cont == 4:
        break
    sleep(900)


    