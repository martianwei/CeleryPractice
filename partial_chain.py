from celery import chain
from proj.tasks import add, mul
# (? + 4) * 8
g = chain(add.s(4) | mul.s(8))
ans = g(4).get()
# 64
print(ans)
