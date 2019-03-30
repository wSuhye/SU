# 연습문제 (리스트 내장함수)

list = ['Life', 'is', 'too', 'short']
A = ' '.join(list)
print(A)

# 연습문제 (if)
# 이 문제의 답은 shirt

a = "Life is too short, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
else:
    print('none')


# 연습문제 (while문 별 찍기)

star = 0
while star < 4:
    star = star +1
    print("*"*star)

#연습문제 (모음찾기)

a = "mutzangesazachurum"
b = "aeiou"
number = 0
for i in a:
    if i in b:
        number+=1
        print(number)

#과제 1 (while)
#1-1 다시 해보자
Sum = 0
for x in range(1,1001):
    if x % 3==0:
        Sum += x
        print(Sum)
    
        
#1-2
star = 11
while star > 1:
    star = star-1
    print("*"*star)

#1-3
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
B =[]
for i in A:
    if i >=50:
        B.append(i)
sum(B)

# 과제 2 (for)
#2-1 For문을 활용하여 1부터 100까지의 숫자를 출력
A = range(1,101)
for x in A:
    print(x)

#2-2 For문을 활용하여 A학급의 평균점수 구하기
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
Num = len(A)
sum(A)/Num
#for문 사용해서
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for x in A:
    sum += x
print(sum/len(A))

# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# Num = len(A)
# B = 0
# for i in A:
#     B = B+i
# print(B)
# B/Num

#2-3 
result = [i*2 for i in [1,2,3,4,5] if i%2==1]
print(result)
