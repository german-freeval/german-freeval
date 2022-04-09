import os
import pandas as pd
import inspect


class HBSHandler:
    def __init__(self) -> None:
        self.dirname = os.path.dirname(__file__)
        self.hbs_table_A3_4 = self.import_table(table_name="TabA3-4")
        self.hbs_table_A3_5 = self.import_table(table_name="TabA3-5")
        self.hbs_table_A3_6 = self.import_table(table_name="TabA3-6")
        self.hbs_table_A3_7 = self.import_table(table_name="TabA3-7")

    def import_table(self, table_name: str):
        table_path = os.path.join(
            self.dirname, "resources", "hbs_" + table_name + ".csv"
        )
        table = pd.read_csv(table_path, sep=";")
        return table

    def get_freeflow_speed(self, ):

        freeflow_speed = 