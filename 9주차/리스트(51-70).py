Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #51
>>> movie_rank=["닥터 스트레인지", "스플릿", "럭키"]
>>> #52
>>> movie_rank=["닥터 스트레인지", "스플릿", "럭키"]
>>> movie_rank.append("베트맨")
>>> print(movie_rank)
['닥터 스트레인지', '스플릿', '럭키', '베트맨']
>>> #53
>>> movie_rank=["닥터 스트레인지", "스플릿", "럭키"]
>>> movie_rank.insert(1,"슈퍼맨")
>>> print(movie_rank)
['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키']
>>> #54
>>> movie_rank=["닥터 스트레인지", "스플릿", "럭키"]
>>> del movie_rank[3]
>>> print(movie_rank)
SyntaxError: multiple statements found while compiling a single statement
>>>  movie_rank=["닥터 스트레인지", "스플릿", "럭키", "베트맨"]
>>> del movie_rank[3]
>>> print(movie_rank)
SyntaxError: unexpected indent
>>> movie_rank=["닥터 스트레인지", "스플릿", "럭키", "베트맨"]
>>> del movie_rank[3]
>>> print(movie_rank)
SyntaxError: multiple statements found while compiling a single statement
>>> movie_rank=['닥터 스트레인지', '스플릿', '럭키', '베트맨']
>>> del movie_rank[3]
>>> print(movie_rank)
['닥터 스트레인지', '스플릿', '럭키']
>>> #55
>>> movie_rank=['닥터 스트레인지','슈퍼맨', '스플릿', '베트맨']
>>> del movie_rank[2]
>>> del movie_rank[2]
>>> print(movie_rank)
['닥터 스트레인지', '슈퍼맨']
>>> #56
>>> lang1=["C","C++","JAVA"]
>>> lang2=["Python", "Go", "C#"]
>>> langs=lang1+lang2
>>> print(langs)
['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
>>> #57
>>> nums=[1,2,3,4,5,6,7]
>>> print("max", max(nums))
max 7
>>> print("min", min(nums))
min 1
>>> #58
>>> nums=[1,2,3,4,5]
>>> print(sum(nums))
15
>>> cook=["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
>>> print(len(cook))
12
>>> #60
>>> nums=[1,2,3,4,5]
>>> average=sum(nums)/len(nums)
>>> print(average)
3.0
>>> #61
>>> price=['20190778', 100, 130, 140, 150, 160, 170]
>>> print(price(1:])
SyntaxError: invalid syntax
>>> print(price[1:])
[100, 130, 140, 150, 160, 170]
>>> #62
>>> nums=[1,2,3,4,5,6,7,8,9,10]
>>> rint(nums[::2])
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    rint(nums[::2])
NameError: name 'rint' is not defined
>>> print(nums[::2])
[1, 3, 5, 7, 9]
>>> #63
>>> nums=[1,2,3,4,5,6,7,8,9,10]
>>> print(nums[1::2])
[2, 4, 6, 8, 10]
>>> #64
>>> nums=[1,2,3,4,5]
>>> print(nums[::-1])
[5, 4, 3, 2, 1]
>>> #65
>>> interest=['삼성전자', 'LG전자', 'Naver']
>>> print(interest[0], interest[2])
삼성전자 Naver
>>> #66
>>> interest=['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
>>> print("".join(interest))
삼성전자LG전자NaverSK하이닉스미래에셋대우
>>> #67
>>> interest=['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
>>> print("/".join(interest))
삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
>>> #68
>>> interest=['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
>>> print("\n".join(interest))
삼성전자
LG전자
Naver
SK하이닉스
미래에셋대우
>>> #69
>>> string="삼성전자/LG전자/NAver"
>>> interest=string.split("/")
>>> print(interest)
['삼성전자', 'LG전자', 'NAver']
>>> #70
>>> data=[2,4,3,1,5,10,9]
>>> data.sort()
>>> print(data)
[1, 2, 3, 4, 5, 9, 10]
>>> data=[2,3,4,1,5,10,9]
>>> data2=sorted(data)
>>> print(data2)
[1, 2, 3, 4, 5, 9, 10]
>>> 
