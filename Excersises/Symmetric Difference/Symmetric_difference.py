# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_num = int(input())
eng_set= set(map(int, input().split()))
# s = set(eng_set)

fren_num = int(input())
fren_set= set(map(int, input().split()))
# s = set(fren_set)

print (len(eng_set.symmetric_difference(fren_set)))