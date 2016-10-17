import os

list_of_modified_files = []
for file_name in os.listdir("."):
    if ".fasta" in file_name:
        is_modified = False
        new_file_content = []
        with open(file_name, "r") as f:
            for line in f:
                if ":" in line:
                    line = line.replace(":", "-")
                    is_modified = True
                new_file_content.append(line)
        #create the new file
        with open(file_name.replace(".fasta","_modified.fasta"),"w") as f:
            for line in new_file_content:
                f.write(line)
        if is_modified:
            list_of_modified_files.append(file_name)

with open("modified.txt","w") as f:
    if not list_of_modified_files:
        print ("Empty array")
        f.write(("No files were modified")+"\n")
    else:
        for file in list_of_modified_files:
            f.write((file)+"\n")
print("All done!")
        