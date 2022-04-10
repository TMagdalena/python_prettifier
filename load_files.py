import glob
#import re


def load_files(root_dir=str) -> list():
    files = []
    for file in glob.glob(f"{root_dir}/**/*.py",recursive=True):
        print(file)
        files.append(file)
    print(len(files))
    return files

#def copy_files(files)


def handle_imports(paths=list) -> list:
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
    handle_imports(files)


if __name__=="__main__":
    main()