# k近邻算法

- 解决分类问题，天然可解决多分类问题
- 思想简单，效果强大
- 也可以解决回归问题（预测数值）
- 最大缺点：效率低下
  - 如果训练集有m个样本，n个特征
  - 则预测一个新数据需要o(m*n)
  - 优化：使用树结构：KD-Tree

- 缺点2：高度数据相关
- 缺点3：预测结果不具有可解释性
- 缺点4：维数灾难
  - 随着维度增加，“看似相近”的两点之间的距离越来越大
  - 解决方案：降维