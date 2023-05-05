
def hide_accounts(operations):
    '''Возвращает список со скрытыми счетами'''
    operations_with_hidden_acc = []
    for operation in operations:
        # Скрываем счет получателя
        # Разбиваем информацию по счету список, скрываем счет и склеиваем список обратно
        resipent_data = operation['to'].split(' ')
        hide_recip_account = '**' + resipent_data[-1][-4:]
        resipent_data[-1] = hide_recip_account
        operation['to'] = ' '.join(resipent_data)
        # Скрываем счет отправителя
        # Разбиваем информацию по счету список, скрываем счет и склеиваем список обратно
        # Делаем условие, т.к. ключ from может отсутствовать
        for key in operation:
            if key == 'from':
                sender_data = operation[key].split(' ')
                hide_sender_account = sender_data[-1][0:4] + ' ' + sender_data[-1][4:6] + '**' + ' ' + '****' + ' ' + sender_data[-1][-4:]
                sender_data[-1] = hide_sender_account
                operation[key] = ' '.join(sender_data)
        operations_with_hidden_acc.append(operation)
    return operations_with_hidden_acc





