# Amazon Automated Search
This is a very very small and basic RPA / Web Scrapping project as a practice. This bot basically takes a list of items from an Excel workbook and then makes a search one by one, and for each search takes the first page results and for each result takes 3 parameters, the url, the price and the title of the item, then all the information is store in another Excel workbook, as simple as that, but evendough is small, it demostrates how powerfull is python por scrap websites and more.

## Features

- The bot takes all the content from the articles.xlsx so you can put there as many articles to search as you may want
- I developed a solution to bypass Amazon’s anti-bot mechanisms.
- To make the behavior of the bot more human I added some delay after each search, however those delays use static values so always the delay after a search is the same, so I probabbly shoud have implemented a logic to randomly set a value for the delay after each search.

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
You need the following libraries installed to run the project in your vs code wether you're using Anaconda or your default python enviroment.

* Pandas
* Openpyxl
* Selenium

**Note: Make sure to have the appropriate chrome driver according your browser version.** 