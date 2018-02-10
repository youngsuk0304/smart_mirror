a=input()
i=0
input_char=a[i]
cnt=1
for i in range(1,len(a)):
    if input_char==a[i]:
        cnt=cnt+1
    elif input_char!=[i]:
        print(input_char+str(cnt))
        input_char=a[i]
        cnt=1

print(input_char+str(cnt))
