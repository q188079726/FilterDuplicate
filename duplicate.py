import os
import re

file_sets = []
p = os.path.dirname(os.path.abspath(__file__))
logPath = os.path.join(p,'duplicate_log.txt')
divide = '====================='
def duplicate():
    root_path = os.path.dirname(os.path.abspath(__file__))
    print(root_path)
    
    gci(root_path)
    for i in range(len(file_sets)-1):
        for j in range(i+1,len(file_sets)):
            a = file_sets[i]
            b = file_sets[j]
            c = b[1]&a[1]
            if len(c) > 0 and c != {'Thumbs.db'}:
                log = 'p1:'+str(a[0])+'\n'+'p2:'+str(b[0])+'\n'+str(c)+'\n'+divide+'\n\n\n'
                print(log)
                with open(logPath,'a') as f:
                    f.write(log)

def gci(filepath):
    #遍历filepath下所有文件，包括子目录
    dirs = os.listdir(filepath)
    file_set = set()
    for dir in dirs:
        if dir.startswith('.'):
            continue
        new_dir = os.path.join(filepath,dir)
        if os.path.isdir(new_dir):
            gci(new_dir)                  
        elif os.path.isfile(new_dir): 
            ctime = os.path.getctime(new_dir)
            mtime = os.path.getmtime(new_dir)
            size = os.path.getsize(new_dir)
            file_set.add(dir+'//'+str(ctime)+str(mtime)+str(size))
            print('.')
    if len(file_set) > 0:
        file_sets.append((filepath,file_set))

def deleteFile():
    path_pattern = re.compile(r'p\d:(.*)\n')
    file_names_pattern = re.compile(r'\'(\b.*?)//')
    with open(logPath,'r') as f:
        string =  f.read()
        for paths in string.split(divide):
            p = 0
            r = re.search(path_pattern,paths)
            if r:
                p = r.group(1)
            else:
                continue
            file_names = re.findall(file_names_pattern,paths)
            
            for x in file_names:
                final_file_path = os.path.join(p,x)
                if os.path.isfile(final_file_path):
                    if os.path.exists(final_file_path):
                        print('run',final_file_path)
                        try :
                            os.remove(final_file_path)
                        except Exception as e:
                            print('err',final_file_path,e)
    print('finished delete')

if __name__ == "__main__":
    duplicate()
    # deleteFile()
    
