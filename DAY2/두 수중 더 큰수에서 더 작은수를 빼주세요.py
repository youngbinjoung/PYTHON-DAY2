num=int(input("입력"))
num2=int(input("입력"))

if num>num2 :
    print("{} - {} = {}입니다.".format(num,num2,num-num2))
elif num<num2 :
    print("{} - {} = {}입니다.".format(num2,num,num2-num))
else :
    print("{} - {} = {}입니다.".format(num,num2,num-num2))
