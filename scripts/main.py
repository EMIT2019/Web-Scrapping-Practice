import json
from browser import Browser
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

def read_json_assets(file_path:str) -> dict:
    try:
        json_object:dict = {}
        with open(file_path, "r") as json_file:
            json_object = json.load(json_file)
        return json_object
    except Exception as ex:
        print(f"THIS IS THE ERROR MESSAGE: {ex}")

def main() -> None:
    driver_path:str = r"resources\drivers\chromedriver.exe"
    json_file_path:str = r"resources\json\dom_assets.json"
    page_elements_metadata:dict = read_json_assets(json_file_path)
    url:str = 'https://www.amazon.com/?language=en_US&currency=USD'
    search_list:list[str] = ["MackBook Air Pro", "Samsung Galaxy S20", "Office chair", "Office desktop", "A/C", "LED Ligths"]
    browser:Browser = Browser(driver_path, url, page_elements_metadata)
    
    try:
        browser.open_web_page()
        values = browser.check_dom_element(xpath=page_elements_metadata["security_button"]["xpath"])

        if values["flag"]:
            values["element"].click()

        values:dict = browser.check_dom_element(id=page_elements_metadata["search_bar"]["alt_id"])

        if values["flag"]:
            values["element"].click()
            values["element"].send_keys(Keys.ENTER)

        values = browser.check_dom_element(id=page_elements_metadata["search_bar"]["id"])
        browser.make_search(search_list)

    except Exception as ex:
        print(f"THIS IS THE ERROR MESSAGE: {ex}")
        browser.close_browser()

if __name__ == "__main__":
    main()