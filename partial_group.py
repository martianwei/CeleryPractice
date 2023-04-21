from celery import group
from proj.tasks import add

g = group(add.s(i) for i in range(10))
myList = g(10).get()
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(myList)
