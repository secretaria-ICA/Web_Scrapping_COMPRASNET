from anticaptchaofficial.recaptchav2proxyless import *  # https://urldefense.com/v3/__https://anti-captcha.com/__;!!LpKI!wKmKAz-O-T_qHailt2ZI4ulA5qh_3p_ialYZiHye8VWEZ2wTXjsNKzafWxovZklwl9k$ [anti-captcha[.]com]
from anticaptchaofficial.imagecaptcha import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import time
#import pdfplumber
import re
import os
#import ctypes 

#import subprocess
import sys
### CONEXÃO COM O BANCO DO MEU SERVER HOSTGATOR ###
#import MySQLdb as db

import datetime
import shutil


##### salvar imagem da web ############
import urllib.request
#######################################


usuario = os.getlogin()
print("usuário = " + usuario)


import datetime
dt = datetime.datetime.today()
month = dt.month

hoje = datetime.datetime.today().strftime('%d/%m/%Y')
monthDoisDigitos = '{:02d}'.format(dt.month)
monthAnterior = month - 1


now = datetime.datetime.now()
ano = now.year


caminhoPastaDownloads = ("C:/Users/" + usuario + "/Downloads/")         
pasta = (caminhoPastaDownloads)


### SE EXISTIR EXCLUI O ARQUIVO .ZIP DA PASTA DOWNLOAD ##############
'''
arquivoComprov = (r"[(0-9)(\(\))]+.zip")
print ('caminho do arquivo ='+ pasta + arquivoComprov)
diretorio = os.listdir(pasta)
if arquivoComprov in diretorio:
    print('---removendo arquivo----')
    os.remove('{}/{}'.format(pasta, arquivoComprov))
    print('%s removido da pasta %s' % (arquivoComprov, pasta))
else:
    print('este arquivo nao existe') 
'''


for file in os.listdir(caminhoPastaDownloads):
    if file.endswith(".zip"):
        print(os.path.join(caminhoPastaDownloads, file))
        os.remove('{}/{}'.format(caminhoPastaDownloads, file))


######################################################################



### Acesso ao link #######################################################
#caminhoChromedriver = ("C:/Users/" + usuario + "XXXXXX/Desktop/Robo/Chromedriver/chromedriver.exe") 
caminhoChromedriver = ("C:/Users/XXXXXXXX/Robo/Chromedriver/chromedriver.exe")
driver = webdriver.Chrome(caminhoChromedriver)
#driver.maximize_window()
driver.get("https://urldefense.com/v3/__http://comprasnet.gov.br/ConsultaLicitacoes/ConsLicitacao_Filtro.asp__;!!LpKI!0SAD8aa8xX0cZ_aZwalX2MuviUIG6_ohKP4Av3v_Ddm9g9jRctLoy6Mzx3jp-m5KyY8$ [comprasnet[.]gov[.]br]")
##############################################################################

time.sleep(2)

####################### INICIO DO PREENCHIMENTO DO FORMULÁRIO ################################

###### PREENCHIMENTO DA DATA INICIAL E FINAL ###################################

dataHoje = hoje
#data1 = "14/01/2022"
#data2 = "17/01/2022"

dataIni = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "dt_publ_ini")))
dataIni.send_keys(dataHoje)
#dataIni.send_keys(data1)
#dataIni.send_keys(Keys.RETURN)  

dataFim = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "dt_publ_fim")))
dataFim.send_keys(dataHoje)
#dataFim.send_keys(data2)
#dataIni.send_keys(Keys.RETURN)  

###################################################################################################


###### ESCOLHA DE TODAS AS MODALIDADES  ######################################################

checkTodas = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmLicitacao']/table/tbody/tr[2]/td/table[2]/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[7]/td/input")))
checkTodas.click()    

###################################################################################################

###### ESCOLHA DA UNIDADE DE FEDERAÇÃO => DISTRITO FEDERAL (DF)  ###############################

