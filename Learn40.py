# numpy是列表类的，pandas更像字典版本的numpy，便于灵活筛选
import pandas as pd
import numpy as np
# 创建序列(默认行0累加排序)
print("---------------创建--------------")
s = pd.Series([1, 3, 5, 7, 9, np.nan])
print("创建默认序列: ")
print(s)

# 指定行描述,列指定为a b c d
dates = pd.date_range('20160101', periods=6)
df_o = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print("指定行列属性标签: ")
print(df_o)

# 用字典作为参数创建data frame
df = pd.DataFrame({'attr1': 1, 'attr2': 2}, index=['val1'])
print("以字典进行初始化数据: ")
print(df)
print("dtypes值: ")
print(df.dtypes)

# 实际使用中排序的实现
print("---------------排序--------------")
dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['attr1', 'attr2', 'attr3', 'attr4'])
sorted_r = df.sort_values(by='attr1', ascending=False)
print("按某属性列排序: ")
print(sorted_r)
sorted_r = df.sort_index(ascending=True)
print("按行索引值排序: ")
print(sorted_r)

print("---------------索引--------------")
print("第一列属性值: ")
print(df.attr1)

print("前2行数据: ")
print(df[0:2])

# select by label 字典label
print("loc输出: ")
print(df_o.loc['20160102'])
print(df_o.loc[:, ['a', 'b']])

# select by position iloc
print("iloc输出: ")
print(df_o.iloc[3:5, 1:3])
print(df_o.iloc[[3, 5], [1, 3]])

# mixed selection : ix
print("ix输出: ")
print(df_o.ix[:3, ['a', 'd']])

# boolean selection
print("boolean索引输出: ")
print(df_o['a'] > 0)
print(df[df_o['a'] > 0])

print("---------------设置值--------------")
# 赋值
df_o.loc['20160102', 'a'] = 211
df_o.iloc[2, 2] = 985
print("输出设置之后的数据: ")
print(df_o)

# 添加列
df_o['e'] = np.nan
df_o['f'] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
print("添加列f、e: ")
print(df_o)

# 空数据处理
# 对存在空的数据的丢弃 axis控制行列0代表行
print("删除空数据列: ")
print(df_o.dropna(axis=1, how='any'))  # how=['any', 'all']  any as default

# 空数据调整
if np.any(df_o.isnull()):
    fill_r = df_o.fillna(0)
    print("填充之后的结果: ")
    print(fill_r)

print("---------------Excel导入导出--------------")
data = pd.read_excel('data/data1.xlsx')
print("输出指定单元格的数据：", data.ix[0, 'userName'])

print("---------------合并DataFrame--------------")
# concat
data1 = pd.read_excel('data/data1.xlsx')
data2 = pd.read_excel('data/data2.xlsx')
c_data = pd.concat([data1, data2], axis=0, ignore_index=True)
print("concat: ")
print(c_data)
# concat不加参数只能拼接属性对应的情况否则
df1 = pd.DataFrame(np.ones((3, 3))*0, columns=['a', 'b', 'c'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 3))*1, columns=['e', 'b', 'c'], index=[2, 3, 4])
c_data = pd.concat([df1, df2], axis=0)
print("outer join concat: ")
print(c_data)
# 解决: 参数join ['inner', 'outer'] 默认outer
c_data = pd.concat([df1, df2], axis=0, join="inner", ignore_index=True)
print("inner join 列 concat: ")
print(c_data)
# 同样对于行合并
c_data = pd.concat([df1, df2], axis=1, join="inner")
print("inner join 行 concat: ")
print(c_data)

# append 将df2加到df1上面去
res = df1.append(df2, ignore_index=True)
print("append 结果: ")
print(res)

print("---------------merge高级合并--------------")
arr_one = pd.DataFrame(np.ones((3, 3)), index=[1, 2, 3], columns=['attr1', 'attr2', 'key'])
arr_two = pd.DataFrame(np.ones((3, 3)), index=[1, 2, 3], columns=['attr1', 'attr2', 'key'])
res = pd.merge(arr_one, arr_two, on=['key'])
print("输出基于key的merger: ")
print(res)
# 这里的默认为how=inner合并保留相同的元素，支持多key合并
# how=right的时候以右边的也就是第二个数组的key为基准

# 当然也可以不用key进行何必还可以用left_index=True和right_index=True来通过index合并

# 如果合并的属性名字相同但是合并还想区分所属对像，用suffix属性
# plot和panda 见matplotlib代码
