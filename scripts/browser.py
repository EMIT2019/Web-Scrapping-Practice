import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class Browser:
    def __init__(self, web_driver_path:str, web_url:str, page_elements_metadata:dict):
        self.web_driver_path:str = web_driver_path
        self.web_page_url:str = web_url
        self.driver:Chrome = None
        self.page_elements:dict = page_elements_metadata

    def open_web_page(self) -> None:
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        options.add_argument("--start-maximized")
        service = Service(self.web_driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        
        #Bypassing Captchas
        stealth(
            self.driver,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True
        )

        self.driver.get(self.web_page_url)

    def check_dom_element(self, id:str = None, xpath:str = None) -> bool:
        try:
            parameter = None
            element_value:str = ""

            if id is not None:
                parameter = By.ID
                element_value = id
            elif xpath is not None:
                element_value = xpath
                parameter = By.XPATH

            element_exists:bool = False
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((parameter, element_value)))
            wait.until(EC.element_to_be_clickable((parameter, element_value)))
            dom_element = self.driver.find_element(parameter, element_value)
            if dom_element.is_displayed() and dom_element.is_enabled():
                element_exists = True
                return {"flag":element_exists, "element":dom_element}
            else:
                element_exists = False
                return {"flag":element_exists, "element":dom_element}
        except Exception as ex:
            print(f"Something went wrong during the execution. This is the full error message: {ex}")
            return {"flag":False, "element":None}

    def make_search(self, search:list[str] | str = None) -> None:
        try:
            element_id:str = self.page_elements["search_bar"]["id"]
            flag = self.check_dom_element(id=element_id)["flag"]
            if flag:
                if isinstance(search, list):
                    for item in search:
                        search_bar:WebElement = self.check_dom_element(id=element_id)["element"]
                        search_bar.clear()
                        search_bar.send_keys(item)
                        search_bar.send_keys(Keys.ENTER)
                        time.sleep(3)
                elif isinstance(search, str):
                    search_bar.send_keys(search)
                    search_bar.send_keys(Keys.ENTER)
                    time.sleep(3)
            else:
                self.close_browser()
        except Exception as ex:
            print(f"Something went wrong during the execution. This is the full error message: {ex}")

    def close_browser(self) -> None:
        if self.driver is not None:
            self.driver.quit()
