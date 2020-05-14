def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        # 这里必须使用地板除，否则会有小数产生
        return to_str(n // base, base) + convert_string[n % base]


if __name__ == '__main__':
    print(to_str(1452, 16))

"""
5AC
"""
