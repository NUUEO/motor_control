from this import d
import pandas as pd

data = pd.read_excel("./angle.xlsx",engine='openpyxl')
df = pd.DataFrame(data,columns=['key','馬達1','馬達2','馬達3'])
d_names = df.set_index('key').T.to_dict('list')

#print(d_names)
dict
d_list = list(d_names)

with open('file.txt','w') as f:
    j = 0
    for i in d_list:
        n = "'"+d_list[j]+ "' :" + str(d_names[i])+",\n"
        f.write(n)
        j+=1
