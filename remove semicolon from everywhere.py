import os

list_of_modified_files = []
for file_name in os.listdir("."):
    if ".fasta" in file_name and not "modified" in file_name:
        is_modified = False
        new_file_content = []
        with open(file_name, "r") as f:
            strings_to_replace = []
            for line in f:
                if ":" in line:
                    strings_to_replace.append(line[1:].replace(" ","").replace("\n",""))
                    line = line.replace(":", "-")
                    is_modified = True                    
                new_file_content.append(line)
        #create the new file
        with open(file_name.replace(".fasta","_modified.fasta"),"w") as f:
            for line in new_file_content:
                f.write(line)
        if is_modified:
            list_of_modified_files.append(file_name+" "+' '.join(strings_to_replace))
            for file_name2 in os.listdir("."):
                found_nhx = False
                found_nh = False
                if file_name[:file_name.index(".")] in file_name2 and file_name2 != file_name:
                    if 'nhx' in file_name2 and not found_nhx:
                        found_nhx = True
                    elif 'nh' in file_name2 and not found_nh:
                        found_nh = True
                    elif not 'modified.fasta' in file_name2:
                        print ("Found wrong file " + file_name2)
                        list_of_modified_files.append("Found wrong file " + file_name2)
                        break
                    with open(file_name2, "r") as f:
                        found_brackets = False
                        for line in f:
                            if line[0]=="(" and not found_brackets:
                                for string_to_replace in strings_to_replace:
                                    if string_to_replace in line:
                                        line=line.replace(string_to_replace,string_to_replace.replace(":","-"))
                                    else:
                                        print ("Failed to find "+string_to_replace+" in " + file_name2)
                                        list_of_modified_files.append("Failed to find "+string_to_replace+" in " + file_name2) 
                                found_brackets = True
                            elif line[0]=="(":
                                print ("Found more than one line that start with ( in "+file_name2)
                                list_of_modified_files.append("Found more than one line that start with ( in "+file_name2)
                            with open(file_name2.replace(".emf",".newick"),"w") as f:
                                f.write(line)

with open("modified.txt","w") as f:
    if not list_of_modified_files:
        print ("Empty array")
        f.write(("No files were modified")+"\n")
    else:
        for file in list_of_modified_files:
            f.write((file)+"\n")
print("All done!")
