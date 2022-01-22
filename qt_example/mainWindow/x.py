import pandas as pd 

data = pd.read_excel('./angle.xlsx',engine='openpyxl')

dict_data = data.set_index('key').T.to_dict('list')
print(dict_data)
keys = list(dict_data)
print(keys)



with open('file.txt','w') as f:
    for i in keys:
        f.write('\''+i+'\''+':'+str(dict_data[i])+','+"\n")
