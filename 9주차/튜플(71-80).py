Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #71
>>> my_variable=()
>>> print(type(my_variable))
<class 'tuple'>
>>> #72
>>> movie_rank=("닥터 스트레인지", "스플릿", "럭키")
>>> #73
>>> my_tuple=(1)
>>> type(my_tuple)
<class 'int'>
>>> #74
>>> #tuple은 원소의 값을 변경할 수 없다
>>> #75
>>> #원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 고라호 없이 동작한다
>>> #76
>>> #튜플의 값은 변경할 수 없기 때문에, 새로운 튜플을 반들고 변수 t를 업데이트 해야 함
>>> #77
>>> data=list(interest)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    data=list(interest)
NameError: name 'interest' is not defined
>>> interest=('삼성전자', 'ㅣㅎwjswk', 'SK Hynix')
>>> data=list(interest)
>>> #78
>>> data=tuple(interest)
>>> #79
>>> #apple banana cake
>>> #80
>>> data=tuple(range(2,100,2))
>>> print(data)
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)
>>> 
