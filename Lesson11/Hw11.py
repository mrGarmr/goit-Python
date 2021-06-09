import re
from collections import UserList
from datetime import datetime,timedelta,date

class Field:
    def __init__(self,value):
        self.__value=value
        #self.value=value
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,new_value):
        self.__value=new_value

class AddressBook(UserList):
    
    data = []
    
    def add_record(self, record):
        self.data.append(record)

        
    def iterator(self,n):
        counter=0
        result=''
        
        while counter < n:
            result += next(self.data)
        yield result

        
class Birthday(Field):
    def __init__(self,value):
        self.__birthday = None
        self.birthday=value
        
    @property
    def birthday(self):
        return self.__birthday.strftime('%d.%m.%Y')
        

    @birthday.setter
    def birthday(self, birthday):
        try:
            self.__birthday = datetime.strptime(birthday, '%d.%m.%Y')
        except Exception:
            print("Incorrect format, expected day.month.year(Example:25.12.1970)")

class Record:
    def __init__(self,name,phones=None, birthday=None):
        #self.name = name
        self.phones = []
        #self.birthday = birthday
        self.user = {'Name': name.name, 'Phones': self.phones, 'Birthday': birthday}
        
    def add_phone(self, phone):
        phone=str(phone)
        try:
            num=re.match('[+]?[0-9]{12}', phone)
            if num:
                self.phones.append(phone)
            
        except:
            print('Phone must start with + and have 12 digits. Example +380501234567 ADD')          

    def days_to_birthday(self):
        if self.birthday:
            today_d = datetime.now().date()
            bday=datetime.strptime(self.birthday,"%d.%m.%Y").date()
            bday=date(today_d.year,bday.month,bday.day)
            if today_d>bday:
                bday=date(today_d.year+1,bday.month,bday.day)
                days_left=(bday-today_d)
            else:
                days_left=(bday-today_d)
            return days_left.days
        

    def remove_phone(self,phone):
        for i in range(len(self.phones)):
            if self.phones[i].phone == phone:
                self.phones.pop(i)
    
    def edit_phone(self,phone,new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)


class Name(Field):
    def __init__(self,name):
        self.name=name
        
  

class Phone(Field):
    def __init__(self,phone):
        phones=[]
        self.phones =list()
        self.__phone=phone
        
    @property  
    def phone(self):
        return self.__phone
    @phone.setter    
    def phone(self,value):
        self.__phone=''
        if re.match('[+]?[0-9]{12}',value):
            self.__phone=value
        else:
            print('Phone must start with + and have 12 digits. Example +380501234567 SETT')          
    
    #def __str__(self):
        #return self.phone
    def __repr__(self):
        return self.phone


book=AddressBook()

name2=Name('Vova')
phone=Phone('+380501558911')
phone_1=Phone('+380637007500')
record_1=Record(name2, phone, birthday='05.04.1987')
record_1.add_phone(phone)
record_1.add_phone(phone_1)
book.add_record(record_1.user)
name2=Name('Vasj')
phone=Phone('+380505558575')
record_1=Record(name2, phone)
record_1.add_phone(phone)
book.add_record(record_1.user)

print(book)
