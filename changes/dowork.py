import sys

pr_title = sys.argv[1] #제목
pr_number = sys.argv[2] #번호

index = pr_title.find(':') 

new_title = pr_number + '.' + pr_title[0:index] +'.md'
file = open(new_title,"w")
file.write(pr_title[index+1:])
file.close()