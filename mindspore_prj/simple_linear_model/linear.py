# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/9/13 14:43
"""

from mindspore import context

context.set_context(mode=context.GRAPH_MODE, device_target="GPU")

import numpy as np
import mindspore as ms
from mindspore import Tensor


def get_data(num, w=2.0, b=3.0):
    np_x = np.ones([num, 1])
    np_y = np.ones([num, 1])

    for i in range(num):
        x = np.random.uniform(-10.0, 10.0)
        np_x[i] = x
        noise = np.random.normal(0, 1)
        y = x * w + b + noise
        np_y[i] = y

    return Tensor(np_x, ms.float32), Tensor(np_y, ms.float32)


import matplotlib.pyplot as plt

eval_x, eval_label = get_data(50)
x1, y1 = eval_x.asnumpy(), eval_label.asnumpy()

plt.scatter(x1, y1, color="red", s=5)
plt.title("Eval data")
plt.show()


from mindspore.common.initializer import TruncatedNormal
from mindspore import nn

#TruncatedNormal(sigma=0.01)
# | Args:
# | sigma(float): The
# sigma of the array.Default: 0.01.
# | Returns: Array, truncated normal array.
# Dense(in_channels, out_channels, weight_init='normal', bias_init='zeros',
#       has_bias=True, activation=None)

from mindspore.common.initializer import TruncatedNormal
from mindspore import nn

net = nn.Dense(1,1,TruncatedNormal(0.02),TruncatedNormal(0.02))
print("weight:", net.weight.default_input[0][0], "bias:", net.bias.default_input[0])
