from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service =servico)

navegador.get("https://pep.celesc.com.br/PEP/externo/login.xhtml")
navegador.find_element('xpath', '//*[@id="j_idt12:loginUsuario"]').send_keys('xxx')
navegador.find_element('xpath', '//*[@id="j_idt12:loginSenhaUsuario"]').send_keys('xxx')

loginbutton = navegador.find_element('xpath', '/html/body/div[1]/div[2]/div/section/form/div[3]/button')
navegador.execute_script('arguments[0].click();', loginbutton)

input("Pressione Enter para fechar o navegador...")
navegador.quit()