import glob
import re


def load_files(root_dir:str) -> list:
    files = []
    for file in glob.glob(f"{root_dir}/**/*.py",recursive=True):
        print(file)
        files.append(file)
    #print(len(files))
    return files

#def copy_files(files)

def handle_whitespaces() -> list:
    

def handle_line_length() -> list:
    for line in lines:
        if len(line) > 79:
            line = line[:80] + "\\n" + line[80:]

def handle_spaces_between_functions() -> list:
    paths = ["C:/Programming/PythonPrettifier/python_prettifier/ugly_file_tabs.py"]
    formatted_file = "ffile_tabs.py"
    lines = []
    new_lines = []
    previous_line = ""
    flag = False
    for path in paths:
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                match_def = line.find("def")
                match_class = line.find("class",)
                #match_empty = not line.strip()
                #print(match_empty)
                # print(match)
                # print(line)
                # if match_empty == True:
                #     if not previous_line.strip():
                #         previous_line = line
                #         continue
                if match_def!=-1:
                    if previous_line.strip():
                        previous_line = previous_line + "\n"
                if match_class!=-1:
                    if previous_line.strip():
                        previous_line = previous_line + "\n\n"
                new_lines.append(previous_line)
                previous_line = line
            new_lines.append(previous_line)
        file.close()
    
    with open(formatted_file, "w") as ffile:
        for line in new_lines:
            ffile.writelines(line)


def handle_tabs_and_spaces(paths:list) -> list:
    paths = ["C:/Programming/PythonPrettifier/python_prettifier/ugly_file_tabs.py"]
    formatted_file = "ffile_tabs.py"
    lines = []
    counter = 0
    for path in paths:
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line.rstrip()
                line = line.replace("\t", "    ")
                for character in line:
                    if character == " ":
                        counter += 1
                    else:
                        break
                print(counter)
                line = line[:counter] + re.sub("\s{2,}"," ", line[counter:])
                print(line)   #tu ce se odmah pisat u isti fajl nakon sto se implementira fja za copy files
                counter = 0
    #izbrojati tabove(spaceovi) na pocetku linije
    #replaceati sve vise od 2 spacea REGEX = \s{2,}
    #vratit tabove na pocetku u obliku spaceova(koji su prebrojani)

    #     file.close()
    # with open(formatted_file, "w") as ffile:
    #     for line in line_group1,line_group2,line_group3:
    #         ffile.writelines(line)
    # ffile.close()
    # return paths

def handle_imports(paths:list) -> list:
    paths = ["C:/Programming/PythonPrettifier/python_prettifier/ugly_file.py"]
    formatted_file = "ffile.py"
    line_group1=[]
    line_group2=[]
    line_group3=[]
    for path in paths:
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                match_import = line.find("import ",0,7)
                match_from = line.find("from ",0,5)
                if match_import != -1:
                    line = line.replace(",","\nimport ")
                    line_group1.append(line)
                elif match_from != -1:
                    line_group2.append(line)
                else:
                    line_group3.append(line)
        file.close()
    with open(formatted_file, "w") as ffile:
        for line in line_group1,line_group2,line_group3:
            ffile.writelines(line)
    ffile.close()
    return paths


def main():
    files = load_files("C:/Programming")
    #handle_imports(files)
    #handle_tabs_and_spaces(files)
    handle_spaces_between_functions()


if __name__=="__main__":
    main()
