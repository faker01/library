import os
list_of_expansion = ['txt', 'doc', 'docx', 'pdf', 'epub', 'fb2']
# .txt ; .doc ; .docx ; .pdf ; .epub ; .fb2

def path_find_file(finded_files):
    global list_of_expansion
    result = []
    for i in range(len(finded_files)):
        expansion = finded_files[i].split('.')[1]
        if expansion in list_of_expansion:
            result.append(finded_files[i])
    return result
