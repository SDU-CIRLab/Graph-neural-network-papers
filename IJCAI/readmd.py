import os
import shutil

CON=r'IJCAI2020'

AllFiles=[]
filename=os.listdir('./md')

lookup={}
rank=0
for files in filename:
    lookup[files]=str(rank)+'.md'
    rank+=1


with open(CON+'.md','w',encoding='utf-8') as f:
    f.write("## "+CON+"包含的相关文章如下\n")
    for files in filename:
        f.write('[{}]({})'.format(files.split('.')[0],'./md/'+lookup[files]))
        f.write('\n')

for files in filename:
    
    os.rename('./md/'+files,'./md/'+lookup[files])
