from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium_stealth import stealth


class Browser:
    def __init__(self, web_driver_path:str):
        self.web_driver_path:str = web_driver_path
        self.driver:Chrome = None

    def open_browser(self) -> None:
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")
        service = Service(self.web_driver_path)
        self.driver = webdriver.Chrome(service=service)
        
        #Bypassing Captchas
        stealth(
            self.driver,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True
        )
        #self.driver.get('https://bot.sannysoft.com')
        self.driver.get('https://www.amazon.com')

        search_bar = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
        search_bar.send_keys("MacBook Air")
        search_bar.send_keys(Keys.RETURN)

    def close_browser(self) -> None:
        if self.driver is not None:
            self.driver.quit()
