import pandas as pd


class ExcelParser:
    """Класс для парсинга Excel-файлов."""

    def __init__(self, url_excel):
        self._url_excel = url_excel
        self.table = self.load_excel_file()
        self._rename_columns()
        self._clean_data()
        self._filter_data()

    def load_excel_file(self) -> pd.DataFrame:
        """Читает Excel-файл и возвращает DataFrame с нужными столбцами"""
        return pd.read_excel(self._url_excel, header=12, usecols=[1, 2, 3, 4, 5, 14])

    def _rename_columns(self) -> None:
        """Переименовывает столбцы DataFrame."""
        self.table.columns = ["код_инструмента", "наименование_инструмента", "базис_поставки",
                                  "объем_договора в единицах измерения", "объем_договора", "количество_договоров"
                                  ]

    def _clean_data(self) -> None:
        """Очищает данные DataFrame от первой и последних двух строк(Итого, Итого по секции)"""
        self.table = self.table.iloc[1:-2]

    def _filter_data(self) -> None:
        """Фильтрует данные DataFrame от строк, где количество договоров равно 0"""

        self.table = self.table.loc[self.table["количество_договоров"].str.strip() != "-"]

if __name__ == '__main__':
    url = "https://spimex.com/upload/reports/oil_xls/oil_xls_20250320162000.xls?r=9858"
    parser = ExcelParser(url)
    a = parser.table
    for i, row in a.iterrows():
        print(row["количество_договоров"])
