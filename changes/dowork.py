import sys

pr_number = sys.argv[1] #번호
pr_title = sys.argv[2] #제목

index = pr_title.find(':') 

new_title = pr_number + '.' + pr_title[0:index] +'.md'
file = open(new_title,"w")
file.write("파일에 뭔가를 쓸 수 있어야한다...")
file.close()