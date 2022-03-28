from selenium import webdriver
import time,random,smtplib,os
from selenium.webdriver import Chrome



class NotionRedacao():
    def __init__(self):
        self.ppp = webdriver.Chrome('chromedriver.exe')
        self.emailnotion = ''
        self.senhanotion = ''
        self.entNotion()
        time.sleep(3)
        lista = self.Pgredacao()
        self.tratamento(lista)

    def entNotion(self):
        try:
            self.ppp.get('LINK')
        except:
            return print('Não foi possivel entrar nesse site')
        
        while True:
            try:
                self.ppp.find_element_by_xpath('//*[@id="notion-email-input-1"]').send_keys(self.emailnotion)
                time.sleep(1)
                self.ppp.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/main/div/div[3]/div[3]/form/div[4]').click()
                time.sleep(1)
                self.ppp.find_element_by_xpath('//*[@id="notion-password-input-2"]').send_keys(self.senhanotion)
                time.sleep(1)
                self.ppp.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/main/div/div[3]/div[3]/form/div[4]').click()
                break
            except:
                pass
    


    def Pgredacao(self):
        while True:
            try:
                self.ppp.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[5]/div/a/div/div/div[1]/div').click()
                break
            except:
                pass
        
        time.sleep(3)

        redacoes = []


        for j in range(1,101):
            try:
                redacao = self.ppp.find_element_by_xpath(f'//*[@id="notion-app"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[{j}]/div/a/div/div/div[1]/div/div[2]')
                redacoes.append(redacao.text)
            except:
                break
        
        self.ppp.close()
        os.system('cls')
        
        return redacoes
    


        

    def tratamento(self,lista):
        quemja  = []
        quemnao = []

        for j in lista:
            if '#' in list(j):
                quemja.append(j)
            else:
                quemnao.append(j)


        print(quemnao[random.randint(0,len(quemnao)-1)])
        




NotionRedacao()





