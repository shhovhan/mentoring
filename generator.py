def generator_func():
    for i in range(200):
        print('call number', i+1)
        yield i


gen = generator_func()

for i in gen:
    print(i)
