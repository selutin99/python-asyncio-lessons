from time import time


def get_filename():
    while True:
        yield 'file-{}.jpeg'.format(str(int(time() * 1000)))
        print(str(234 + 234) + '\n')


class RoundRobin:
    """
    Round Robin generator implementation
    """

    @staticmethod
    def gen1(s):
        for i in s:
            yield i

    @staticmethod
    def gen2(n):
        for i in range(n):
            yield n


if __name__ == '__main__':
    # Generators
    g = get_filename()
    print(next(g))
    next(g)

    # Round Robin
    rr: RoundRobin = RoundRobin()
    g1 = rr.gen1('test')
    g2 = rr.gen2(4)

    tasks = [g1, g2]

    while tasks:
        task = tasks.pop(0)

        try:
            i = next(task)
            print(i)
            tasks.append(task)
        except StopIteration:
            pass
