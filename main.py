import requests
from openpyxl import Workbook


class Wildberries():
    def __init__(self, country: str, debug: bool = False):
        '''
        country in ['ru', 'by', 'kz', 'kg', 'am', 'uz', 'az']
        '''
        self._debug = debug
        self.country = country.lower()

    def get_all_delivery_points(self) -> dict:
        data = requests.get('https://static-basket-01.wb.ru/vol0/data/all-poo-fr-v8.json').json()

        for item in data:
            if item['country'] == self.country:
                required_data = item

        return required_data

    def make_excel_file(self, data, filename: str = 'all_delivery_points.xlsx') -> None:
        wb = Workbook()
        ws = wb.active

        ws.append(['Country', 'Latitude', 'Longitude', 'Adress', 'ID', 'Pickup_Type', 'isWb', 'dest', 'sign'])

        try:
            for item in data['items']:
                country = self.country.upper()
                lat, lon = item.get('coordinates', [None, None])
                address = item.get('address', None)
                id = item.get('id', None)
                pickup_type = item.get('pickupType', None)
                isWb = item.get('isWb')
                dest = item.get('dest', None)
                sign = item.get('sign', None)
                ws.append([country, lat, lon, address, id, pickup_type, isWb, dest, sign])

        except Exception as e:
            raise e
            # Сюда можно добавить какой то логгер ошибок

        # Сохранение файла
        wb.save(filename)

        print('Файл успешно создан!')


def main():
    wb = Wildberries('ru')
    data = wb.get_all_delivery_points()
    wb.make_excel_file(data)


if __name__ == '__main__':
    main()
