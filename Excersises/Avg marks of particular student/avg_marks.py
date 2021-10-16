n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
# print(student_marks)
if query_name in student_marks:
   l = student_marks.get(query_name) 
avg = (float(l[0]) + float(l[1])+ float(l[2]))/3
print("{:.2f}".format(avg))
   