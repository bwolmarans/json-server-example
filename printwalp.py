class Print:
    def __lt__(self, thing):
        print(thing)

p = Print()

p < 'hello'   #  ->  hello

