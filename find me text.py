for file_name in os.listdir("."):
    with open(file_name, "r") as f:
        for line in f:
            if "ENSG00000172757" in line:
                print (file_name)