import json

# Выносим путь к файлу json в константу
OPERATIONS = "/home/rusanov/Skypro_study/Course_3/course_work/project_operations/data/operations.json"


def load_operations():
    '''Возвращает список операций'''
    with open(OPERATIONS, encoding='utf8') as file:
        operations = json.loads(file.read())
        return operations


def get_executed_operations(operations):
    '''Возвращает список выполненных операций'''
    executed_operations = []
    for operation in operations:
        for key in operation:
            if operation[key] == 'EXECUTED':
                executed_operations.append(operation)
    return executed_operations
