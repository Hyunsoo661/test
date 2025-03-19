

#연습문제 2.9
print("섭씨 화씨")
for celsius in range(0,51,10):
    fahrenheit=(9/5)*celsius + 32
    print(f"{celsius:<5} {fahrenheit:<5.1f}")

#연습문제 2.10
celsius=int(input('섭씨온도를 입력하세요.'))
fahrenheit=(9/5)*celsius+32
print('섭씨',celsius,'도는 화씨',fahrenheit,'도입니다.')

#연습문제 2.11
fahrenheit=float(input("화씨 온도를 입력하세요:"))
celsius=(fahrenheit-32)*5/9
print(f"화씨{fahrenheit}도는 섭씨{celsius:.1f}도 입니다.")

#연습문제 2.12
PI=3.141592
radius=11

circumference=2*PI*radius
area=PI*radius**2

print(f"원의 반지름={radius},원의 둘레={circumference:.6f},원의 면적={area:.12f}")

#연습문제 2.13
PI=3.141592

radius=float(input("원의 반지름을 입력하세요:"))

circumference=2*PI*radius
area=PI*radius**2

print(f"원의 둘레={circumference:.6f},원의면적={area:.12f}")

#연습문제 2.14
for num in range(1,11):
    sqrt_value=num**0.5
    print(f"{num}의 제곱근={sqrt_value:.115f}")


#연습문제 2.15
import math
z=complex(1,2)

rotated_90=z*complex(0,1)

angle_30=math.radius(30)
cos_30=math.cos(angle_30)
sin_30=math.sin(angle_30)
rotation_30=complex(cos_30,sin_30)
rotated_30=z*rotation_30

print(f"회전하기 전:{z}")
print(f"90도 회전한 후:{rotated_90}")
print(f"30도 회전한 후:{rotated_30}")

#연습문제 2.16
z=complex(1,2)

rotated_z*complex(0,1)

print(f"회전하기 전:{z}")
print(f"90도 회전한 후:{rotated_z}"}

#연습문제 2.17
for i in range(10):
    print(2<<i,end="")

#연습문제 2.18
n=int(input("정수를 입력하세요:"))

is_even=(n%2==0)
print(f"이 수가 짝수인가요?{is_even}")

#연습문제 2.19
n=int(input("정수를 입력하세요:"))

is_valid=(0<=n<=100)and(n%2==0)
print(f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?{is_valid}")

#연습문제 2.20
a=5
b=6

and_result=a&b
or_result = a | b
xor_result=a^b

print(f"{bin(a)} & {bin(b)} = {bin(and_result)}")
print(f"{bin(a)} | {bin(b)} = {bin(or_result)}")
print(f"{bin(a)} ^ {bin(b)} = {bin(xor_result)}")

#연습문제 2.21
n=int(input("정수를 입력하세요:"))
binary_n=bin(n)
negation_n=bin(~n)

print(f"{n}의 2진수 값:{binary_n}")
print(f"{n}의 2진수 값에 대한 비트단위 부정값:{negation_n}")

#연습문제 2.22
a=int(input("정수 a를 입력하세요:"))
b=int(input("정수 b를 입력하세요:"))

quotient=a//b
remainder=a%b

print(f"a/b의 몫:{quotient}")
print(f"a/b의 나머지:{remainder}")

#연습문제 2.23
n=int(input("세 자리 정수를 입력하세요:"))

hundreds=n//100
tens=(n//10)%10
ones=n%10

print(f"백의자리:{hundreds}")
print(f"십의자리:{tens}")
print(f"일의자리:{ones}")

#연습문제 2,24
n=int(input("세 자리 정수를 입력하세요:"))

hundreds=n//100
tens=(n//10)%10
ones=n%10

print(ones)
print(tens)
print(hundreds)
    
