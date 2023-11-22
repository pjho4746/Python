Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #81
>>> socres=[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.5, 7.8, 9.4]
>>> #82
>>> #81
>>> socres=[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.5, 7.8, 9.4]
>>> *valid_score, _, _ = scores
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    *valid_score, _, _ = scores
NameError: name 'scores' is not defined
>>> scores=[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.5, 7.8, 9.4]
>>> *valid_score, _, _=scores
>>> print(valid_score)
[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.5]
>>> #82
>>> scores=[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
>>> a, b, *valid_score=scores
>>> print(valid_score)
[8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
>>> #83
>>> scores=[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
>>> a, *valid_score, b=scores
>>> print(valid_score)
[8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8]
>>> #84
>>> temp={}
>>> #85
>>> ice={"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
>>> print(ice)
{'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
>>> #86
>>> ice={"메로나": 1000, "vhffkvh": 1200, "빵빠레": 1800}
>>>  ice={"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
 
SyntaxError: unexpected indent
>>> ice={"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
>>> ice["죠스바"]=1200
>>> ice["월드콘"]=1500
>>> print(ice)
{'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
>>> #87
>>> print("메로나 가격: ", ice["메로나"])
메로나 가격:  1000
>>> #88
>>> ice["메로나"]=1300
>>> #89
>>> del ice["메로나"]
>>> print(ice)
{'폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
>>> #90
>>> #딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생합니다
>>> #91
>>> inventory={"메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
>>> print(inventory)
{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
>>> #92
>>> print(inventory["메로나"][0],"원")
300 원
>>> #93
>>> print(inventory["메로나"][1], "개")
20 개
>>> #94
>>> inventory={"메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
>>> inventory["월드콘"]=[500,7]
>>> print(inventory)
{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}
>>> #95
>>> icecream={'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나': 1000}
>>> ice=list(icecream.keys())
>>> print(ice)
['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']
>>> #96
>>> icecream={'xodzmqhdl':1200,'vhffkvh':1200,'빵빠레':1800,'월드콘':1500,'메로나':1000}
>>> price=list(icecream.values())
>>> print(price)
[1200, 1200, 1800, 1500, 1000]
>>> #97
>>> icecream={'탱크보이':1200,'폴라포':1200,'빵빠레':1800,'월드콘':1500,'메로나':1000}
>>> print(sum(icecream.values()))
6700
>>> #98
>>> icecream={'탱크보이':1200,'폴라포':1200,'빵빠레':1800,'월드콘':1500,'메로나':1000}
>>> new_product={'팥빙수':2700, '아맛나':1000}
>>> icecream.update(new_product)
>>> print(icecream)
{'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000, '팥빙수': 2700, '아맛나': 1000}
>>> #99
>>> keys=("apple", "pear", "peach")
>>> vals=(300,250,400)
>>> result=dict(zip(keys,vals))
>>> print(result)
{'apple': 300, 'pear': 250, 'peach': 400}
>>> #100
>>> date=['09/05','09/06','09/07','09/08',09/09']
      
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> date=['09/05','09/06','09/07','09/08','09/09']
>>> close_price=[10500, 10300, 10100, 10000, 11000]
>>> close_tavle=dict(zip(date,close_price))
>>> print(close_table)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(close_table)
NameError: name 'close_table' is not defined
>>> date=['09/05','09/06','09/07','09/08','09/09']
>>> close_price=[10500, 10300, 10100, 10000, 11000]
>>> close_table=dict(zip(date,close_price))
>>> print(close_table)
{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10000, '09/09': 11000}
>>> 
