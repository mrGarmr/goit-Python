book={}

def error_handler(func):
    def inner(*args):
        try:
            result=func(*args)
            return result
        except:
            result=input_error()
            return result
    return inner   
    
def exit():
    print('Good bye!')
    esc=False
    return esc

def greeting():
    return 'How can I help you?'

@error_handler
def handler(user_input):
    global user_list
    user_list=user_input.split()
    user_list[0]=user_list[0].lower()
    if user_list[0] in ANSWEARS.keys():
        return ANSWEARS[user_list[0]]()
    else:
        return input_error()

def main():
    global user_input, user_list
    esc=True
    while esc:
        user_input=input('What do you want?\n')
        result=handler(user_input)
        if result:
            print(result)
        elif result==None:
            pass
        else:
            break
        
@error_handler       
def show():
    print(10*'*')
    for key,value in book.items():
        print(f'{key}\'s number {value}')
    print(10*'*')    
    return 

@error_handler
def phone():
    return f'{user_list[1]}\'s number is {book[user_list[1]]}'

            
            
def input_error():
    return print('Wrong input! Type "help" for commands or "exit" to exit')

def help_func():
    return print(' Type "add" + space + name + space + phone to add new contact\n Type "change" + space + name to change contact\'s phone\n Type "phone" + space + contact name to see phone number\n Type "show" to show you all phonebook\n Type "exit" to exit')
    
@error_handler
def contact():
    book[user_list[1]]=user_list[2]
    return f'{user_list[1]}\'s number {book[user_list[1]]} added'

@error_handler
def contact_change():
    old=book[user_list[1]]
    book[user_list[1]]=user_list[2]
    return f'You changed {user_list[1]}\'s number for {book[user_list[1]]}. Old number was {old}'
     
     
    
ANSWEARS={'hello': greeting,'add': contact, 'change': contact_change,'show': show,'good':exit, 'close': exit, 'exit': exit, 'phone':phone, 'help':help_func}

    
if __name__ =='__main__':
    main()

