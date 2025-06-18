from browser import Browser
import time

def main() -> None:
    driver_path:str = r"resources\drivers\chromedriver.exe"
    browser:Browser = Browser(driver_path)
    browser.open_browser()
    time.sleep(30)
    browser.close_browser()
if __name__ == "__main__":
    main()
    