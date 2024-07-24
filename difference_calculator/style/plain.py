def formating(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, list):
        return "[complex value]"
    if isinstance(value, str):
        value = f"'{value}'"
    return value


def make_key(prv, key):
    if prv == "":
        return key

    return f"{prv}.{key}"


def plain(status, key=""):
    draw = []
    skip = False
    for i, row in enumerate(status):
        row_status = row['status']
        row_key = row['key']
        row_value = row["value"]

        match row_status:
            case "same":
                if isinstance(row_value, list):
                    draw.append(plain(row_value, make_key(key, row_key)))
                continue
            case "first":
                if len(status) - 1 == i:
                    begin = "was removed"
                    value = ""
                else:
                    next_row = status[i + 1]
                    if row_key == next_row['key']:
                        skip = True
                        begin = "was updated. From "
                        value1 = formating(row_value)
                        value2 = formating(next_row["value"])
                        value = f'{value1} to {value2}'
                    else:
                        begin = "was removed"
                        value = ""
            case "second":
                if skip:
                    skip = False
                    continue
                begin = "was added with value: "
                value = formating(row_value)

        draw.append(f"Property '{make_key(key, row_key)}' {begin}{value}")
    return "\n".join(draw)
