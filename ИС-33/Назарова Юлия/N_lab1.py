from datetime import date 
import datetime 
 
inf=("Назарова", "Юлия", "Валерьевна", 4, 8, 2004) 
 
subject={
    "Химия" : 4,
    "Биология" : 5, 
    "Русский язык" : 4, 
    "Литература" : 5, 
    "Иностранный язык" : 4, 
    "История" : 5, 
    "Геометрия" : 5,
    "Физика" : 4, 
    "Алгебра" : 4,    
    "Физическая культура" : 4, 
    "География" : 5,
    "Информатика" : 5,
    "История России" : 5,
    "ОБЖ" : 5,
    "Обществознание" : 4, 
    } 
relatives=["Валерий", "Елена", "Наталья", "Дмитрий", "Наталья"] 
 
kiwa="Кузя"



number = ((int(inf[3]) + int(inf[4])**2 + int(inf[5])) % 21 +1)

 
def srrating(): 
    summa=0 
    for i in subject: 
        summa += subject[i] 
    summa /= len(subject) 
    return round(summa, 3) 
print ("№1", srrating()) 
 
relatives.append(inf[1]) 
print("№2", list(set(relatives))) 
relatives.remove("Юлия") 
 
def subjectlen(): 
    summa = 0 
    for i in subject: 
        summa += len(i) 
    return summa 
print("№3", subjectlen()) 
 
obj = " " 
for m in subject: 
    obj += m 
uniq=[] 
for i in obj: 
    n=0 
    for j in obj: 
        if i==j: 
            n += 1
        if n>1:
            break
    if n == 1: 
       uniq += [i] 
print ("№4", uniq) 
 
binkiwa = ' '.join(format(ord(x), '08b') for x in kiwa) 
print("№5", binkiwa) 
 
sortrel=relatives 
sortrel.sort(reverse=True)
print("№6", sortrel)
print(relatives)

tday=datetime.date.today()
bday=datetime.date(int(inf[5]), int(inf[4]), int(inf[3]))  
result=str(tday-bday) 
print("№7", result.split()[0]) 
 
print("№8.Введите индекс предмета который хотите добавить в FIFO очередь. Признак конца ввода -> end")
FIFO=[]
objlist=list(subject.keys())
while (True): 
    indobj=input()
    if (indobj=="end"): 
        for i in range(len(FIFO)): 
            print(FIFO[i]) 
        break
    if int(indobj)>=0 and int(indobj)<len(objlist):
        FIFO.append(objlist[int(indobj)])
    else:
        print("Некорректный ввод. Введите значение от 0 до 15.")
 
print("№9")
print("Номер", number, "это Тисок")
print("Введите индекс от 0 до 4:")
while (True): 
    index=int(input()) 
    if index < len(sortrel) and index >=0: 
        sortrel[int(index)]="Тисок" 
        break
    print("Некорректный ввод.Введите индекс заново:")
print(sortrel)
print(relatives)
linked_list = {}
for i in range(len(relatives)):
        linked_list[relatives[i]] = relatives[(i+1)%len(relatives)]
print("#10", linked_list)
variant=(len("НазароваЮлияВалерьевна"))*(len(relatives[0])+len(relatives[1])+len(relatives[2])+len(relatives[3])+len(relatives[4]))%4
print("№11 Мой вариант", variant)
print("Числа трибоначи. Функция выводит первые N чисел Трибоначчи.")
N=int(input("Введите N:"))

def tribonachi(n):
    numbers = [1, 1, 1]
    while len(numbers) < n:
        numbers.append(numbers[-1] + numbers[-2] + numbers[-3])
    if n > 3: print(*numbers)
    else: print(*numbers[:n])
    
tribonachi(N)

print("P.S Не сразу увидела что есть варианты поэтому сделала еще первые 2 варианта функций))))")

def alikvot(n, firstn):
    newn=0
    if n==firstn:
        print(n)
    if n==1:
        print(0)
        return
    else:
        for i in range(1, n//2+1):
            if n%i==0:
                newn+=i
        print(newn)
        return alikvot(newn, firstn)
A=int(input("Введите число, функция выведет аликвотную последовательность для него:"))
alikvot(A, A)

def silvestr(n):
    pred=1
    new=2
    for i in range(1, n+1):
        print(new)
        new=(pred*new)
        pred=new
        new+=1
print("Функция выводит первые M чисел последовательности Сильвестра")
M=int(input("Введите М:"))
silvestr(M)




print("The end.")
