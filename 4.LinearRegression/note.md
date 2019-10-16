# 线性回归法

> 主要用于解决回归问题
>
> 思想简单，容易实现
>
> 许多非线性模型的基础
>
> 结果具有可解释性
>
> 蕴含机器学习的很多思想

## 1. 简单线性回归

- 简单线性回归：样本特征只有一个
  - y = ax + b

- 目标：找到a,b，使得  $\sum_{i=1}^m$  (y<sup>(i)</sup>  - ax<sup>(i)</sup> - b)<sup>2</sup>最小 
  - 损失函数
  - 效用函数
  - 统称目标函数

- 一类机器学习基本思路
  - 通过分析问题，确定问题的损失函数或者效用函数；通过最优化损失或效用函数，获得机器学习的模型

## 2. 最小二乘法

- 求J(a,b)极值 -> 求导=0

![草图](https://user-images.githubusercontent.com/33116315/66361340-0abaac80-e9b1-11e9-8f18-01c657067d2a.png)

![草图](https://user-images.githubusercontent.com/33116315/66361375-2c1b9880-e9b1-11e9-89ee-7c84d1f04544.png)

![草图](https://user-images.githubusercontent.com/33116315/66361448-6a18bc80-e9b1-11e9-9391-01bdc1acc8c9.png)

![草图](https://user-images.githubusercontent.com/33116315/66361524-a8ae7700-e9b1-11e9-8d84-4f110b2c3f15.png)

![草图](https://user-images.githubusercontent.com/33116315/66361578-e14e5080-e9b1-11e9-89bd-363109005b58.png)

## 3. 实现

## 4. 向量化

- 对于a的计算方式
- 可以将循环替换为矩阵乘法

## 5. 回归算法评价

- MSE 均方误差(Mean Squared Error)
- RMSE 均方根误差(Root Mean Squared Error)
- MAE 平均绝对误差(Mean Absolute Error)

## 6. R Squared

- R^2 <= 1
- R^2 越大越好，当我们的预测模型不犯错误时，R^2最大值为1
- 若R^2 < 0 说明，可能我们的数据不存在线性关系
- 1 - mse/var  （方差）