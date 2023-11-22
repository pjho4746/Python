a = int(input("A의 주사위 숫자는 : "))
b = int(input("B의 주사위 숫자는 : "))

if a>b :
    print("A의 주사위 숫자는 %d입니다." %a)
    print("B의 주사위 숫자는 %d입니다." %b)
    print("A가 이겼습니다.")
elif a<b :
    print("A의 주사위 숫자는 %d입니다." %a)
    print("B의 주사위 숫자는 %d입니다." %b)
    print("B가 이겼습니다.")
else :
    print("A의 주사위 숫자는 %d입니다." %a)
    print("B의 주사위 숫자는 %d입니다." %b)
    print("A와 B는 비겼습니다.")
