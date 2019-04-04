def add(a, b):
    return a + b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

print('-'*15)
print("1.더하기\n2.빼기\n3.곱하기\n4.나누기\n5.그만")
print('-'*15)


while True:  #While True:를 하는 이유를 모르겟다
    menu = int(input("어떤 계산.  "))
    if(menu <= 4):
        numberA= int(input("First_number.  "))
        numberB= int(input("Second_number.  "))
        if (menu ==1):
            result = add(numberA, numberB)
            print("값은 %d 입니다."%result)
        elif (menu ==2):
            result= sub(numberA, numberB)
            print("값은 %d 입니다."%result)
        elif (menu ==3):
            result = mul(numberA, numberB)
            print("값은 %d 입니다."%result)
        elif (menu==4):
            if numberA or numberB == 0:
                print("바보")
            else:
                result = div(numberA, numberB)
                print("값은 %d 입니다."%result)
        
    elif(menu ==5):
        break
    else:
        print("바보")


