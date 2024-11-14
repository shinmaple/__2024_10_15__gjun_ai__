import random
def get_names(nums:int = 2)->list[str]:
    with open('names.txt', mode='r', encoding = 'utf-8') as f:  
        names_str = f.read()
    names:list[str] = names_str.split(sep= '\n')    #name後面加上:list[str] 增加程式可讀性
    names_list = random.choices(names,k=nums)
    return names_list
def generate_students(names:list[str])->list[dict]:
    students:list[dict] = []    #先給students這個dict塞一個空的
    for name in names:
        #print(name)
        chinese = random.randint(50, 100)
        #print(chinese)
        english = random.randint(50, 100)
        #print(english)
        math1 = random.randint(50, 100)
        #print(math1)
        math2 = random.randint(50, 100)
        #print(math2)
        student={'name':name,'chinese':chinese,'english':english,'math1':math1,'math2':math2}
        students.append(student)
    return students
nums = int(input('輸入學生數量(最多十位:)'))
student_names:list[str] = get_names(nums = nums)    #這裡的nums=nums不會搞混,因為nums= 程式會知道是引數名稱的呼叫、後面的nums是上一行輸入的值
students:list[dict] = generate_students(names = student_names)
print(students)