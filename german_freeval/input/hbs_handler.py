import os

import pandas as pd


class HBSHandler:
    def __init__(self) -> None:
        self.dirname = os.path.dirname(__file__)
        self.hbs_table_A3_2 = self.import_table(table_name="TabA3-2")
        self.hbs_table_A3_3 = self.import_table(table_name="TabA3-3")
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

    def get_parameters_equation_A3_7(
        self,
        slope: float,
        heavy_vehicle_share: float,
        lanes: int,
        ballungsraum: bool,
        speed_limit: int,
        has_zra: bool,
    ):
        V_0 = None  # TODO
        L_0 = None
        C_0 = None
        C = None
        v_krit = None

        return V_0, L_0, C_0, C, v_krit

    def hbs_equation_A3_7(self, q: int, V_0: float, L_0: float, C_0: int, C: int):
        v_hbs = V_0 / (1 + (V_0 / (L_0 * (C_0 - q))))
        return v_hbs

    def hbs_freeflow_speed(
        self,
        slope: float,
        heavy_vehicle_share: float,
        lanes: int,
        ballungsraum: bool,
        speed_limit: int,
        has_zra: bool,
    ):
        q = 0
        V_0, L_0, C_0, C, v_krit = self.get_parameters_equation_A3_7(
            slope, heavy_vehicle_share, lanes, ballungsraum, speed_limit, has_zra
        )

        freeflow_speed = self.hbs_equation_A3_7(q, V_0, L_0, C_0, C)

        return freeflow_speed

    def hbs_capacity(
        self,
        slope: float,
        heavy_vehicle_share: float,
        lanes: int,
        ballungsraum: bool,
        speed_limit: int,
        has_zra: bool,
    ):  # TODO
        capacity = None
        return capacity

    def hbs_jam_density(
        self,
        lanes: int,
        heavy_vehicle_share: float,
        vehicle_length: float = 4.5,
        heavy_vehicle_length: float = 12,
        distance_headway: float = 2,
    ):
        jam_density = 1000 / (
            (1 - heavy_vehicle_share) * (vehicle_length + distance_headway)
            + (heavy_vehicle_share * (heavy_vehicle_length + distance_headway))
        )
        return jam_density
