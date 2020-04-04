store = []


def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]

    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)


sorted_str = sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
sorted_str = sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
sorted_str = sort_by_last_letter(['hello', 'from', 'a', 'local', 'function'])
print(sorted_str)

g = 'global'


def outer(p='param'):
    l = 'local'

    def inner():
        print(g, p, l)

    inner()


outer()
outer.inner()
