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

# preencher com o usuario e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

 # preencher com o usuario em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    #não preencher o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

# preencher com o usuario, mas deixar a senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    #não preencher o senha
    context.driver.find_element(By.ID, "login-button").click()

 # Clicar no botão de login sem ter preenchido o usuario e a senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    #não preencher o usuario
    #não preencher o senha
    context.driver.find_element(By.ID, "login-button").click()


@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    #time.sleep(2) #esperar por dois segundos, depois remover = alfinete

    #teardown / encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    #validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    #teardown / encerramento
    context.driver.quit()

#verifica a mensagen para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    #validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    #teardown / encerramento
    context.driver.quit()


