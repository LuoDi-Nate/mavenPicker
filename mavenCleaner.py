import os
import sys


# path validate
def is_path_dir(path):
    return os.path.exists(path) and os.path.isdir(path)


def do_clean(path):
    cmd = "mvn clean"
    os.system(cmd)


def recursion_clean(root_path):
    if not is_path_dir(root_path):
        return

    list = os.listdir(root_path)

    if "pom.xml" in list:
        do_clean(root_path)

    for file_name in list:
        recursion_clean(file_name)


def exit_with_msg(msg):
    print msg
    exit(1)


def env_validate():
    # is mvn in path
    cmd = "mvn -version"
    result = os.system(cmd)
    if result:
        exit_with_msg("check maven error! make sure mvn in your path")


# begin
env_validate()

recursion_clean(sys.argv[0])

print "done"