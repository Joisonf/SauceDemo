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
    self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
    self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")