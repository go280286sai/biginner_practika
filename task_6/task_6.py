text="Денис, Олег, Вася, Петя,Дима,Женя"
spisok=text.split(',')
n=0
while n!=len(spisok):
    spisok[n]=str(spisok[n]).strip()
    n+=1
print(spisok)