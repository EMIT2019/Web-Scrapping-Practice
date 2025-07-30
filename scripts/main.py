import json
from browser import Browser
from ExcelReader import ExcelReader
from ExcelResultWrite import ExcelResultWriter
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from Values import Values as v

def read_json_assets(file_path:str) -> dict:
    try:
        json_object:dict = {}
        with open(file_path, "r") as json_file:
            json_object = json.load(json_file)
        return json_object
    except Exception as ex:
        print(f"THIS IS THE ERROR MESSAGE: {ex}")

def main() -> None:
    #Reading and getting the data from the Excel file
    excel:ExcelReader = ExcelReader(v.EXCEL_PATH.value)
    excel.load_file_instance()
    excel.get_sheetnames()
    excel.load_worksheet()
    excel.set_articles_list()

    driver_path:str = v.DRIVER_PATH.value
    json_file_path:str = v.JSON_PATH.value
    page_elements_metadata:dict = read_json_assets(json_file_path)
    url:str = 'https://www.amazon.com/?language=en_US&currency=USD'
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
        browser.make_search(excel.articles_list)

        excel_writer:ExcelResultWriter = ExcelResultWriter("")
        excel_writer.parse_to_dataframe(browser.all_results)

    except Exception as ex:
        print(f"THIS IS THE ERROR MESSAGE: {ex}")
        browser.close_browser()

if __name__ == "__main__":
    main()