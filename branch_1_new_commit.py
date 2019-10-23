import re
import subprocess
import sys
filename = sys.argv[1]
# val1 = subprocess.check_output('cat mod_val.txt',shell=True).decode(
#     'utf-8').strip('\n')
val1 = subprocess.Popen('cat mod_val.txt', shell=True,
                      stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip('\n')
print("before md5sum\n")
print(val1)
print("\nafter md5sum\n")

cmd = 'md5sum "{}" | cut -d" " -f1'.format(filename)
val2=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
val2 = val2.communicate()[0].decode('utf-8').strip('\n')
cmd='echo "{}" > mod_val.txt'.format(val2)
# print(cmd)
subprocess.Popen(cmd, shell=True)
# val2 = subprocess.check_output(cmd, shell=True).decode('utf-8').strip('\n')
print(val2)
if val1 != val2:
    print("file modified\n")
    print('checking for pylint\n')
    cmd = "pylint {}".format(filename)
    print(cmd)
    eq = subprocess.Popen(cmd, shell=True,
                          stdout=subprocess.PIPE).communicate()[0].decode(
        'utf-8').strip('\n')
    # print(eq.split('\n')[-1])
    score = re.search("Your code has been rated at ([-+]?\d+)", eq).group(1)
    print("pylint score of modified file is \n")
    print(score)
    score = int(score)
    # print(type(score))
    if score >= 8:
        print("pylint successfull")
    else:
        print("pylint failed, score is less than 8")
else:
    print("file not modified\n")
# subprocess.check_output('echo val2 > mod_val.txt',shell=True)
