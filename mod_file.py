import subprocess
import re
file_list = subprocess.Popen('git diff origin/master --name-only .', shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').split('\n')
cmd = 'pylint '
i = 0 
if len(file_list) != 1:
    while i < len(file_list):
        if file_list[i].find('.py') != -1:
            cmd = cmd+' '+file_list[i]
        i = i+1
    print(cmd)
    eq = subprocess.Popen(cmd, shell=True,
                              stdout=subprocess.PIPE).communicate()[0].decode(
            'utf-8').strip('\n')
    score = re.search("Your code has been rated at ([-+]?\d+)", eq).group(1)
    print("pylint score of modified file is --> ", score)
    print("\n")
    score = int(score)
    if score >= 8:
        print("pylint successfull, score is more than 8")
    else:
        print("pylint failed, score is less than 8")
else:
    print("There are no modified files")

