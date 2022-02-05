from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Olá pessoal! Sejam bem-vindos aos nosso canal de comunicação interna do RH."
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Help", "Comprovantes"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        # Código Grupo - <span dir="auto" title="Help" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Help</span>
        # Código caixa texto - <div tabindex="-1" class="p3_M1">
        # Código send - <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(5)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(5)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(5)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
