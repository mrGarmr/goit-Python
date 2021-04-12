import pathlib
import sys
    
#list_dir=[]
music=[]
pictures=[]
documents=[]
archives=[]
unknown=[]
video=[]
known=('.amr','.ogg','.wav','.mp3','.svg','.jpg','.jpeg','.png','.doc','.docx','.xlsx','.pdf','.txt','.pptx','.rar','.zip','.gz','.tar',
'.avi','.mp4','.mov','.mkv')
known_list=[]
unknown_list=[]

def main(user_input):
    #global list_dir 

    if len(sys.argv)<2:
        user_input=''
    else:
        user_input=sys.argv[1]
    path=pathlib.Path(user_input)
    
    if path.exists():
        if path.is_dir():
            for element in path.iterdir():
                if element.is_file():
                    if element.suffix in known:
                        known_list.append(element.suffix)
                    else: 
                        unknown_list.append(element.suffix)
                        
                        
                    #list_dir+=[element.name]
                    if element.suffix=='.amr' or element.suffix=='.ogg' or element.suffix=='.wav' or element.suffix=='.mp3':
                        music.append(element)
                    elif element.suffix=='.svg' or element.suffix=='.jpg' or element.suffix=='.jpeg' or element.suffix=='.png':
                        pictures.append(element)
                    elif element.suffix=='.doc' or element.suffix=='.docx' or element.suffix=='.xlsx' or element.suffix=='.pdf':
                        documents.append(element)
                    elif element.suffix=='.txt' or element.suffix=='.pptx':
                        documents.append(element)
                    elif element.suffix=='.rar' or element.suffix=='.zip' or element.suffix=='.gz' or element.suffix=='.tar':
                        archives.append(element)
                    elif element.suffix=='.avi' or element.suffix=='.mp4' or element.suffix=='.mov' or element.suffix=='.mkv':    
                        video.append(element)
                    else:
                        unknown.append(element)
                else:
                    main(element)
                

if __name__=='__main__': 
    main(user_input='/user/Desktop/Хлам')
    
#print(f'В директории присутствуют следующие файлы: {list_dir}')
print(f'В директории присутствуют известные расширения:{set(known_list)}')
print(f'В директории присутствуют неизвестные расширения:{set(unknown_list)}')
print(f'В директории присутствует музыка: {music}')
print(f'В директории присутствуют изображения: {pictures}')
print(f'В директории присутствуют документы: {documents}')
print(f'В директории присутствуют архивы: {archives}')
print(f'В директории присутствует видео: {video}')
print(f'В директории присутствуют файлы с неизвестным расширением: {unknown}')