import os, getpass
list_of_expansion_books = ['doc', 'docx', 'pdf', 'epub', 'fb2']  # 'txt',
list_of_expansion_music = ['mp3']
list_of_expansion_video = ['mp4', 'avi', 'mov', 'mpg', 'mpeg', 'wmv']

def path_find_file(finded_files):
    result = []
    for i in finded_files:
        try:
            # print(i[0])
            path = i[0] + '/'
            if 'AppData' not in path and '%SystemDrive%' not in path:
                for j in i[2]:
                    name = j.split('.')[0]
                    expansion = j.split('.')[1]
                    if expansion in list_of_expansion_books:
                        result.append('book::' + name + '::' + path + j + '\n')
                    elif expansion in list_of_expansion_music:
                        result.append('music::' + name + '::' + path + j + '\n')
                    elif expansion in list_of_expansion_video:
                        result.append('video::' + name + '::' + path + j + '\n')
        except IndexError:
            pass
    return result


prog = os.getcwd()
user = getpass.getuser()
sett = open(prog + '/settings.txt', 'r')
sett1 = sett.read().split('\n')
with open('exceptions.txt', 'r') as exc:
    exceptions = [line for line in exc]
for i in sett1:
    if i == 'txt':
        list_of_expansion_books.append(i)
    elif i in ['aac', 'wav', 'ogg', 'flac']:
        list_of_expansion_music.append(i)
sett.close()
f = open((prog + '/list_of_books.txt'), 'w')
r = path_find_file(os.walk(('C://users/' + user), topdown=True))
for i in r:
    if i not in exceptions:
        f.write(i)
f.close()
