Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #연습문제 2.1
>>> print(200,'+',300,'+',400,'=',200+300+400)
200 + 300 + 400 = 900
>>> #연습문제 2.2
>>> weight=30
>>> height=60
>>> print(weight)
30
>>> print(height)
60
>>> #연습문제 3.3
>>> width=30
>>> height=60
>>> area=width*height
>>> print('사각형의면적:',area)
사각형의면적: 1800
>>> #연습문제 2,4
>>> width=40
>>> height=20
>>> area=width*height//2
>>> print('삼각형의면적:',area)
삼각형의면적: 400
>>> #연습문제 2.5
>>> width=int(input('정사각형의 밑변을 입력하시오:'))
정사각형의 밑변을 입력하시오:40
>>> area=width*width
>>> print('정사각형의 면적:',area)
정사각형의 면적: 1600
>>> #연습문제 2.6
>>> print('1부터 10까지의 합:',1+2+3+4+5+6+7+8+9+10)
1부터 10까지의 합: 55
>>> #연습문제 2.7
>>> print('10!=',1*2*3*4*5*6*7*8*9*10)
10!= 3628800
>>> #연습문제 2.8
>>> print("a n a**n")
a n a**n
for a in range(2,7):
    n=2
    result=a**n
    print(f"{a:<3}{n:<3}{result:<5}")

    
2  2  4    
3  2  9    
4  2  16   
5  2  25   
6  2  36   

============== RESTART: C:/Users/82105/OneDrive/AIprogram/test.py ==============
섭씨 화씨
Traceback (most recent call last):
  File "C:/Users/82105/OneDrive/AIprogram/test.py", line 4, in <module>
    fahrenheit=(9/5)*celcius + 32
NameError: name 'celcius' is not defined. Did you mean: 'celsius'?

============== RESTART: C:/Users/82105/OneDrive/AIprogram/test.py ==============
섭씨 화씨
Traceback (most recent call last):
  File "C:/Users/82105/OneDrive/AIprogram/test.py", line 4, in <module>
    fahrenheit=(9/5)*celcius + 32
NameError: name 'celcius' is not defined. Did you mean: 'celsius'?

============== RESTART: C:/Users/82105/OneDrive/AIprogram/test.py ==============
섭씨 화씨
Traceback (most recent call last):
  File "C:/Users/82105/OneDrive/AIprogram/test.py", line 7, in <module>
    print(f"{celsius:<5} {fehrenheit:<5.1f}")
NameError: name 'fehrenheit' is not defined. Did you mean: 'fahrenheit'?

============== RESTART: C:/Users/82105/OneDrive/AIprogram/test.py ==============
섭씨 화씨
0     32.0 
10    50.0 
20    68.0 
30    86.0 
40    104.0
50    122.0
섭씨온도를 입력하세요.30
섭씨 30 도는 화씨 86.0 도입니다.
