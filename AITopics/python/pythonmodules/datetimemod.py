from datetime import datetime
import os
time_now = datetime.now()
# print(time_now)
# print(time_now.year)
# print(time_now.month)
# print(time_now.day)
# print(time_now.strftime("%Y-%m-%d %H:%M:%S"))
# print(time_now.strftime("%d-%m-%Y"))
# print(time_now.strftime("%d/%m/%Y"))   # string format of the time 

applogtime = time_now.strftime("%d_%m_%Y_%H_%M_%S")

dirpath = "/Users/premkumargontrand/AITrainingApril2026/pythoncode/testdir/"

if os.path.exists(dirpath):
    print("Directory already exists and i am going to create a app log file inside that")
    os.system(f"echo 'This is a log file created at {applogtime}' > applog_{applogtime}.log")
    print("Log file created successfully")
else:
    os.mkdir(dirpath)
    os.chdir(dirpath)
    os.system(f"echo 'This is a log file created at {applogtime}' > applog_{applogtime}.log")
    print("Directory and log file path created successfully")
