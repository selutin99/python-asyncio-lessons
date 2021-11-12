from inspect import getgeneratorstate


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def subgen():
    message = yield
    print('Subgen received: ', message)


def subgen2():
    x = 'Ready to accept the message'
    message = yield x
    print('Subgen received: ', message)


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)


@coroutine
def average_return():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average


if __name__ == '__main__':
    g = subgen()
    g.send(None)
    print(getgeneratorstate(g))
    # g.send('qwerty')  # Stop Iteration
    # print(getgeneratorstate(g))

    g = subgen2()
    g.send(None)
    # g.send('qwerty')  # Stop Iteration
    # print(getgeneratorstate(g))

    g = average()
    print(g.send(4))
    print(g.send(5))
    print(g.send(10))
    g.throw(StopIteration)

    g = average_return()
    g.send(5)
    g.send(6)
    try:
        g.throw(StopIteration)
    except StopIteration as e:
        print('Average', e.value)
