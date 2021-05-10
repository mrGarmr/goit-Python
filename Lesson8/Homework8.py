from datetime import datetime,timedelta,date

users={'Konnor':'16.05.1991', 'John':'14.05.1991', 'Вася':'15.05.1991', 'Саша':'16.05.1991', 'Даша':'13.05.1991', 'Паша':'16.05.1991'}
    


def congratulate(users):
    
    today_d = datetime.now().date()
    cong=timedelta(days=7)
    
    monday=[]
    tuesday=[]
    wednesday=[]
    thursday=[]
    friday=[]
    
    for key, value in users.items():
        
        bday=datetime.strptime(value,"%d.%m.%Y").date()
        bday=date(today_d.year,bday.month,bday.day)

        if (bday-today_d)<=cong:
            bday_day=bday.strftime('%A')
            if bday_day=="Monday":
                monday.append(key)
            elif bday_day=='Tuesday':
                tuesday.append(key)
            elif bday_day=='Wednesday':
                wednesday.append(key)
            elif bday_day=='Thursday':
                thursday.append(key)
            elif bday_day=='Friday':
                friday.append(key)
            else:
                monday.append(key)
            
    return print(f'Monday: {monday};\nTuesday: {tuesday};\nWednesday: {wednesday};\nThursday: {thursday};\nFriday: {friday};')
            
        
    
if __name__=='__main__':   
    congratulate(users)