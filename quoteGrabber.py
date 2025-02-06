import os 

path = "C:\Users\snp32\Downloads\ProgrammingClass\ProgrammingProject1\LogFileAnalyzer\Quotes"

os.chdir(path) 
  
def read_text_file(file_path): 
    with open(file_path, 'r') as f: 
        print(f.read()) 
  
  

for file in os.listdir(): 
 
    if file.endswith(".txt"): 
        file_path = f"{path}\{file}"
   
        read_text_file(file_path) 