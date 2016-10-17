import os

list_of_modified_files = []
for file_name in os.listdir("."):
    is_modified = False
    if ".emf" in file_name:
        with open(file_name, "r") as f:
            new_file_content = []
            for line in f:
                if line[0]=="(":
                    i = 0
                    replaced_string=[]
                    temp_line=[]
                    while i<len(line):
                        if line[i]==":":
                            if (line[i-1].isalpha() or line[i+1].isalpha()) and line[i+2] != ".":
                                temp_line.append("-")
                                is_modified = True
                                replaced_string.append(line[i-2:i+3])
                            else:
                                temp_line.append(line[i])
                        else:
                            temp_line.append(line[i])
                        i=i+1
                    if is_modified:
                        list_of_modified_files.append(file_name+" "+' '.join(replaced_string))  
                    new_file_content.append(''.join(temp_line))
        #create the new file
        with open(file_name.replace(".emf",".newick"),"w") as f:
            for line in new_file_content:
                f.write(line)
with open("modified_trees.txt","w") as f:
    if not list_of_modified_files:
        print ("Empty array")
        f.write(("No files were modified")+"\n")
    else:
        for file in list_of_modified_files:
            f.write((file)+"\n")
print("All done!")
        
