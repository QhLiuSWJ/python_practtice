# -*- coding: UTF-8 -*-
"""
@author:QHL
@file:Forcast 6.py
@time:2020/03/02
"""

import numpy as np
import paddle as paddle
import paddle.fluid as fluid
from PIL import Image
import matplotlib.pyplot as plt
import os


# 定义多层感知器
def multilayer_perceptron(inp):
    # 第一个全连接层，激活函数为ReLU
    hidden1 = fluid.layers.fc(input=inp, size=100, act='relu')
    # 第二个全连接层，激活函数为ReLU
    hidden2 = fluid.layers.fc(input=hidden1, size=100, act='relu')
    # 以softmax为激活函数的全连接输出层，大小为10
    prediction = fluid.layers.fc(input=hidden2, size=10, act='softmax')
    return prediction


train_reader = paddle.batch(paddle.reader.shuffle(paddle.dataset.mnist.train()
                                                  , buf_size=512),
                            batch_size=128)
test_reader = paddle.batch(paddle.dataset.mnist.test(), batch_size=128)
temp_reader = paddle.batch(paddle.dataset.mnist.train(), batch_size=1)
temp_data = next(temp_reader())
# print(temp_data)

# 定义输入输出层
image = fluid.layers.data(name='image', shape=[1, 28, 28], dtype='float32')  # 单通道，28*28像素值
label = fluid.layers.data(name='label', shape=[1], dtype='int64')  # 图片标签

# 获取分类器
model = multilayer_perceptron(image)
# 获取损失函数和准确率函数
cost = fluid.layers.cross_entropy(input=model, label=label)  # 使用交叉熵损失函数,描述真实样本标签和预测概率之间的差值
avg_cost = fluid.layers.mean(cost)
acc = fluid.layers.accuracy(input=model, label=label)

# 定义优化方法
optimizer = fluid.optimizer.AdamOptimizer(learning_rate=0.001)  # 使用Adam算法进行优化
opts = optimizer.minimize(avg_cost)
# 定义一个使用CPU的解析器
place = fluid.CPUPlace()
exe = fluid.Executor(place)
# 进行参数初始化
exe.run(fluid.default_startup_program())

# 定义输入数据维度
feeder = fluid.DataFeeder(place=place, feed_list=[image, label])

# 开始训练和测试
for pass_id in range(5):
    # 进行训练
    for batch_id, data in enumerate(train_reader()):  # 遍历train_reader
        train_cost, train_acc = exe.run(program=fluid.default_main_program(),  # 运行主程序
                                        feed=feeder.feed(data),  # 给模型喂入数据
                                        fetch_list=[avg_cost, acc])  # fetch 误差、准确率
        # 每100个batch打印一次信息  误差、准确率
        if batch_id % 100 == 0:
            print('Pass:%d, Batch:%d, Cost:%0.5f, Accuracy:%0.5f' %
                  (pass_id, batch_id, train_cost[0], train_acc[0]))

    # 进行测试
    test_accs = []
    test_costs = []
    # 每训练一轮 进行一次测试
    for batch_id, data in enumerate(test_reader()):  # 遍历test_reader
        test_cost, test_acc = exe.run(program=fluid.default_main_program(),  # 执行训练程序
                                      feed=feeder.feed(data),  # 喂入数据
                                      fetch_list=[avg_cost, acc])  # fetch 误差、准确率
        test_accs.append(test_acc[0])  # 每个batch的准确率
        test_costs.append(test_cost[0])  # 每个batch的误差
    # 求测试结果的平均值
    test_cost = (sum(test_costs) / len(test_costs))  # 每轮的平均误差
    test_acc = (sum(test_accs) / len(test_accs))  # 每轮的平均准确率
    print('Test:%d, Cost:%0.5f, Accuracy:%0.5f' % (pass_id, test_cost, test_acc))

    # 保存模型
    model_save_dir = "F:/python/PaddlePaddle/demo"
    # 如果保存路径不存在就创建
    if not os.path.exists(model_save_dir):
        os.makedirs(model_save_dir)
    print('save models to %s' % model_save_dir)
    fluid.io.save_inference_model(model_save_dir,  # 保存推理model的路径
                                  ['image'],  # 推理（inference）需要 feed 的数据
                                  [model],  # 保存推理（inference）结果的 Variables
                                  exe)  # executor 保存 inference model


# 对图片进行预处理
def load_image(file):
    im = Image.open(file).convert('L')  # 将RGB转化为灰度图像，L代表灰度图像，灰度图像的像素值在0~255之间
    im = im.resize((28, 28), Image.ANTIALIAS)  # resize image with high-quality 图像大小为28*28
    im = np.array(im).reshape(1, 1, 28, 28).astype(np.float32)  # 返回新形状的数组,把它变成一个 numpy 数组以匹配数据馈送格式。
    # print(im)
    im = im / 255.0 * 2.0 - 1.0  # 归一化到【-1~1】之间
    print(im)
    return im


img = Image.open('5.png')
plt.imshow(img)  # 根据数组绘制图像
plt.show()  # 显示图像

# In[ ]:


infer_exe = fluid.Executor(place)
inference_scope = fluid.core.Scope()

# 最后把图像转换成一维向量并进行预测，数据从feed中的image传入。fetch_list的值是网络模型的最后一层分类器，所以输出的结果是10个标签的概率值，这些概率值的总和为1。

# In[ ]:


# 加载数据并开始预测
with fluid.scope_guard(inference_scope):
    # 获取训练好的模型
    # 从指定目录中加载 推理model(inference model)
    [inference_program,  # 推理Program
     feed_target_names,  # 是一个str列表，它包含需要在推理 Program 中提供数据的变量的名称。
     fetch_targets] = fluid.io.load_inference_model(model_save_dir,
                                                    # fetch_targets：是一个 Variable 列表，从中我们可以得到推断结果。model_save_dir：模型保存的路径
                                                    infer_exe)  # infer_exe: 运行 inference model的 executor
    img = load_image('5.png')

    results = exe.run(program=inference_program,  # 运行推测程序
                      feed={feed_target_names[0]: img},  # 喂入要预测的img
                      fetch_list=fetch_targets)  # 得到推测结果,

    for number, acc in enumerate(results[0][0]):
        print(f'是{number}的概率为：{acc * 100:.5f}%')
# 拿到每个标签的概率值之后，我们要获取概率最大的标签，并打印出来。

# In[ ]:
print(results)
# 获取概率最大的label
lab = np.argsort(results)  # argsort函数返回的是result数组值从小到大的索引值
# print(lab)
print("该图片的预测结果的label为: %d" % lab[0][0][-1])  # -1代表读取数组中倒数第一列
print()