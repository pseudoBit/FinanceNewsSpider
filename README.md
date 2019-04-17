# FinanceNewsSpider
基于python2.7的快兰斯新闻爬虫，讲信息推送到telegram的channel上

## 使用方法

#### 需要用到的包

此程序基于python2.7，所以使用之前请先查询python版本
```
python -V
```
若显示的是 ```python 2.7```, 则可以进行下一步；若否，请将python 2.7装到服务器（或者计算机）中，当然更好的方式是建个[虚拟环境](https://www.jianshu.com/p/44ab75fbaef2)来作此配置，易于管理。下面我会以python2/pip2来表示我用的python版本是python2.7。

打开虚拟环境``` ```
```
source ~/venv/bin/activate
```
安装所需的爬虫包```urllib2```和```re```（大部分python库都配了，就不写在这了）
```
pip2 install urllib2
```
将telegram机器人的api和你创建channel的api分别填入```FinanceNewsSpider.py```中的```boi_api```和```user_api```中（注意要放在```' '```）


```
nohup python2 sina_finance.py &
```
