from celery import chord, group, chain
from proj.tasks import add, xsum

ans1 = chord((add.s(i, i) for i in range(3)), xsum.s())().get()
ans2 = chain(group(add.s(i, i) for i in range(10)) | xsum.s())().get()
print(ans2)
