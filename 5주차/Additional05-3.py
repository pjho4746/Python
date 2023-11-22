select = int(input("달러(1), 엔(2), 유로(3), 위안(4) 중에 선택해주세요 : "))
money = int(input("금액을 입력해 주세요 : "))

if select == 1:
    dollar = 1167
    res = dollar * money
    print("환전한 금액은 %d 원 입니다." % res)
elif select == 2:
    yen = 1.096
    res = yen * money
    print("환전한 금액은 %f 원 입니다." % res)
elif select == 3:
    euro = 1268
    res = euro * money
    print("환전한 금액은 %d 원 입니다." % res)
else :
    renmibi = 171
    res =renmibi * money
    print("환전한 금액은 %d 원 입니다." % res)


