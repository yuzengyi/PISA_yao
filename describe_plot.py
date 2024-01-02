import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
data_path = 'mapped_data.xlsx'
data = pd.read_excel(data_path)

# 转换性别字段为可读形式
data['ST004D01T'] = data['ST004D01T'].map({1: 'Female', 2: 'Male'})

# 转换地区代码为可读形式
area_mapping = {'TAP': 'Taipei', 'HKG': 'Hong Kong', 'MAC': 'Macao'}
data['CNT'] = data['CNT'].map(area_mapping)

# 提取需要的数据进行描述性统计
descriptive_stats = data[['ST292', 'MATH_avg', 'CNT', 'ST004D01T']].groupby(['CNT', 'ST004D01T']).describe()
print(descriptive_stats)
# 准备绘图数据
plot_data = pd.melt(data, id_vars=['CNT', 'ST004D01T'], value_vars=['ST292', 'MATH_avg'],
                    var_name='Variable', value_name='Score')

# 使用暗度色系
dark_colors = sns.color_palette("dark")
# 使用另一种更鲜艳的色系
bright_colors = sns.color_palette("tab10")

# 绘制柱状图
g = sns.catplot(x="CNT", y="Score", hue="ST004D01T", col="Variable",
                data=plot_data, kind="bar", palette=bright_colors, height=5, aspect=1)

# 设置图表标题和坐标轴标签
g.fig.suptitle('Anxiety and Math Average Scores by Area and Gender', y=1.05)
g.set_axis_labels("Area", "Score")

# 展示图表
plt.show()
# 设置莫兰迪色系
morandi_colors = ["#6a4c93", "#f4acb7", "#9d8189", "#f7ede2", "#b8bedd"]

# 为了清晰区分ST292和MATH_avg，我们将为每个变量创建一个单独的柱状图
plt.figure(figsize=(14, 10))

# 创建ST292的柱状图
plt.subplot(2, 1, 1)  # 第一行的第一个图
sns.barplot(x='CNT', y='Score', hue='ST004D01T', data=plot_data[plot_data['Variable'] == 'ST292'], palette=morandi_colors)
plt.title('Anxiety Scores by Country and Gender')
plt.xlabel('Country')
plt.ylabel('Anxiety Score')
plt.legend(title='Gender')

# 创建MATH_avg的柱状图
plt.subplot(2, 1, 2)  # 第二行的第一个图
sns.barplot(x='CNT', y='Score', hue='ST004D01T', data=plot_data[plot_data['Variable'] == 'MATH_avg'], palette=morandi_colors)
plt.title('Math Average Scores by Country and Gender')
plt.xlabel('Country')
plt.ylabel('Math Score')
plt.legend(title='Gender')

# 调整布局
plt.tight_layout()

# 展示图表
plt.show()
