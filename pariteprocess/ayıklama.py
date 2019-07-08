import pandas
import pkg_resources
import os
from pathlib import Path

class Ayıklama():

    def oku(self):
        DATA_PATH=pkg_resources.resource_filename(__name__,"listeler/")
        files = os.listdir(DATA_PATH)
        listpath = Path(DATA_PATH).joinpath("USD_TRY Geçmiş Verileri.csv")
        csvv=pandas.read_csv(listpath)
        return csvv
    def veriler(self):
        veri=self.oku()


if __name__ == "__main__":
    ds=Ayıklama()
    ds.oku()