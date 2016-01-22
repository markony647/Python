def currency_converter():
    sum_to_convert = raw_input('Enter the value you need to convert: ')
    currency_lst = sum_to_convert.split()
    if currency_lst[1] == 'USD':
        result = float(currency_lst[0]) * 0.81 * 100
        rounded_result = int(result)
    elif currency_lst[1] == 'EUR':
        result = float(currency_lst[0]) * 1.22 * 100
        rounded_result = int(result)

    dollars_euro = rounded_result / 100
    cents = rounded_result % 100

    if cents == 0 and currency_lst[1] == 'USD':
        print '%d EUR' %(dollars_euro)
    elif cents and currency_lst[1] == 'EUR':
        print '%d USD' %(dollars_euro)
    elif cents != 0 and currency_lst[1] == 'USD':
        print '%d EUR and %d cents' % (dollars_euro, cents)
    else:
        print '%d USD and %d cents' % (dollars_euro, cents)