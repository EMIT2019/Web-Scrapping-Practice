import pandas as pd
from pandas import DataFrame

class ExcelResultWriter:
    def __init__(self, save_path:str) -> None:
        self.save_path = save_path
        self.result_df:DataFrame = DataFrame()

    def parse_to_dataframe(self, result_list:list[dict]) -> DataFrame:
        try:
            new_dataframe:DataFrame = pd.DataFrame(columns=["result_url", "result_name", "result_price"]) 

            for idx, item in enumerate(result_list):
                new_dataframe.at[idx, "result_url"] = item["item_url"]
                new_dataframe.at[idx, "result_name"] = item["item_title"]
                new_dataframe.at[idx, "result_price"] = item["item_price"]
            new_dataframe.to_excel("results/results.xlsx")
        except Exception as ex:
            print(f"Something went wrong during the execution. This is the full error message: {ex}")
