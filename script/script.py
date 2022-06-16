import time

from settings import SHEETS_ID, PERIOD
from credential import Authorize
from queries import CreateTable, GetTable, UpdateTable, DeleteFromTable
from rate import GetRate


def main():
    """Основная функция скрипта"""
    service = Authorize()

    # Забираем все содержимое таблицы Лист1
    request = service.spreadsheets().values().get(
        spreadsheetId=SHEETS_ID,
        range='Лист1',
        majorDimension='ROWS')

    CreateTable()
    while True:
        # Получаем актуальную таблицу из бд
        db_table = GetTable()
        # Получаем курс
        rate = GetRate()
        # Получаем актуальную таблицу из google sheets
        google_table = request.execute()['values'][1:]
        
        # Вычисляем изменения
        # Форматирование строк
        for row in google_table:
            # Подсчет стоимости в рублях по курсу
            cost_rub = round(float(row[2]) * rate, 2)
            row.append(cost_rub)
            row[0] = int(row[0])
            row[2] = int(row[2])

        # Добавление новых строк    
        update_list = tuple(
            filter(lambda row: tuple(row) not in db_table,
            google_table
            ))

        # Удаление исчезнувших строк
        delete_list = tuple(
            filter(lambda row: list(row) not in google_table,
            db_table
            ))
        
        # Если изменения есть, вносим их в бд
        changed = False

        if len(update_list) > 0:
            UpdateTable(update_list)
            changed = True

        if len(delete_list) > 0:
            DeleteFromTable(delete_list)
            changed = True

        time_now = time.ctime(time.time())
        if changed:
            print(f'{time_now}: Data base has been updated.')
        else:
            print(f'{time_now}: No changes.')

        # 
        time.sleep(PERIOD)
    
if __name__ == '__main__':
    main()