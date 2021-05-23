from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record]=record.phones
        

class Record:
    def __init__(self,name,*args):
        self.name=name
        self.phones=[]
        self.new_phone=''
        
    def add_phone(self, phone):
        self.phones.append(phone)
        
    def remove_phone(self,phone):
        for i in range(len(self.phones)):
            if self.phones[i].phone == phone:
                self.phones.pop(i)
    
    def edit_phone(self,phone,new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)



class Field:
    pass
class Name(Field):
    def __init__(self,name):
        self.name=name

class Phone(Field):
    def __init__(self,phone):
        self.phone=phone