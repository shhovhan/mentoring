#Simple generator which gives numbers from 0 to 199
def generator_func():
    for i in range(200):
        print('call number', i+1)
        yield i

if __name__ == '__main__':
    gen = generator_func()

    for item in gen:
        print(item)
