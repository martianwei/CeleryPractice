from celery import chain
from proj.tasks import add, mul

# (4 + 4) * 8
ans = chain(add.s(4, 4) | mul.s(8))().get()
# 64
print(ans)
