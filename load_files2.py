import glob
import re
import shutil

def load_files(root_dir:str) -> list:
    files = []
    for file in glob.glob(f"{root_dir}/**/*.py",recursive=True):
        print(file)
        files.append(file)
    return files

def copy_files(paths:list) -> list:
    print("tusam")
    new_paths = []
    for path in paths:
        orig_path = path
        path = path[:-3] + "2.py"
        new_path = path
        with open(new_path, "w") as file:
            shutil.copy(orig_path, new_path)
        file.close()
        new_paths.append(new_path)
    return new_paths

def handle_spaces(paths:list) -> list:
    for path in paths:
        lines = []
        new_lines = []
        previous_line = ""
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                match_empty = not line.strip()
                if match_empty == True:
                    if not previous_line.strip():
                        continue
                new_lines.append(line)
        file.close()
        with open(path, "w") as file:
            for line in new_lines:
                file.writelines(line)
        file.close()
    return paths

def handle_line_length(paths:list) -> list:
    for path in paths:
        lines = []
        new_lines = []
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if len(line) > 79:
                    print(line)
                    line1 = line[:80] + "\"" + "\\"
                    new_lines.append(line1)
                    line2 = "\n" + "\"" + line[80:]
                    new_lines.append(line2)
                else:
                    new_lines.append(line)
            if not lines[-1].strip():
                print("tusam")
                new_lines.append("")
        file.close()
        with open(path, "w") as file:
            for line in new_lines:
                file.writelines(line)
        file.close()
    return paths

def handle_spaces_between_functions(paths:list) -> list:
    for path in paths:
        lines = []
        new_lines = []
        previous_line = ""
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:

                match_def = line.find("def")


                match_class = line.find("class",)

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
        with open(path, "w") as file:
            for line in new_lines:
                file.writelines(line)
        file.close()
    return paths

def handle_tabs_and_spaces(paths:list) -> list:
    for path in paths:
        lines = []
        new_lines = []
        counter = 0
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line.rstrip()
                line = line.replace("\t", " ")
                for character in line:
                    if character == " ":
                        counter += 1
                    else:
                        break
                print(counter)
                line = line[:counter] + re.sub("\s{2,}"," ", line[counter:])
                print(line)
                counter = 0
                new_lines.append(line)
        file.close()
        with open(path, "w") as file:
            for line in new_lines:
                file.writelines(line)
        file.close()
    return paths

def handle_imports(paths:list) -> list:
    for path in paths:
        line_group1=[]
        line_group2=[]
        line_group3=[]
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
        with open(path, "w") as file:
            for line in line_group1,line_group2,line_group3:
                file.writelines(line)
        file.close()
    return paths

def main():
    files = load_files("D:/gitProjects/blacky/python_prettifier/")
    new_files = copy_files(files)
    new_files = handle_tabs_and_spaces(new_files)
    new_files = handle_spaces(new_files)
    new_files = handle_imports(new_files)
    new_files = handle_spaces_between_functions(new_files)
    new_files = handle_line_length(new_files)
if __name__=="__main__":
    main()
