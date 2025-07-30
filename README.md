# Amazon Automated Search
This is a simple RPA / Web Scraping project as a practice. This bot takes a list of items from an Excel workbook and searches for each item on Amazon. For every search, it scrapes the first page of results and extracts three parameters: the item's title, price, and URL. All the information is stored in a separate Excel workbook.

Although it is a small project, it demonstrates how powerful Python is for scraping websites and more.

## Features

- Reads the list of articles to search from `articles.xlsx`.
- Extracts title, price, and URL from the first page of results.
- Saves the results into `results.xlsx`.
- Implements basic anti-bot bypass techniques for Amazon.
- Introduces static delays after each search to simulate human behavior (could be improved with random delays).

## Installation

```bash
# Clone the repository
git clone https://github.com/EMIT2019/Web-Scrapping-Practice.git
```
All the dependencies are inside the root of the project so it should run without any problem no matter where you execute it. 

```
📁 WEB SCRAPPING
├── 📁 .vscode
├── 📁 resources
│   ├── 📁 drivers
│   ├── 📁 files
│   │   ├── articles.xlsx
│   │   └── 📁 json
│   │       └── dom_assets.json
├── 📁 results
│   └── results.xlsx
├── 📁 scripts
│   ├── 📁 __pycache__
│   ├── browser.py
│   ├── ExcelReader.py
│   ├── ExcelResultWrite.py
│   ├── main.py
│   └── Values.py
└── README.md
```
You need the following libraries installed to run the project in your vs code whether you're using Anaconda or your default python environment.

* Pandas
* Openpyxl
* Selenium

```bash
pip install pandas openpyxl selenium
```

**Important - Make sure to have the appropriate chrome driver according to your browser version.** 

## 💡 Notes

* Delays are currently static. Consider randomizing them to better mimic human behavior
* The project was built for learning purposes and can be improved in areas like error handling, dynamic waits, and user-agent rotation.


## 🏷️ Tags

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium)
![Excel](https://img.shields.io/badge/Excel-Automation-green?logo=microsoft-excel)
![Web Scraping](https://img.shields.io/badge/Web--Scraping-Python%20%7C%20Selenium-orange)
![Practice Project](https://img.shields.io/badge/Practice-Project-lightgrey)