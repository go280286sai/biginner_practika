my_list=['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
n=int(input())
def my_fun(a,b):
    if len(a)/n>=1:
        k=len(a)//b
        l=len(a)%b
        if l>0 and l<=k:
            l=l+1
        elif l>0:
            l=l+1
        mas=[]
        total=''
        m=0
        s=k
        while k<=len(a)-l:
            for i in range(m, k):
                total+=a[i]+' '
            total=total.rstrip()
            mas.append(total)
            m=m+s
            k+=s
            total=''
        if l>0:
            for i in range(m, len(a)):
                total+=a[i]+' '
            total=total.rstrip()
            mas.append(total)            
        return mas
    else:
        return 0
print(my_fun(my_list,n))