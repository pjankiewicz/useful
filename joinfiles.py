import os,shutil,fnmatch

def joinfiles(path,output,recursive=False):
    """
    Join files (matches wildcards) to one file
    """
    
    # otwieram plik do zapisu
    f=open(output,"w")
    wildcard_split = path.split(os.path.sep)
    path = os.path.sep.join(wildcard_split[:-1])
    wildcard = wildcard_split[-1]

    for r,d,fi in os.walk(path):
        if recursive or (r == "." or r == path):
            for files in fi:
                if fnmatch.fnmatch(files, wildcard):
                    with open(os.path.join(r,files)) as g:
                        shutil.copyfileobj(g,f)
    
    f.close()
