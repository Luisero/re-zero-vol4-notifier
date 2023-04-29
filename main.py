from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from EmailSender import EmailSender

class Scrapper():
    def __init__(self,url) -> None:
        
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.url = url

        self.browser.get(url)

    def get_book_price(self):
        try:
            
            price_span = self.browser.find_element(By.CSS_SELECTOR, '.a-size-medium.a-color-price.header-price.a-text-normal')
            return price_span.text
        except:
            return None 
        
    def send_email(self):
        email_sender = EmailSender()
        email = environ.get('EMAIL','.')
        password = environ.get('PASSWORD','.')

        email_destination = 'luismoura2005@gmail.com'
        subject = 'Boas notícias sobre Re:zero vol 4 Luis!'

        html_text = '''
            <h1>Re:zero vol 4 está de volta ao estoque da amazon Luis!</h1>
            <p>Se eu fosse você já ia comprar antes que acabe</p>
            <img src="https://m.media-amazon.com/images/I/511wUksYqoL._SX370_BO1,204,203,200_.jpg" />
        '''
        email_sender.enviarEmail(email,password, html_text, email_destination,subject)
        



scrapper = Scrapper('https://www.amazon.com.br/dp/8583621535/?colid=1PA81P3P0Z0YJ&coliid=I21YBS4IM7N5UB&ref_=gv_ov_lig_pab')

price = scrapper.get_book_price()

if price != None:
    scrapper.send_email()