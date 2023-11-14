# Экспорт точек выдачи Wildberries в Excel

Этот Python-скрипт позволяет экспортировать данные о точках выдачи из Wildberries для определенной страны и сохранять их в файл Excel.

## Содержание

- [Установка](#установка)
- [Описание методов](#описание-методов)
- [Использование](#использование)

## Установка

1. Клонируйте репозиторий на ваш компьютер:

```bash
git clone https://github.com/MRossa157/WB_Parser.git
```
2. Перейдите в директорию проекта:
```bash
cd WB_Parser
```
3. Установите необходимые зависимости с помощью pip:
```bash
pip install -r requirements.txt
```
## Описание методов
Метод ```get_all_delivery_points``` получает данные о точках выдачи в стране назначения

Метод ```make_excel_file``` создает XLSX файл с заголовками ```'Country', 'Latitude', 'Longitude', 'Adress', 'ID', 'Pickup_Type'```

Список поддерживаемых стран: ```'ru', 'by', 'kz', 'kg', 'am', 'uz', 'az'```

## Использование
1. Импортируйте класс Wildberries из скрипта:
```python
from wildberries_export import Wildberries
```
2. Создайте экземпляр класса Wildberries, указав код страны (например, 'ru'):
```python
wb = Wildberries('ru')
```
3. Получите данные о точках выдачи для указанной страны:
```python
data = wb.get_all_delivery_points()
```

4. Экспортируйте данные в файл Excel (имя файла по умолчанию - 'all_delivery_points.xlsx')
```python
wb.make_excel_file(data)
```
