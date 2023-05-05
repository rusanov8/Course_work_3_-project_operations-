from utils_json import *
from utils_dates import *
from utils_accounts import *

# Переменная с количеством выводимых операций
OPERATIONS_COUNT = 5

def main():
    # Каждая функкия постепенно преобразовывает список словарей в необходимый для вывода вид
    operations = load_operations()
    executed_operations = get_executed_operations(operations)
    reformat_date_operations = reformate_date(executed_operations)
    sorted_by_date_operations = sorting(reformat_date_operations)
    operations_with_hidden_acc = hide_accounts(sorted_by_date_operations)

    # Оставляем в списке только необходимое кол-во операций
    del operations_with_hidden_acc[OPERATIONS_COUNT:]

    # Выводим информацию с помощью цикла
    for operation in operations_with_hidden_acc:
        print(operation["date"], operation["description"])
        # Делаем условие, т.к. ключ from может отсутствовать
        if 'from' in operation:
            print(operation['from'], '->', operation['to'])
        else:
            print('->', operation['to'])
        print(operation['operationAmount']['amount'],operation['operationAmount']['currency']['name'])
        print()


if __name__ == '__main__':
    main()
