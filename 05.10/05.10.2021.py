
import random
def random_name(names, surnames, sec_names, num):
    i = 0
    while i < num:
        yield (random.choice(names) + ' ' + random.choice(surnames) + ' ' + random.choice(sec_names))
        i+=1
first = ['Макар', 'Азат', 'Илья', 'Семен', 'Павел']
second = ['Нуриев', 'Лососев', 'Никитин', 'Кузнецов', 'Рженов']
third = ['Осьминогович', 'Ражокович', 'Георгиевич', 'Альбертович', 'Мусхудатович']
for i in random_name(first,second,third,4):
    print(i)