import os
import sys
import time


# args
target_sum = 0
poms = []


# path validate
def is_path_dir(path):
    return os.path.exists(path) and os.path.isdir(path)


def do_clean(path):
    cmd = "cd %s ; mvn clean" % path
    os.system(cmd)


def recursion_clean(root_path):
    print root_path

    if not is_path_dir(root_path):
        return

    list = os.listdir(root_path)

    if "pom.xml" in list:
        do_clean(root_path)
        global target_sum, poms
        target_sum += 1
        poms.append(root_path + "/pom.xml")

    for file_name in list:
        recursion_clean(root_path + "/" + file_name)


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
begin_time = time.time()

env_validate()

recursion_clean(sys.argv[1])

end_time = time.time()

for pom in poms:
    print(pom)

print "\n\ndone"
print "[ last ]: %s sec" % (end_time - begin_time)
print "find pom.xml : %s" % target_sum
print "exit"
