"10110101"
data = str(input())
data = list(data)

data_error = str(input())
data_error = list(data_error)

def col_bit_control(len_date):
    for i in range(len_date):
        if 2**i >= len_date + 1:
            return int(i)


def insert_bit_control_x(data):
    l = len(data)
    col = col_bit_control(l)
    data_bit_control_zero = [1 for _ in range(l + col)]

    for i in range(l + col):
        fl = True
        for j in range(col):
            if i == (2**j - 1):
                data_bit_control_zero[i] = "x"
                fl = False
                break
        if fl:
            data_bit_control_zero[i] = data.pop(0)

    return data_bit_control_zero


def count_bit_control(data):
    l = len(data)
    bit_control_x = insert_bit_control_x(data)
    col = col_bit_control(l)

    control_value = []
    for i in [2**i for i in range(col)]:
        pos_dop_bit = []
        for j in range(i-1, len(bit_control_x), i*2):
                for q in range(j, i+j):
                    if q < len(bit_control_x):
                        pos_dop_bit.append(q)

        spec_pos = sum([int(bit_control_x[i]) for i in pos_dop_bit if bit_control_x[i].isdigit()])
        control_value.append(0) if spec_pos % 2 == 0 else control_value.append(1)

    control_value_copy = control_value.copy()
    for i in range(len(bit_control_x)):
        if bit_control_x[i] == 'x':
            bit_control_x[i] = control_value.pop(0)

    print(bit_control_x)

    return control_value_copy


def check_error(data_error, data):
    print("Исходные данные с контрольными битами: ")
    bit_control_data = count_bit_control(data)
    print(bit_control_data)
    print()
    print("Переданные  данные с контрольными битами: ")
    bit_control_error_data = count_bit_control(data_error)
    print(bit_control_error_data)


    position_error = 0
    for i in range(len(bit_control_data)):
        if bit_control_data[i] != bit_control_error_data[i]:
            position_error += 2**i

    print("Позиция ошибки: " , position_error)

check_error(data_error, data)