btnSelecionar = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "btUf")))
btnSelecionar.click()    

##### VAI PARA O POP UP ##########################
driver.switch_to.window(driver.window_handles[-1])
##################################################

checkboxDF = driver.find_elements_by_name("chkUF")
checkboxDF[6].click()
time.sleep(2)
btnSelecionarUF = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmPesquisaUF']/table/tbody/tr[6]/td/input[3]")))
btnSelecionarUF.click()   

####### AQUI FECHA O POP UP ######################
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
####################################################################################################



###### ESCOLHA DO MATERIAL OBJETO DA PESQUISA ########################################################################################################################################

btnSelecionarMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "btMaterial")))
btnSelecionarMaterial.click()    

##### VAI PARA O POP UP ##########################
driver.switch_to.window(driver.window_handles[-1])
##################################################


######### FAZENDO A PESQUISA = COMPUTADOR #####################
pesquisa = "COMPUTADOR"
inputMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/input[1]")))
inputMaterial.send_keys(pesquisa)  

time.sleep(1)

btnOKmaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[7]/td/input[3]")))
btnOKmaterial.click()  

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[3]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[4]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[5]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[6]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[8]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[9]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[10]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[19]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[34]/td[1]/input[1]")))
checkMaterial.click()
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[37]/td[1]/input[1]")))
checkMaterial.click()

#3,4,5,6,8,9,10,19,34,37

time.sleep(1)
btnSelecionarMat = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[13]/td/input[2]")))
btnSelecionarMat.click()  

#############################################################################################################################################################

##### RETORNA AO FORMULÁRIO ##########################
driver.switch_to.window(driver.window_handles[0])
##################################################



###### ESCOLHA DO MATERIAL  ########################################################################################################################################

btnSelecionarMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "btMaterial")))
btnSelecionarMaterial.click()    

##### VAI PARA O POP UP ##########################
driver.switch_to.window(driver.window_handles[-1])
##################################################

######### FAZENDO A PESQUISA = UNIDADE DE FITA MAGNÉTICA ####################################################################################################
pesquisa = "UNIDADE DE FITA MAGNÉTICA"
inputMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/input[1]")))
inputMaterial.send_keys(pesquisa)  

time.sleep(1)

btnOKmaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[7]/td/input[3]")))
btnOKmaterial.click()  

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[3]/td[1]/input[1]")))
checkMaterial.click()

time.sleep(1)

btnSelecionarMat = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[13]/td/input[2]")))
btnSelecionarMat.click()  
##############################################################################################################################################################


time.sleep(1)

######### AQUI SAI DO POP UP #####################
driver.switch_to.window(driver.window_handles[0])
##################################################


###### ESCOLHA DO MATERIAL  ########################################################################################################################################

btnSelecionarMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "btMaterial")))
btnSelecionarMaterial.click()    

##### VAI PARA O POP UP ##########################
driver.switch_to.window(driver.window_handles[-1])
##################################################

######### FAZENDO A PESQUISA = SWITCH ####################################################################################################
pesquisa = "SWITCH"
inputMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/input[1]")))
inputMaterial.send_keys(pesquisa)  

time.sleep(1)

btnOKmaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[7]/td/input[3]")))
btnOKmaterial.click()  

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[6]/td[1]/input[1]")))
checkMaterial.click()

time.sleep(1)

btnSelecionarMat = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[13]/td/input[2]")))
btnSelecionarMat.click()  
##############################################################################################################################################################


time.sleep(1)

######### AQUI SAI DO POP UP #####################
driver.switch_to.window(driver.window_handles[0])
##################################################


###### ESCOLHA DO MATERIAL  ########################################################################################################################################

btnSelecionarMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "btMaterial")))
btnSelecionarMaterial.click()    

##### VAI PARA O POP UP ##########################
driver.switch_to.window(driver.window_handles[-1])
##################################################

