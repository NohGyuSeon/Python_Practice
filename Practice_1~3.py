from cmath import pi

# 원 넓이 구하기
print("원의 넓이를 계산합니다.")
반지름 = 15
원의넓이 = 반지름 * 반지름 * 3.141592
print("원의 넓이는", 원의넓이, "입니다.")
print()

# 피자 크기 계산하기
diameter = 45
r = diameter / 2
pizza_area = r * r * 3.14
p = pizza_area / 8
print("피자 한 조각의 넓이는", p, "입니다.")
print()

# 환전 금액 계산하기
# 저축 후 원리금 계산하기
# 0이 많이 들어가는 큰 값 입력하기
# 세금을 고려한 원리금 계산하기

"""
이미지를 표현할 때 한 픽셀 당 3Byte의 메모리 크기를 사용하여 색상을
표현한다고 하자. 픽셀은 몇 가지 색상을 표현할 수 있을까?
"""
pix = 3
pix_color = 3 * 8 # 1Byte = 8bits
pix_result = 2 ** pix_color
print(pix_result)
print()

"""
두 번 곱해서 5가 되는 수 (제곱근 5) : 
세 번 곱해서 7가 되는 수 (삼제곱근 7) : 
"""
D_pow_5 = 5 ** (1/2)
T_pow_7 = 7 ** (1/3)
print(D_pow_5)
print(T_pow_7)
print()

# 센티미터를 인치로 변환하기
print(90 / 2.54)
print(90 // 2.54)
print()

"""
아버지의 바지 허리 사이즈가 32 inch 이다.
cm 단위로 76, 78, 80, 82, 84, 86 중에서 어떤 것을 선택해야 할까?
"""
print(32 * 2.54)
print()

# 키를 피트와 인치로 변환하기
# 1 inch = 2.54cm 
# 1 feet = 12 inch
inch = 170 / 2.54
feet = inch // 12
print("170cm = ", feet, "feets ", inch % 12, " inches")
print()

# y의 값은?
x = int(input())
y = x ** 2 + (3/5)*x + (3/10)**2
print(y)
print()

# 스스로 해보기
"""
반지름: 15
원의둘레: 94.24775
원의넓이: 706.8582
"""
r = 15
length = 2 * 4 * 3.14
area = r ** r * 3.14
print(r)
print()
print(length)
print()
print(area)
print()
