# nonebot_plugin_weather_lite

使用wttr.in的天气查询 ，支持大部分wttr.in的用法。nonebot版本必须大于nonebot2.0b1。

使用://github.com/chubin/wttr.in

### 命令：

注：1.以下`天气`命令均可以使用`wttr`、`weather`、`tianqi`等效替代,

​		2.`城市名`可以使用各种语言，例如`Beijing`、`Peking`、`北京`是等效的。

​		3.支持查询全球各种地区。例如莫斯科什么的都可以。

​		4.本项目只是wttr.in在线服务的一个简陋包装。后端代码是人家写的。如果因为各种原因实现不了功能，除了确定是插件的缺陷都不要找我。

### 基础：

`天气 城市名(可选，如不给出机器人会提示获取)`

![img](https://wttr.in/beijing.png)

### 高级一点点:

`天气 城市名_format=v2`

![img](https://wttr.in/beijing_format=v2.png)

`天气 城市名_format=v3`

![img](https://wttr.in/beijing_format=v3.png)

#### 指定语言:

`天气 城市名_lang=语言`	语言可选于：

> ```
> am ar af be bn ca da de el et fr fa hi hu ia id it lt mg nb nl oc pl pt-br ro ru ta tr th uk vi zh-cn zh-tw
> ```

例如俄文查询北京：

`天气 北京_lang=ru`

![img](https://wttr.in/%E5%8C%97%E4%BA%AC_lang=ru.png)

#### 多格式联动:

wttr.in支持多种格式联动：

使用v2格式、俄文来查询北京：

`天气 北京_format=v2_lang=ru`

![img](https://wttr.in/%E5%8C%97%E4%BA%AC_format=v2_lang=ru.png)

#### 甚至支持看月相：

`天气 Moon`

![img](https://wttr.in/Moon.png)

#### 更多用法请参考wttr.in的文档！

地址：https://github.com/chubin/wttr.in

#### 缺陷：

1.无法使用`%`自定义格式。

2.其他暂时应该用不上我也没测试的功能。
