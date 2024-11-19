#print(__name__)
#print(type(__name__))   #在.py裡的__name__一定是字串
import random
def get_names(nums:int = 2)->list[str]:
    with open('names.txt', mode='r', encoding = 'utf-8') as f:  
        names_str = f.read()
    names:list[str] = names_str.split(sep= '\n')    #name後面加上:list[str] 增加程式可讀性
    names_list = random.choices(names,k=nums)
    return names_list

def generate_students(names:list[str])->list[dict]:
    students:list[dict] = [] 
    for name in names:
        #print(f'姓名:{name}')
        height = random.randint(140, 190)
        #print(f'身高:{height}公分')
        weight = random.randint(50, 110)
        #print(f'體重:{weight}公斤')
        BMI = weight / ((height/100)**2) 
        #print(f'BMI:{BMI:.0f}')
        status=get_bmistatus(BMI)
        #print(f'狀態:{status}')
        #print("===================")
        student={'name':name,'height':height,'weight':weight,'BMI':format(BMI,'.0f'),'status':status}
        students.append(student)
    return students

def get_bmistatus(BMI:int)->str: 
    if BMI >=35:
        status="重度肥胖"
    elif BMI >= 30:
        status="中度肥胖"
    elif BMI >= 27:
        status="輕度肥胖"
    elif BMI >= 24:
        status="過重"
    elif BMI >= 18.5:
        status="正常範圍"
    else:
        status="體重過輕"
    return status

if __name__== '__main__':       #可便於判斷主程式從何開始
    nums = int(input('請輸入人數:'))
    print(f'請輸入人數:{nums}')
    student_names:list[str] = get_names(nums = nums)
    s1:list[dict]  = generate_students(names = student_names)
    #for name in s1:
    #    print(f"姓名: {name['name']}")
    #    print(f"身高: {name['height']}")
    #    print(f"體重: {name['weight']}")
    #    print(f"BMI: {name['BMI']}")
    #    print(f"狀態: {name['status']}")
    #    print("=================")
    for name in s1:
        for key,value in name.items():
            print(f'{key}:{value}')
        print("=============")
