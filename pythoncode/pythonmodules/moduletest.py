import os, sys


# OS - chdir, mkdir, getcwd, listdir, rmdir
# OS - system, name, path
# OS - chmod, chown , user, group, stat

if os.path.exists("/Users/premkumargontrand/AITrainingApril2026/pythoncode/testdir"):
    print("Directory already exists")
    sys.exit(200)
else:
    os.mkdir("/Users/premkumargontrand/AITrainingApril2026/pythoncode/testdir")

# print(os.getcwd())
# print(os.listdir("/Users/premkumargontrand/AITrainingApril2026/pythoncode"))
# 0 -- success other than 0 every number is failure 
# 200 -- In API level 200 mean success other 200 every number is failure 
# https enpoint different error code 




