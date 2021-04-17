import re


def normalize(text):
    
    cyrilic_f=['А','Б','В','Г','Ґ','Д','Е','Є','Ж','З','И','І','Ї','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ю','Я',
                'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я']
    cyr=','.join(cyrilic_f)            

    trans_f=['A','B','V','H','G','D','E','E','Z','Z','Y','I','I','Y','K','L','M','N','O','P','R','S','T','U','F','H','T','C','S','S','Y','Y',
              'а', 'b', 'v', 'h', 'g', 'd', 'е', 'e', 'z', 'z', 'y', 'i', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 't', 'c', 's', 's', 'y', 'y']
    trans=','.join(trans_f)
    
    dictionary = str.maketrans(cyr, trans)
    clean_text = re.sub(r'[^\w\s]', '_', text)
    
    result=clean_text.translate(dictionary)
    return result
