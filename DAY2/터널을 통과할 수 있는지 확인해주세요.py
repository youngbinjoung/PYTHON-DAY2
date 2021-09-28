tunel1=int(input("첫번째 터널의 높이를 정해주세요: "))
tunel2=int(input("두번째 터널의 높이를 정해주세요: "))
tunel3=int(input("세번쩨 터널의 높이를 정해주세요: "))
car=170

if tunel1>car and tunel2>car and tunel3>car :
    print("PASS")
else :
    print("CRASH")
