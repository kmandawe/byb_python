def median(iterable):
    items = sorted(iterable)
    if len(items) == 0:
        raise ValueError("median() arg is an empyt sequence")
    median_index = (len(items) - 1) // 2
    if len(items) % 2 != 0:
        return items[median_index]
    return (items[median_index] + items[median_index + 1]) / 2.0


print(median([5, 2, 1, 4, 3]))

print(median([5, 2, 1, 4, 3, 6]))


# print(median([]))


def main():
    # try:
    #     median([])
    # except ValueError as e:
    #     print("Payload:", e.args)
    #     print(str(e))

    try:
        b'\x81'.decode("utf-8")
    except UnicodeError as e:
        print(e)
        print("encoding:", e.encoding)
        print("reason:", e.reason)
        print("object:", e.object)
        print("start:", e.start)
        print("end", e.end)


if __name__ == '__main__':
    main()
