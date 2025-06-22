from browser import Browser
import time

def main() -> None:
    driver_path:str = r"resources\drivers\chromedriver.exe"
    search_bar_xpath:str = "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input"

    browser:Browser = Browser(driver_path)
    browser.open_browser()
    value = browser.check_dom_element(search_bar_xpath)
    print(f"THIS IS THE VALUE OF THE VARIABLE VALUE: {value}")
    time.sleep(30)
    browser.close_browser()
if __name__ == "__main__":
    main()
    