######### FAZENDO A PESQUISA = UNIDADES CENTRAIS DE PROCESSAMENTO DIGITAIS ####################################################################################################
pesquisa = "UNIDADES CENTRAIS DE PROCESSAMENTO DIGITAIS"
inputMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/input[1]")))
inputMaterial.send_keys(pesquisa)  

time.sleep(1)

btnOKmaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[7]/td/input[3]")))
btnOKmaterial.click()  

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[3]/td[1]/input[1]")))
checkMaterial.click()

time.sleep(1)

btnSelecionarMat = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[13]/td/input[2]")))
btnSelecionarMat.click()  
##############################################################################################################################################################

time.sleep(1)

######### AQUI SAI DO POP UP #####################
driver.switch_to.window(driver.window_handles[0])
##################################################


###### ESCOLHA DO MATERIAL  ########################################################################################################################################

btnSelecionarMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "btMaterial")))
btnSelecionarMaterial.click()    

##### VAI PARA O POP UP ##########################
driver.switch_to.window(driver.window_handles[-1])
##################################################

######### FAZENDO A PESQUISA = UNIDADES CENTRAIS DE PROCESSAMENTO HÍBRIDAS ####################################################################################################
pesquisa = "UNIDADES CENTRAIS DE PROCESSAMENTO HÍBRIDAS"
inputMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/input[1]")))
inputMaterial.send_keys(pesquisa)  

time.sleep(1)

btnOKmaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[7]/td/input[3]")))
btnOKmaterial.click()  

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[3]/td[1]/input[1]")))
checkMaterial.click()

time.sleep(1)

btnSelecionarMat = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[13]/td/input[2]")))
btnSelecionarMat.click()  
##############################################################################################################################################################


time.sleep(1)

######### AQUI SAI DO POP UP #####################
driver.switch_to.window(driver.window_handles[0])
##################################################



###### ESCOLHA DO MATERIAL  ########################################################################################################################################

btnSelecionarMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "btMaterial")))
btnSelecionarMaterial.click()    

##### VAI PARA O POP UP ##########################
driver.switch_to.window(driver.window_handles[-1])
##################################################

######### FAZENDO A PESQUISA = ARMAZENAMENTO ####################################################################################################
pesquisa = "ARMAZENAMENTO"
inputMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/input[1]")))
inputMaterial.send_keys(pesquisa)  

time.sleep(1)

btnOKmaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[7]/td/input[3]")))
btnOKmaterial.click()  

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[13]/td[1]/input[1]")))
checkMaterial.click()

time.sleep(1)

btnSelecionarMat = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[13]/td/input[2]")))
btnSelecionarMat.click()  
##############################################################################################################################################################


time.sleep(1)

######### AQUI SAI DO POP UP #####################
driver.switch_to.window(driver.window_handles[0])
##################################################



###### ESCOLHA DO MATERIAL  ########################################################################################################################################

btnSelecionarMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "btMaterial")))
btnSelecionarMaterial.click()    

##### VAI PARA O POP UP ##########################
driver.switch_to.window(driver.window_handles[-1])
##################################################

######### FAZENDO A PESQUISA = SERVIDOR ####################################################################################################
pesquisa = "SERVIDOR"
inputMaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[5]/td/table/tbody/tr/td[2]/table/tbody/tr/td/input[1]")))
inputMaterial.send_keys(pesquisa)  

time.sleep(1)

btnOKmaterial = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[7]/td/input[3]")))
btnOKmaterial.click()  

################### 5 CHECKS ##########################################################
checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[4]/td[1]/input[1]")))
checkMaterial.click()

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[5]/td[1]/input[1]")))
checkMaterial.click()

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[7]/td[1]/input[1]")))
checkMaterial.click()

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[8]/td[1]/input[1]")))
checkMaterial.click()

checkMaterial =  WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[12]/td/table/tbody/tr[9]/td[1]/input[1]")))
checkMaterial.click()
#######################################################################################

time.sleep(1)

btnSelecionarMat = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, "//*[@id='frmMaterial']/table/tbody/tr[13]/td/input[2]")))
btnSelecionarMat.click()  
##############################################################################################################################################################


