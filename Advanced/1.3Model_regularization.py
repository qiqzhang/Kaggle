#-*- coding:utf-8 -*-
#!/usr/bin/python
'''
模型正则化 Regularization 提高模型的泛化Generalization能力 
避免参数模型过拟合  Overfitting
'''
# 比萨数据  直径和对应售价
# 输入训练样本的特征以及目标值，分别存储在变量X_train与y_train之中
X_train = [[6], [8], [10], [14], [18]]
y_train = [[7], [9], [13], [17.5], [18]]

######## 线性模型预测#######
# 从sklearn.linear_model中导入LinearRegression
from sklearn.linear_model import LinearRegression
# 使用默认配置初始化线性回归模型
regressor = LinearRegression()
# 直接以披萨的直径作为特征训练模型
regressor.fit(X_train, y_train)

# 导入numpy并且重命名为np
import numpy as np
# 在x轴上从0至25均匀采样100个数据点
xx = np.linspace(0, 26, 100)
xx = xx.reshape(xx.shape[0], 1)#转换成一列

# 以上述100个数据点作为基准，预测回归直线
yy = regressor.predict(xx)
# 对回归预测到的直线进行作图
import matplotlib.pyplot as plt#画图
plt.scatter(X_train, y_train)#样本数据散点图
plt.plot(xx, yy, color="red", linewidth=2.5, linestyle="-",  label=u"模型维度=1")
plt.axis([0, 25, 0, 25])# 图大小
plt.xlabel(u'比萨直径')
plt.ylabel(u'售价')
#plt.legend(handles = [plt1],labels = ["Degree=1"], loc='upper left')
plt.legend(loc='upper left')# 在画图 里面添加 label
plt.show()

print '线性回归准确度： ', regressor.score(X_train, y_train)


##########2项多项式模型##########
# 从sklearn.preproessing中导入多项式特征产生器
from sklearn.preprocessing import PolynomialFeatures
# 使用PolynominalFeatures(degree=2)映射出2阶多项式特征，存储在变量X_train_poly2中
poly2 = PolynomialFeatures(degree=2) # 模型
X_train_poly2 = poly2.fit_transform(X_train)#训练
# 以线性回归器为基础，初始化回归模型。尽管特征的维度有提升，但是模型基础仍然是线性模型
regressor_poly2 = LinearRegression()
# 对2次多项式回归模型进行训练
regressor_poly2.fit(X_train_poly2, y_train)
# 从新映射绘图用x轴采样数据
xx_poly2 = poly2.transform(xx)

# 使用2次多项式回归模型对应x轴采样数据进行回归预测
yy_poly2 = regressor_poly2.predict(xx_poly2)
# 分别对训练数据点、线性回归直线、2次多项式回归曲线进行作图
plt.scatter(X_train, y_train) #训练数据散点图
plt.plot(xx, yy, color='red', linewidth=2.5, linestyle="-",  label=u"模型维度=1")
plt.plot(xx, yy_poly2, color='blue', linewidth=2.5, linestyle="-",  label=u"模型维度=2")
# 'blue'  'yellow'
plt.axis([0, 25, 0, 25])
plt.xlabel(u'比萨直径')
plt.ylabel(u'售价')
plt.legend(loc='upper left') # 图例位置  左上
plt.show()
# 输出2次多项式回归模型在训练样本上的R-squared值
print '二阶多项式模型准确度：', regressor_poly2.score(X_train_poly2, y_train)

##########4项多项式模型##########
# 从sklearn.preproessing中导入多项式特征产生器
from sklearn.preprocessing import PolynomialFeatures
# 使用PolynominalFeatures(degree=4)映射出4阶多项式特征，存储在变量X_train_poly2中
poly4 = PolynomialFeatures(degree=4) # 模型
X_train_poly4 = poly4.fit_transform(X_train)#训练
# 以线性回归器为基础，初始化回归模型。尽管特征的维度有提升，但是模型基础仍然是线性模型
regressor_poly4 = LinearRegression()
# 对4次多项式回归模型进行训练
regressor_poly4.fit(X_train_poly4, y_train)
# 从新映射绘图用x轴采样数据
xx_poly4 = poly4.transform(xx)

