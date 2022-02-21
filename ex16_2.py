# languages = ['Python', 'Java', 'JS', 'SQL']
# languages.insert(2, input('Введите язык программирования: '))
# ind_lang = languages.index(input('Индекс какого ЯП вытащить?'))
# print(languages)
# print(ind_lang)

# films = [
#     'Крепкий орешек', 'Назад в будущее', 'Таксист', 
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#     'Мементо', 'Отступники', 'Деревня', 
#     'Проклятый остров', 'Начало', 'Матрица'
# ]

# my_list=[]
# while True:
#   print("Ващ топ фильмов:", my_list)
#   new_movie = input('')

# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(1, 'bear')
# print(zoo)
# zoo.remove('elephant')
# print(zoo)
# print("Лев сидит в клетке", zoo.index('lion')+1)
# print("Обезьяна сидит в клетке", zoo.index('monkey')+1)

n = []
k = int(input(('Кол-во сотрудников: ')))
for i in range(k):
  j = int(input('ЗП: '))
  n.append(j)
print(n)
for o in n:
  if o == 0:
    n.remove(o)
print("Осталось сотрудников:", len(n))
print("Список": n)
print("Максимальная ЗП:", max(n))
print("Минимальная ЗП:", min(n))