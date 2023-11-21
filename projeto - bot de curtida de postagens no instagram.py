from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1200,850', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait


driver, wait = iniciar_driver()
# Entrar no site do instagram
driver.get('https://www.instagram.com/')
# Clicar e digitar meu usuário
campo_usuario = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
campo_usuario.send_keys('61994620909')
sleep(2)
# clicar e digitar minha senha
campo_senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//input[@aria-label='Senha']")))
campo_senha.send_keys('Luiss1lv@1204LR')
sleep(3)

# clicar no campo entrar
campo_entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//div[text()='Entrar']")))
sleep(2)
campo_entrar.click()
sleep(5)

while True:
    # navegar até a página alvo https://www.instagram.com/luiztaven/ (nesse caso meu próprio insta)
    driver.get('https://www.instagram.com/luiztaven')
    sleep(5)
    # clicar na última postagem 
    postagens = wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH, "//div[@class='_aagu']")))
    sleep(5)
    postagens[0].click()
    sleep(3)
    # verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 
    try:
        curtir_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Curtir']")
        sleep(2)
        curtir_button.click()
        print('publicação curtida com sucesso!')
        sleep(86400) # equivalente as 24 horas
    except:
        print('Publicação já curtida')
        sleep(86400) # equivalente as 24 horas

input('')
driver.close()
