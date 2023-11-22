## 변수 선언 부분 ##
money, c50000, c10000, c5000, c1000, c500, c100, c50, c10 = 0, 0, 0, 0, 0, 0, 0, 0, 0

## 메인 코드 부분 ##
money = int(input("교환할 돈은 얼마?"))

c50000 = money // 50000
money %= 50000

c10000 = money // 10000
money %= 10000

c5000 = money // 5000
money %= 5000

c1000 = money // 1000
money %= 1000

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("50000원짜리 %d장, 10000원짜리 %d장, 5000원짜리 %d장, 1000원짜리 %d장"  %(c50000, c10000, c5000, c1000))
print("500원짜리 %d장, 100원짜리 %d장, 50원짜리 %d장, 10원짜리 %d장"  %(c500, c100, c50, c10))
print("바꾸지 못한 잔돈 ==> %d원\n"%money)
