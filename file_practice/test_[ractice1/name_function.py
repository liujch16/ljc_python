def get_formmateed_name(first, last, middle = ''):#将中间名修改为可选的
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

