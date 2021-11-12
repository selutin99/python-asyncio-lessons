def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    for q in 'test':
        yield q


def delegator(g):
    for i in g:
        yield i


@coroutine
def cor_subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('.......', message)
    return 'Returned'


@coroutine
def cor_delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g  # replaces the code above
    print(result)


if __name__ == '__main__':
    sg = subgen()
    g = delegator(sg)
    print(next(g))

    sg_cor = cor_subgen()
    g_cor = cor_delegator(sg_cor)
    g_cor.send('Ok')
    g_cor.throw(StopIteration)
