import pandas as pd
import sys
import real_python as rp
data = rp.data
columns = rp.columns

# df = pd.DataFrame(data=data).transpose()

# df = pd.DataFrame(data=data, index=columns).T
# print(df)

# df.to_json('test2.json')

# df.to_csv('data_csv_write.csv', sep="~")

# df = pd.read_csv('data_csv_write.csv')

# df.to_excel('panda_xl.xlsx')

# df = pd.read_excel('panda_xl.xlsx', usecols=list(columns)[:4])
df = pd.read_excel('panda_xl.xlsx')
# print(df.columns.ravel())
# for k, v in df.T.items():
    # print(f'{k}', list(v))

print(df.to_dict(orient='record'))


