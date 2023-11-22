Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: C:/파이썬(2-1)/9주차/code09-01.py ====================
>>> tt1=(10,20,30);tt1
(10, 20, 30)
>>> tt2=10,20,30; tt2
(10, 20, 30)
>>> tt3=(10); tt3
10
>>> tt4=10; tt4
10
>>> tt5=(10,); tt5
(10,)
>>> tt6=10,; tt6
(10,)
>>> tt1=(10,20,30,40)
>>> tt1[0]
10
>>> tt1[0]+tt1[1]+tt1[2]
60
>>> 
tt1[1:3]
(20, 30)
>>> tt1[1:]
(20, 30, 40)
>>> tt1[:3]
(10, 20, 30)
>>> tt2('A', 'B')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tt2('A', 'B')
TypeError: 'tuple' object is not callable
>>> tt1+tt2
(10, 20, 30, 40, 10, 20, 30)
>>> tt2*3
(10, 20, 30, 10, 20, 30, 10, 20, 30)
>>> 
>>> tt2=('A', 'B')
>>> tt1+tt2
(10, 20, 30, 40, 'A', 'B')
>>> tt2*3
('A', 'B', 'A', 'B', 'A', 'B')
>>> myTuple=(10, 20, 30)
>>> myList=List(myTuple)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    myList=List(myTuple)
NameError: name 'List' is not defined
>>> myList=list(myTuple)
>>> myList.append(40)
>>> myTuple=tuple(myList)
>>> myTuple
(10, 20, 30, 40)
>>> 
dic={1:'a',2:'b',3:'c'}
>>> dic1
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dic1
NameError: name 'dic1' is not defined
>>> dic1
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dic1
NameError: name 'dic1' is not defined

>>> dic1{1:'a',2:'b',3:'c'}
SyntaxError: invalid syntax
>>> dic={1:'a',2:'b',3:'c'}
>>> dic1={1:'a',2:'b',3:'c'}
>>> dic1
{1: 'a', 2: 'b', 3: 'c'}
>>> 
dic2={'a':1,'b':2,'c':3}
>>> dic2
{'a': 1, 'b': 2, 'c': 3}
>>> student1={'학번':1000, '이름':'홍길동', '학과':'컴퓨터공학과'}
>>> student1
{'학번': 1000, '이름': '홍길동', '학과': '컴퓨터공학과'}
>>> student1['연락처']='010-1111-2222'
>>> student1
{'학번': 1000, '이름': '홍길동', '학과': '컴퓨터공학과', '연락처': '010-1111-2222'}
>>> student1['학과']='파이썬학과'
>>> stuednt1
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    stuednt1
NameError: name 'stuednt1' is not defined
>>> student1
{'학번': 1000, '이름': '홍길동', '학과': '파이썬학과', '연락처': '010-1111-2222'}
>>> del(student1['학과'])
>>> student1
{'학번': 1000, '이름': '홍길동', '연락처': '010-1111-2222'}
>>> student1={'학번':1000,'이름':'홍길동','학과':'파이썬학과','학번':2000}
>>> student1
{'학번': 2000, '이름': '홍길동', '학과': '파이썬학과'}
>>> student1['학번']
2000
>>> student1['이름']
'홍길동'
>>> student1['학과']
'파이썬학과'
>>> student.get('이름')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    student.get('이름')
NameError: name 'student' is not defined
>>> student1.get('이름')
'홍길동'
>>> student1['주소']
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    student1['주소']
KeyError: '주소'
>>> student1.get('주소')
>>> student1.keys()
dict_keys(['학번', '이름', '학과'])
>>> list(student1.keys())
['학번', '이름', '학과']
>>> student1.values()
dict_values([2000, '홍길동', '파이썬학과'])
>>> student1.items()
dict_items([('학번', 2000), ('이름', '홍길동'), ('학과', '파이썬학과')])
>>> '이름' in student1
True
>>> '주소' in student1
False
>>> 
