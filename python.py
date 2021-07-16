import os
import json
#To get the list of Files in the Directory
dir=os.listdir('/home/machi16/appd')
path='/home/machi16/appd/'
b=''
count=0
final_count=0
def noofnodes(count):
    final_count=count
    return final_count
for i in dir:
    y='\0'
    #To open a file1
    f1=open(path+i)
    db2 = json.load(f1)
    db2.sort(key=lambda x: x['tierName'], reverse=False)
    k=len(i)-5
    with open(str(i[0:k]) + '.md', 'w') as f:
        f.write(
            "|| Application_name ||              Agent_Type ||                   Tier_name ||              AppAgent_version ||                  NumberOfnodes ||")
        a=i[0:k]
        # To seggregate the required columns
        for element in db2:
            for key, value in element.items():
                if key == 'appAgentVersion':
                    if value!='\0':
                        l = value[14:]
                        b=l[0:13]
                if key == 'agentType':
                    c = value
                if key == 'tierName':
                    x=value
                    if x==y:
                        count+=1
                    if x!=y:
                        if y!='\0':
                            final=noofnodes(count)
                            f.write(str(final))
                            f.write(" | ")
                        count = 1
                        y = x
                        f.write('\n')
                        f.write(" | ")
                        f.write(a)
                        f.write(" |          ")
                        f.write(c)
                        f.write(" |         ")
                        f.write(x)
                        f.write(" |          ")
                        f.write(b)
                        f.write(" |                         ")
                        #f.write(c)
                       # f.write(" |                 ")
        f.write(str(count))
        f.write(" |")
