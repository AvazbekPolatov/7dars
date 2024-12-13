#  Iterators & iterables & Generator

# list, tuple, set, dict, string, range

# --------------------------------------------

users=['Avazbek','Asilbek','Avazbek','Asilbek',] 
iter_users=iter(users)

# print(next(iter_users))
# print(next(iter_users))
# print(next(iter_users))
# print(next(iter_users))

# for user in users:
#     print(user)
# --------------------------------------------

# Generators
# def generator():
#     yield 'Avazbek'
#     yield 'Asilbek'
#     yield 'Alibek'
#     yield 'Muradbek'
#     yield 'Mohammadbek'

# gen=generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for user in generator():
#     print(user)

# --------------------------------------------
# str.__iter__()
# list.__iter__()
# dict.__iter__()
# set.__iter__()
# tuple.__iter__()
# range.__iter__()

# --------------------------------------------

# users=['Avazbek','Asilbek','Avazbek','Asilbek',]
# users_iter=users.__iter__()
# print(users_iter.__next__())
# print(users_iter.__next__())
# print(users_iter.__next__())
# print(users_iter.__next__())

# for user in users:
#     print(user)

# ------------------------------------------------

# from typing import Iterable, Iterator

# users=['Avazbek','Asilbek','Avazbek','Asilbek',]

# class CustomIterator:
#     def __init__(self, iterable):
#         self.__users=users
#         self.__index = -1
        

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.__index += 1
#         if self.__index >= len(self.__users):
#             raise StopIteration("Index out of range")
#         return self.__users[self.__index]
            
        
# a=CustomIterator(users)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# ===========================================================
# def cutome_generator():
#     yield 'Avazbek'
#     yield 'Asilbek'
#     yield 'Alibek'
#     yield 'Muradbek'
#     yield 'Mohammadbek'

# print(cutome_generator().__sizeof__())
# print(list(cutome_generator()))

# for user in cutome_generator():
#     print(user)
# ------------------------------------------------------------------
# def generator_numbers():
#     for num in range(10000):
#         yield num

# print(generator_numbers().__sizeof__())
# # print(list(generator_numbers()))
# nums=[i for i in range(10000)]
# print(nums.__sizeof__())

# ===========================================================


# file=open("navoiy.txt",mode="r",encoding="utf-8")
# print(file.__sizeof__())
# content=file.read()
# print(content.__sizeof__())
# file.close()


import os

def read_file_generator(file_name):
    """
    Faylni satr bo'yicha o'qiydigan generator funksiyasi.
    :param file_name: O'qilishi kerak bo'lgan faylning yo'li
    """
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            for line in file:
                yield line.strip()  # Satr oxiridagi bo'sh joylarni olib tashlash
    except FileNotFoundError:
        print(f"Fayl topilmadi: {file_name}")

# Fayl nomini aniqlash
file_name = r"C:\Users\Admin\OneDrive\Ishchi stol\Najot Talim Fargona\7dars\navoiy.txt"
