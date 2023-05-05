
def reformate_date(executed_operations):
    """Возвращает список с необходимым форматом даты"""
    reformate_date_operations = []
    for operation in executed_operations:
        only_date = operation['date'].split('T')[0]
        new_date_list = only_date.split('-')
        new_date = new_date_list[2] + '.' + new_date_list[1] + '.' + new_date_list[0]
        operation['date'] = new_date
        reformate_date_operations.append(operation)
    return reformate_date_operations


def sorting(operations):
    """Сортирует список словарей по дате"""
    return sorted(operations, key=lambda k: '.'.join(reversed(k['date'].split('.'))))[::-1]

