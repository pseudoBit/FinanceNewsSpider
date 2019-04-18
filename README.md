# FinanceNewsSpider
基于python2.7的快兰斯新闻爬虫，讲信息推送到telegram的channel上

## 使用方法

#### 需要用到的包

此程序基于python2.7，所以使用之前请先查询python版本
```
python -V
```
若显示的是 ```python 2.7```, 则可以进行下一步；若否，请将python 2.7装到服务器（或者计算机）中，当然更好的方式是建个[虚拟环境](https://www.jianshu.com/p/44ab75fbaef2)来作此[配置](https://www.tensorflow.org/install/pip)，易于管理。下面我会以python2/pip2来表示我用的python版本是python2.7。

打开虚拟环境```[ ]```（若要停止虚拟环境则输入```deactivate [ ]```）
```
source ~/venv/bin/activate [ ]
```
安装所需的爬虫包```urllib2```，```threading```和```re```（大部分python库都配了，就不写在这了）
```
pip2 install urllib2
```
将telegram机器人的api和你创建channel的api分别填入```FinanceNewsSpider.py```中的```boi_api```和```user_api```中（注意要放在```' '```中）。

机器人api的创建和寻找方式：
1. 在telegram中寻找BotFather(@BotFather)
2. ```/start```后，给它发送```/newbot```。然后按提示依次输入你要创造的Bot的名称和用户名，然后BotFather就会告知你的机器人的API是什么了（红色字符）
3. 如果你已经创造了机器人，但不知道它的api。那就可以问BotFather```/mybots```，然后选择你先管理的Bot，然后选```API Token```，那你就能获得此机器人的```API```
4. 此时你的```bot_api```该是```bot_api = ```API```

频道（channel）的api的创建和寻找方法（现在只支持公共频道）
1. 在telegram客户端中选择创建```New Channel```
2. 选择频道类型为```Public```，然后设置频道链接```https://t.me/XXX```,这里的```XXX```根据个人偏好设置
3. 如今你可以通过输入```@XXX```来链接到你的频道
4. 此时你的```user_api```该是```user_api = ['@XXX']```

把机器人添加到所建频道中，并给予其管理员权限。

填入这两个api，程序就完成了，若要普通运行，则输入
```
python2 sina_finance.py
```
若要在后台一直运行，则输入
```
nohup python2 sina_finance.py &
```
如此一来，就算你关掉服务器的窗口程序也不会停止运作，也会每```5s```更新一次情况。要查看后台进程，输入```ps```或者```jobs```，用```kill```来关闭普通后台程序。若要关掉后台循环的爬虫，则输入
```
ps ax | grep sina_finance.py
```
基本相关操作就是以上这些。望使用愉快。
