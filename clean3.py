import pandas as pd

# 读取Excel文件
data = pd.read_excel('clean2.xlsx')  # 确保文件路径正确

# 定义需要替换值的列名
columns = ['ST292Q01JA', 'ST292Q02JA', 'ST292Q03JA', 'ST292Q04JA', 'ST292Q05JA', 'ST292Q06JA']

# 定义替换规则
replacements = {97: 0, 1: 4, 2: 3, 3: 2, 4: 1}

# 对指定列应用替换规则
for col in columns:
    data[col] = data[col].map(replacements)

# 显示替换后的数据以进行验证
print(data[columns].head())

# 如果需要，保存到新的Excel文件
data.to_excel('cleaned3.xlsx', index=False)
