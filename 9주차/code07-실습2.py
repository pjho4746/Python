Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
mySet1={1,2,3,3,3,4}
>>> myset1
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    myset1
NameError: name 'myset1' is not defined
>>> mySet1={1,2,3,3,3,4}
>>> mySet1
{1, 2, 3, 4}
>>> salesList=['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '삼각김밥'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> salesList=['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '삼각김밥']
>>> set(salesList)
{'도시락', '삼각김밥', '바나나'}
>>> mySet1={1,2,3,4,5}
>>> mySet2={4,5,6,7}
>>> mySet1&mySet2 ##교집합
{4, 5}
>>> mySet1|mySet2 ##합집합
{1, 2, 3, 4, 5, 6, 7}
>>> mySet1 - mySet2 ##차집합
{1, 2, 3}
>>> mySet1 ^ mySet2 ##대칭 차집합
{1, 2, 3, 6, 7}
>>> 
mySet.intersection(mySet2)
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    mySet.intersection(mySet2)
NameError: name 'mySet' is not defined
>>> mySet1.intersection(mySet2)
{4, 5}
>>> mySet1.union(mySet2)
{1, 2, 3, 4, 5, 6, 7}
>>> mySet1.difference(mySet2)
{1, 2, 3}
>>> mySet1.symmetric_difference(mySet2)
{1, 2, 3, 6, 7}
>>> numList=[]
>>> for num in range(1,6):
	numList.append(num)
numList
SyntaxError: invalid syntax
>>> for num in range(1,6):
	numList.append(num)

	
>>> numList
[1, 2, 3, 4, 5]
>>> numList=[num for num in range(1,6)]
>>> numList
[1, 2, 3, 4, 5]
>>> numList=[num*num for num in range(1,6)]
>>> numList
[1, 4, 9, 16, 25]
>>> numList=[num for num in range(1,21) if num%3==0]
>>> numList
[3, 6, 9, 12, 15, 18]
>>> foods=['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
>>> sides=['오뎅', '단무지', '김치']
>>> for foods, side in zip(foods, sides):
	print(food, '-->', side)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    print(food, '-->', side)
NameError: name 'food' is not defined
>>> for food, side in zip(foods, sides):
	print(food, '-->', side)

	
떡 --> 오뎅
볶 --> 단무지
이 --> 김치
>>> 
>>> foods=['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
>>> sides=['오뎅', '단무지', '김치']
>>> tupList=list(zip(foods, sides))
>>> dic=dict(zip(foods, sides))
>>> tupList
[('떡볶이', '오뎅'), ('짜장면', '단무지'), ('라면', '김치')]
>>> dic
{'떡볶이': '오뎅', '짜장면': '단무지', '라면': '김치'}
>>> oldList=['짜장면', '탕수육', '군만두']
>>> newList=oldList
>>> print(newList)
['짜장면', '탕수육', '군만두']
>>> olList[0]='짬뽕'
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    olList[0]='짬뽕'
NameError: name 'olList' is not defined
>>> oldList[0]='짬뽕'
>>> oldList.append('깐풍기')
>>> print(newList)
['짬뽕', '탕수육', '군만두', '깐풍기']
>>> 
oldList=['짜장면', '탕수육', '군만두']
>>> newList=oldList[:]
>>> print(newList)
['짜장면', '탕수육', '군만두']
>>> oldList[0]='짬뽕'
>>> oldList.append('깐풍기')
>>> print(newList)
['짜장면', '탕수육', '군만두']
>>> parking=[]
>>> top=0
>>> parking.append('자동차A')
>>> top+=1
>>> parking.append('자동차B')
>>> top+=1
>>> parking.append('자동차C')
>>> top+=1
>>> top-=1
>>> outCar=parking.pop()
>>> print(outCar)
자동차C
>>> 
