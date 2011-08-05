import os,shutil,fnmatch

def joinfiles(path,output):
    # otwieram plik do zapisu
    f=open(output,"a")
    wildcard_split = path.split(os.path.sep)
    path = os.path.sep.join(wildcard_split[:-1])
    wildcard = wildcard_split[-1]
    
    for r,d,fi in os.walk(path):
    for files in fi:
        if fnmatch.fnmatch(files, wildcard):
            with open(os.path.join(r,files)) as g:
                shutil.copyfileobj(g,f)
    f.close()
