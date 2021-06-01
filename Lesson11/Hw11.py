import re
from collections import UserDict,UserList
from datetime import datetime,timedelta,date

class Field:
    def __init__(self,value):
        self.__value=None
        #self.value=value
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self,new_value):
        self.__value=new_value

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value]=record
    def __str__(self):
        result=''
        for key,values in self.data.items():
            result+=f'{key}:\n{20*"="}\n{str(value)}\n'
            return result
    def iterator(self,item_n):
        counter=0
        result=''
        for key,values in self.data.items():
            result+=f'{key}:\n{20*"="}\n{str(value)}\n'
            counter+=1
            if counter>=item_n:
                yield result
                counter=0
                result=''

        
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
    def __init__(self,name,phone='', birthday=None):
        self.name=name
        self.phone=phone
        self.phones=[]
        self.new_phone=''
        self.birthday=birthday
        
    def add_phone(self, phone):
        self.phones.append(phone)

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
        self.__phone=''
        self.phone=phone
    @property  
    def phone(self):
        return self.__phone
    @phone.setter    
    def phone(self,value):
        if re.match(r'[+][0-9]{12}',value):
            self__phone=value[:13]
        else:
            print('Phone must start with + and have 12 digits. Example +380501234567')


# name=Name('Vova')
# phone=Phone('+380501558911')
# phone_1=Phone('+380637007500')
# record_1=Record(name, birthday='05.04.1987')
# record_1.add_phone(phone)
# record_1.add_phone(phone_1)

# print(record_1.days_to_birthday())
