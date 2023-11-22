a = int(input("첫번째 숫자를 입력해 주세요 : "))
b = int(input("두번째 숫자를 입력해 주세요 : "))
c = int(input("세번째 숫자를 입력해 주세요 : "))

if a>b :
    if a>c :
        print("가장 큰 숫자는 %d 이다." % a)
    else :
        print("가장 큰 숫자는 %d 이다." % c)
else :
    if b>c :
        print("가장 크 숫자는 %d 이다." % b)
    else :
         print("가장 큰 숫자는 %d 이다." % c)

