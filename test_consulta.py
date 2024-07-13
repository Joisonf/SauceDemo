# 1- Biblioteca - framework
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2- Classe (opcional)
class TestConsultaprodutoselecionado():

  # 2.1 Atributos
  url = "https://www.saucedemo.com"

  # 2.2 Funções e metodos
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
   # self.driver.implicithy_wait(10)

  def teardown_method(self, method):
    self.driver.quit()
  
  
  def test_Consulta(self):
    self.driver.get(self.url)
    self.driver.find_element(By.ID,"user-name").send_keys("standard_user")   #escreve o usuario
    self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")   #escreve a senha
    self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()     #clique no botão login

    #transição da pagina

    assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"