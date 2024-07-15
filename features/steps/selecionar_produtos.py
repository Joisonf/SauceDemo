#Bibliotecas / Imports
import time
from behave import given, when, then 
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    #setup / inicialização
    context.driver = webdriver.Chrome() #instaciar o objeto do selenium WebDriver especializado para o Chrome
    context.driver.maximize_window()  #maximizar a janela do navegador
    context.driver.implicitly_wait(10) #esperar ate 10segundos
    #passo em si
    context.driver.get("https://www.saucedemo.com") #abrir o navegador no endereço do site alvo

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()


@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    #time.sleep(2) #esperar por dois segundos, depois remover = alfinete

    #teardown / encerramento
    context.driver.quit()



