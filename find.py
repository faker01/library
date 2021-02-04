import os, getpass
list_of_expansion_books = ['txt', 'doc', 'docx', 'pdf', 'epub', 'fb2']
list_of_expansion_music = ['mp3', 'aac', 'wav', 'ogg', 'flac']
list_of_expansion_video = ['mp4', 'avi', 'mov', 'mpg', 'mpeg', 'wmv']

def path_find_file(finded_files):
    global list_of_expansion_books, list_of_expansion_music, list_of_expansion_video
    result = []
    for i in range(len(finded_files)):
        try:
            path = os.getcwd()
            expansion = finded_files[i].split('.')[1]
            if expansion in list_of_expansion_books:
                result.append('book::' + finded_files[i] + '::' + path + '\n')
            elif expansion in list_of_expansion_music:
                result.append('music::' + finded_files[i] + '::' + path + '\n')
            elif expansion in list_of_expansion_video:
                result.append('video::' + finded_files[i] + '::' + path + '\n')            
        except IndexError:
            pass
    return result


# os.chdir()
prog = os.getcwd()
user = getpass.getuser()
os.chdir('C://users/' + user + '/Downloads')
os.chdir('C://users/' + user + '/Documents')
f = open(prog + '\list_of_books.txt', 'w')
r = path_find_file(os.listdir())
print(prog)
for i in r:
    print(i)
    f.write(i)
f.close()
