import pandas as pd

# 加载数据
data = pd.read_excel('clean1.xlsx')

# 为每个字段定义十列的名称
fields = [
    ['PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH', 'PV6MATH', 'PV7MATH', 'PV8MATH', 'PV9MATH', 'PV10MATH'],
    ['PV1MCCR', 'PV2MCCR', 'PV3MCCR', 'PV4MCCR', 'PV5MCCR', 'PV6MCCR', 'PV7MCCR', 'PV8MCCR', 'PV9MCCR', 'PV10MCCR'],
    ['PV1MCQN', 'PV2MCQN', 'PV3MCQN', 'PV4MCQN', 'PV5MCQN', 'PV6MCQN', 'PV7MCQN', 'PV8MCQN', 'PV9MCQN', 'PV10MCQN'],
    ['PV1MCSS', 'PV2MCSS', 'PV3MCSS', 'PV4MCSS', 'PV5MCSS', 'PV6MCSS', 'PV7MCSS', 'PV8MCSS', 'PV9MCSS', 'PV10MCSS'],
    ['PV1MCUD', 'PV2MCUD', 'PV3MCUD', 'PV4MCUD', 'PV5MCUD', 'PV6MCUD', 'PV7MCUD', 'PV8MCUD', 'PV9MCUD', 'PV10MCUD'],
    ['PV1MPEM', 'PV2MPEM', 'PV3MPEM', 'PV4MPEM', 'PV5MPEM', 'PV6MPEM', 'PV7MPEM', 'PV8MPEM', 'PV9MPEM', 'PV10MPEM'],
    ['PV1MPFS', 'PV2MPFS', 'PV3MPFS', 'PV4MPFS', 'PV5MPFS', 'PV6MPFS', 'PV7MPFS', 'PV8MPFS', 'PV9MPFS', 'PV10MPFS'],
    ['PV1MPIN', 'PV2MPIN', 'PV3MPIN', 'PV4MPIN', 'PV5MPIN', 'PV6MPIN', 'PV7MPIN', 'PV8MPIN', 'PV9MPIN', 'PV10MPIN'],
    ['PV1MPRE', 'PV2MPRE', 'PV3MPRE', 'PV4MPRE', 'PV5MPRE', 'PV6MPRE', 'PV7MPRE', 'PV8MPRE', 'PV9MPRE', 'PV10MPRE']
]

# 计算每组列的平均值，并作为新列添加到数据集中
for field in fields:
    new_column_name = field[0][2:7] + '_avg'  # 创建新列名，如 'MATH_avg', 'MCCR_avg', 等
    data[new_column_name] = data[field].mean(axis=1)

# 保存修改后的数据
data.to_excel('clean2.xlsx', index=False)
