def Factor(n):
   answer = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           answer.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       answer.append(n)
   for item in answer:
       if answer.count(item)>1:
           u=answer.count(item)
           print(u,item)
           break
   return answer
print("shame")
a=int(input())
print(Factor(a))
