size_disk = 1.44
pages = 100
lines = 50
symbols = 25
symbol_size_bite = 4

size_disk *= 1024 * 1024 ## перевод Мб в б
size_book = symbol_size_bite * symbols * lines * pages
book = int(size_disk // size_book)

print("Количество книг, помещающихся на дискету:", book)
