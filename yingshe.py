import pandas as pd

# 映射函数，将原始区间[min_val, max_val]映射到[new_min, new_max]
def map_to_new_range(x, min_val, max_val, new_min, new_max):
    return (x - min_val) / (max_val - min_val) * (new_max - new_min) + new_min

# 读取数据
data_path = 'data.xlsx'
data = pd.read_excel(data_path)

# 根据已知的正确列名 'ST292' 进行映射
data['ST292'] = data['ST292'].apply(map_to_new_range, args=(5, 20, 0, 1000))

# 保存映射后的数据到新的Excel文件
output_path = 'mapped_data.xlsx'
data.to_excel(output_path, index=False)
