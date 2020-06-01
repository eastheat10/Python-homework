class info:
    def __init__(self, name, num, sex):
        self.name = name
        self.num = num
        if sex == "male" or sex == "female":
            self.sex  = sex
        else :
            self.sex = "unknown"

    def introduce(self) :
        if self.name == "그만" :
            print("이름은 %s, 전화번호는 %s, 성별은 %s입니다"%(self.name, self.num, self.sex))
            return
        print("이름은 %s, 전화번호는 %s, 성별은 %s입니다"%(self.name, self.num, self.sex))

t = True
infoList = []
while(t):
    n = len(infoList)
    i = 0
    name = input("이름을 입력하세요: ")
    if name == "그만" :
        while(i < n) :
            infoList[i].introduce()
            i += 1
        break
    number = input("전화번호를 입력하세요: ")
    sex = input("성별을 입력하세요(male이나 female로 입력해주세요): ")
    
    infoList.append(info(name, number, sex))
    
    while(i < n+1) :
        infoList[i].introduce()
        i += 1
    print()    