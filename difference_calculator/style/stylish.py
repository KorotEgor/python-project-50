def formating(value, ind):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, list):
        return stylish(value, ind)
    return value


def stylish(status, ind=0):
    draw = ["{"]
    for row in status:
        match row["status"]:
            case "same":
                begin = "    "
            case "second":
                begin = "  + "
            case "first":
                begin = "  - "
        value = formating(row["value"], ind + 1)
        draw.append(f'{"    " * ind}{begin}{row["key"]}: {value}')
    draw.append("    " * ind + "}")
    return "\n".join(draw)