# 使用4次多项式回归模型对应x轴采样数据进行回归预测
yy_poly4 = regressor_poly4.predict(xx_poly4)
# 分别对训练数据点、线性回归直线、4次多项式回归曲线进行作图
plt.scatter(X_train, y_train) #训练数据散点图
plt.plot(xx, yy, color='red', linewidth=2.5, linestyle="-",  label=u"模型维度=1")
plt.plot(xx, yy_poly4, color='yellow', linewidth=2.5, linestyle="-",  label=u"模型维度=4")
# 'blue'  'yellow'
plt.axis([0, 25, 0, 25])
plt.xlabel(u'比萨直径')
plt.ylabel(u'售价')
plt.legend(loc='upper left') # 图例位置  左上
plt.show()
# 输出4次多项式回归模型在训练样本上的R-squared值
print '四阶多项式模型准确度：', regressor_poly4.score(X_train_poly4, y_train)



#########在测试数据集上进行模型的测试验证#######
# 准备测试数据
X_test = [[6], [8], [11], [16]]
y_test = [[8], [12], [15], [18]]
# 使用测试数据对线性回归模型的性能进行评估
regressor.score(X_test, y_test)
# 使用测试数据对2次多项式回归模型的性能进行评估
X_test_poly2 = poly2.transform(X_test)
regressor_poly2.score(X_test_poly2, y_test)
# 使用测试数据对4次多项式回归模型的性能进行评估
X_test_poly4 = poly4.transform(X_test)
regressor_poly4.score(X_test_poly4, y_test)

#############引入惩罚项 正则化##########
# 从sklearn.linear_model中导入Lasso   
# 正则化模型  L1范数正则化   （f-y) + lam * ||W|| 加入权重的一阶范数
from sklearn.linear_model import Lasso
# 从使用默认配置初始化Lasso
lasso_poly4 = Lasso()
# 从使用Lasso对4次多项式特征进行拟合
lasso_poly4.fit(X_train_poly4, y_train)
# 对Lasso模型在测试样本上的回归性能进行评估
print 'L1范数正则化后4阶多项式正确率： '
print lasso_poly4.score(X_test_poly4, y_test)
# 输出Lasso模型的参数列表
print 'L1范数正则化4阶多项式参数列表： '
print lasso_poly4.coef_
# 回顾普通4次多项式回归模型过拟合之后的性能
print '未正则化的4阶多项式正确率： '
print regressor_poly4.score(X_test_poly4, y_test)
# 回顾普通4次多项式回归模型的参数列表
print '未正则化4阶多项式参数列表： '
print regressor_poly4.coef_
# 输出上述这些参数的平方和，验证参数之间的巨大差异
print '未正则化4阶多项式参数平方和： '
print np.sum(regressor_poly4.coef_ ** 2)


# 从sklearn.linear_model导入Ridge
from sklearn.linear_model import Ridge   # L2 范数正则化
# 使用默认配置初始化Riedge
ridge_poly4 = Ridge()
# 使用Ridge模型对4次多项式特征进行拟合
ridge_poly4.fit(X_train_poly4, y_train)
# 输出Ridge模型在测试样本上的回归性能
print 'L2范数正则化后4阶多项式正确率： '
print ridge_poly4.score(X_test_poly4, y_test)
# 输出Ridge模型的参数列表，观察参数差异
print 'L2范数正则化4阶多项式参数列表： '
print ridge_poly4.coef_
# 计算Ridge模型拟合后参数的平方和
print 'L2正则化4阶多项式参数平方和： '
print np.sum(ridge_poly4.coef_ ** 2)


