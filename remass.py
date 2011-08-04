import re
import os
import fnmatch

"""
Mass regex file operations v. 0.1
"""

class RegexMass():
    def __init__(self,path):
        """
        Get path from arguments
        
        Path can be 
        - path with filenames (accepts wildcards)
        - current directory
        """
        
        wildcard_split = path.split(os.path.sep)
        if len(wildcard_split) > 1:
            self.path = os.path.sep.join(wildcard_split[:-1])
            self.wildcard = wildcard_split[-1]
        else:
            self.path = "."
            self.wildcard = path
        self.get_files()
    
    def get_files(self):
        # Reads files into dictionary
        self.files = {}
        for file in os.listdir(self.path):
            if fnmatch.fnmatch(file, self.wildcard):
                with open(self.path + os.path.sep + file) as input:
                    self.files[file] = input.read()
                    
    def findall(self,pattern, re_options=None):
        # Uses re.findall on files
        pattern = re.compile(pattern, re_options)
        results = []
        for filename,contents in self.files.items():
            for result in pattern.findall(contents):
                results.append([result,filename])
        return results
    
    def sub(self,pattern,repl,re_options=None):
        # Uses re.sub on files
        pattern = re.compile(pattern, re_options)
        for filename,contents in self.files.items():
            self.files[filename] = re.sub(pattern, repl, contents)
            
    def writeback(self):
        # Writes back changes
        for filename,contents in self.files.items():
            with open(self.path + os.path.sep + filename,"w") as output:
                output.write(contents)
                output.close()
