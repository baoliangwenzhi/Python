# -*- encoding=UTF-8 -*-


def log(level, *args, **kvargs):
    print level

    def inner(func):
        def wrapper(*args, **kvargs):
            print 'before calling', func.__name__
            print 'args', args, 'kvargs', kvargs
            func(*args, **kvargs)
            print 'end calling', func.__name__

        return wrapper

    return inner


@log(level='INFO')
def hello(name, age):
    print 'hello', name, age


@log(level='xxx')
def hello2(name, age):
    print 'hello2', name, age


# if __name__ == '__main__':
#     hello(name='nowcoder', age=2)
#     hello2(name='nowcoder2', age=3)
