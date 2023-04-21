from celery import group
from proj.tasks import add

myList = group(add.s(i, i) for i in range(10))().get()
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(myList)
