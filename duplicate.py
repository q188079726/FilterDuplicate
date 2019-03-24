import os

file_sets = []
p = os.path.dirname(os.path.abspath(__file__))
logPath = os.path.join(p,'duplicate_log.txt')

def duplicate():
    root_path = os.path.dirname(os.path.abspath(__file__))
    print(root_path)
    
    gci(root_path)
    for i in range(len(file_sets)-1):
        for j in range(i+1,len(file_sets)):
            a = file_sets[i]
            b = file_sets[j]
            c = b[1]&a[1]
            if len(c) > 0:
                with open(logPath,'a') as f:
                    f.write('p1:'+str(a[0])+'\n'+'p2:'+str(b[0])+'\n'+str(c)+'\n=====================\n\n\n')

def gci(filepath):
    #遍历filepath下所有文件，包括子目录
    dirs = os.listdir(filepath)
    file_set = set()
    for dir in dirs:
        new_dir = os.path.join(filepath,dir)            
        if os.path.isdir(new_dir):
            gci(new_dir)                  
        elif os.path.isfile(new_dir): 
            if dir != '.DS_Store':
                file_set.add(dir)
            else:
                print("***",dir)
    if len(file_set) > 0:
        file_sets.append((filepath,file_set))



def gci2(filepath):
#遍历filepath下所有文件，包括子目录
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)            
    if os.path.isdir(fi_d):
        gci2(fi_d)                  
    else:
        print(os.path.join(filepath,fi_d))




if __name__ == "__main__":
    duplicate()
    # gci2(p)
    