time.sleep(1)

######### AQUI SAI DO POP UP #####################
driver.switch_to.window(driver.window_handles[0])
##################################################

########## AGORA RETORNA PARA O FORMULÁRIO E CLICA EM OK PARA EXIBIR O RESULTADO DA BUSCA ###############################

btnOK = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.ID, "ok")))
btnOK.click()  

######################################################################################




######### ABRE A PÁGINA COM A RELAÇÃO DE EDITAIS PARA FAZER DOWNLOAD #####################
driver.switch_to.window(driver.window_handles[-1])
###############################################################################################


########## CLICA NO BOTÃO DE DOWNLOAD DE CADA EDITAL ###############################

for k in range(0,20):
    time.sleep(5) 

    try:        
        btnDownload = driver.find_elements_by_class_name("texField2")
       
        #print("entrou aqui no btnDownload")
        btnDownload[k].click()
    except IndexError:
        driver.close()
        driver.quit()
        break
    
    time.sleep(2)

    try:
        txtModalidade = driver.find_element_by_xpath("//*[@id='frmLicitacao']/table/tbody/tr[2]/td/table[2]/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td[1]")
        textoModalidade = txtModalidade.text
        #print("txtModalidade = " + str(txtModalidade.text))
        if textoModalidade == "Modalidades  ":
            break
        else:
            print("")
    except:
        pass

    ### EXTRAI O TITULO #######################################################################
    pegaTitulo = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table[2]/tbody/tr[2]/td/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/p")))
    pegaTitulo = pegaTitulo.text
    print("TITULO = " + str(pegaTitulo))
    ##############################################################################################


    try:       
        #btnDownload2 = driver.find_elements_by_class_name("texField2")  
        btnDownload2=  driver.execute_script("javascript:ValidaCodigo()")   
        #import pdb; pdb.set_trace()
        #time.sleep(5) #dormindo
        #btnDownload2[1].click()
    except:
        #driver.close()
        #driver.quit()
        pass

    ##############################################################################################

    


    ######### ABRIR A PÁGINA PARA REALIZAR O CAPTCHA E CONFIRMAR O DOWNLOAD ###################
    driver.switch_to.window(driver.window_handles[-1])
    ###############################################################################################

        
    ########### A PARTIR DAQUI ENTRA NA TELA DE DOWNLOAD ##################################################################

    for i in range(0,30):
        ##FAZ UM PRINTSCREEN E SALVA NA PASTA DOWNLOAD ########################
        driver.save_screenshot("C:/Users/" + usuario + "/Downloads/screenshot.png")
        ##############################################################################
       

        time.sleep(4)

        #### SOLUÇÃO PARA O CAPTCHA IMAGE TO TEXT ###################
        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key("XXXXXXXXXXXXXXXXXXXXXXXXXXXX") ## INSIRA AQUI A CHAVE SERIAL DO ANTI-CAPTCHA ##

        captcha_text = solver.solve_and_return_solution("C:/Users/" + usuario + "/Downloads/screenshot.png") 
        if captcha_text != 0:
            print("captcha text "+captcha_text)
        else:
            print("task finished with error "+solver.error_code)
        ##############################################################################


        download_dir = "C:\\Users\\" + usuario + "\\Downloads\\" 
        #options = webdriver.ChromeOptions()
        pasta = download_dir
            
        ### DESTINO DO RESULTADO DO CAPTCHA EM MAIÚSCULO PARA FACILITAR A RESOLUÇÃO ########################
        captcha_text = captcha_text.upper()
        print(captcha_text.upper())
        ###############################################################################

        time.sleep(2)

        ###### LOGIN ##############################################
        print("Realizando o captcha...")
        caixaCaptcha = driver.find_element_by_id("idLetra")
        caixaCaptcha = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idLetra']"))) 
        caixaCaptcha.clear()
        caixaCaptcha.send_keys(captcha_text)
        
        ##############################################################################


        ### BOTÃO DE LOGIN ######################################
        time.sleep(5)
        try:
            btnConfirmar = driver.find_element_by_id("idSubmit")
            btnConfirmar.click()
        except:
            pass
        #########################################################


        time.sleep(10)


        ### BUSCA DO ARQUIVO NA PASTA DOWNLOADS ############################################################# 
        sair = "0"
        for file in os.listdir(caminhoPastaDownloads):
            if file.endswith(".zip"):
                print(os.path.join(caminhoPastaDownloads, file))
                arquivoBaixado = os.path.join(caminhoPastaDownloads, file)
                if arquivoBaixado == "":
                    print("não existe arquivo .zip baixado")
                    sair = "0"
                else:
                    print("encontrei o arquivo = " + str(arquivoBaixado))  
                    sair = "1"

                                                        
                    ########## AQUI CRIA A NOVA PASTA DO DIA E COPIA OS .ZIP PARA ELA ###############################
                    usuario = os.getlogin()
                    print("usuário = " + usuario) 

                    dataHoje = datetime.datetime.today().strftime('%d-%m-%Y')
                    print(datetime.datetime.today().strftime('%d-%m-%Y'))

                    dataHojeHoraMinuto = datetime.datetime.today().strftime(' %d_%m_%Y_%H_%M_%S')
                    print(datetime.datetime.today().strftime('%d_%m_%Y_%H_%M'))


                    ## MONTAGEM DO NOME DO ARQUIVO #####################
                    pegaTitulo = str(pegaTitulo) + str(dataHojeHoraMinuto) + ".zip"
                    ##################################################################

                    #CAMINHO ORIGEM
                    origem = "C:/Users/" + usuario + "/Downloads/" 
                    print('caminho_origem_sem_arquivo =' + str(origem))

                    print("nome arquivo baixado =" + str(file))
                    print("nome do titulo do artigo =" + str(pegaTitulo)) ##->> O TITULO DO ARTIGO SE TORNA O NOME DO ARQUIVO ##

                    #CAMINHO DESTINO                    
                    destino = "C:/Users/" + usuario + "/Downloads/COMPRASNET/"+ str(dataHoje) +"/" # + str(file)
                    print('caminho_destino_sem_arquivo =' + str(destino))
                    
                    

                    if os.path.isdir(destino):
                        print("O diretório existe!")
                    else:
                        print("O diretório não existe!")
                        os.makedirs(destino)


                    #try:
                    ## COPIA DA PASTA ORIGEM PARA A PASTA DESTINO ##
                    shutil.copy2(origem + file, destino + file)
                    ## RENOMEIA O ARQUIVO QUE ACABOU DE SER COPIADO PARA A PASTA DESTINO ##
                    os.rename(destino + file, destino + pegaTitulo)
                    #except:
                    #pass                    
                    
                    ## REMOVE O ARQUIVO .ZIP QUE FOI BAIXADO ############# 
                    os.remove('{}/{}'.format(caminhoPastaDownloads, file))
                    ######################################################

                   
                                    
                    ##################################################################################################

                    break
                    
        if sair == "1":
            print("sair = 1")
            #btnFecharPopUp = driver.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[3]/td/input[3]")
            #btnFecharPopUp.click()
            break


    ### SAI DO POP UP DE DOWNLOAD ###############
    driver.switch_to.window(driver.window_handles[0])
    ##################################################

    
    
    #### CLICA NO BOTAO VOLTAR PARA A TELA COM A LISTA DE EDITAIS A SEREM BAIXADOS ##################
    try:
        btnVoltar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnVoltar")))
        print("clicou no botao de voltar")
        btnVoltar.click()
    except:
        print("entrou no except")
        #driver.close()
        #driver.quit()

    time.sleep(2)  
    ######################################################################################################


print("FIM DO PROCEDIMENTO")
driver.close()
driver.quit()  
                



 
####################################################################################################################################


