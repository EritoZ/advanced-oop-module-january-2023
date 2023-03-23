def tags(html_tag):
    def func_taker(func):
        def wrapper(*args):
            result = func(*args)

            result = f'<{html_tag}>{result}</{html_tag}>'

            return result

        return wrapper

    return func_taker


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))