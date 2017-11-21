

def get_default(value):
    if isinstance(value, int):
        return value
    elif value == "":
        return 0
    elif isinstance(value, str):
        return int(value)


if __name__ =='__main__':
    a = get_default(10)
    b = get_default('2222')
    print(a)
    print(b)