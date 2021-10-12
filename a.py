# import numpy
# l = list(map(int, input().split()))
# m = []
# for i in range(l[0]):
#         m.append((map(int, input().split())))
# m = numpy.array(m)
# print(numpy.mean(m, axis = 1))
# print(numpy.var(m, axis = 0))
# print(numpy.std(m))
import numpy

n,m=map(int,input().split())

a=numpy.array([list(map(int,input().split())) for i in range(n)])
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(numpy.std(a,None))
