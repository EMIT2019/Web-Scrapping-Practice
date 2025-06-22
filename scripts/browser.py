from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def check_dom_element(self, element_xpath:str) -> bool:
        try:
            element_exists:bool = False
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
            wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
            
            search_bar = self.driver.find_element(By.XPATH, element_xpath)
            if search_bar.is_displayed() and search_bar.is_enabled():
                element_exists = True
            return element_exists
        except Exception as ex:
            print(f"Something went wrong during the execution. This is the full error message: {ex}")

    def close_browser(self) -> None:
        if self.driver is not None:
            self.driver.quit()
