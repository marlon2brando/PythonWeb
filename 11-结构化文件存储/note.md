# 格式化文件存储
- xml,json
- 为了解决不同设备之间的信息交换
- xml，可读性强
- json，更简洁

## XML 文件
- 参考资料：
   - 百度xml 格式

- XML解释：可扩展标记语言
   - 标记语言：语言中使用尖括号括起来的文本字符串标记
   - 可扩展：用户可以自己定义需要的标记
   - 例如;
   - 是W3C组织制定的标准
   - XML描述的是数据本身，即数据的结构和语义
   - HTML侧重于如何显示web页面的数据


- XML文件的构成

   1. 处理命令（可以认为一个文件内只有一个处理指令）
      - 最多只有一行
      - 且必须在第一行
      - 内容是与xml本身处理起相关的一些声明或者指令
      - 以xml 关键字开头
      - 一般用于声明xml的版本和采用的编码
         - version属性是必须的
         - encoding 属性用来支出xml解释器使用的编码

   2. 根元素（一个文件内只有一个根元素）
      - 在整个xml文件中，可以把它看做一个树形结构
   3. 子元素
      - 根元素下面的所有元素都是子元素
   4. 属性
   5. 内容
      - 标签中的存储的信息
   6. 注释
      - 起说明作用的信息
      - 注释不能嵌套在标签里面
      - 只有在注释开始和结尾使用注释
      - 三短横线只能出现在注释开头和结尾

- 保留字符的处理
   - xml中使用的富豪可能跟实际富豪相冲突，典型的就是左右尖括号

   - 使用实体引用'EntityRefrence，可以理解成转义
              <score> math>80 </score>
              <score> math&gt;80 </score>

   - 把含有保留字符的部分放在CDATA快内容
            <!CDATA [ select name,age from Student where score > 80 ]>

   - 常用的需要转义的保留字符和对应的实体引用
      - &：&AMP；
      - <: &lt
      - >: &gt;
      - ...
- XML 标签的命名规则

   - Pascal命名法
   - 以单词表示，首字母大小
   - 大小写严格区分
   - 配对标签必须一致


# xml 访问

## 读取
- xml读取分两个技术，SAX，DOM
- SAX（simple api for xml）
   - 基于事件驱动
   - 利用SAX解析文档设计到解析器和事件处理两部分
   - 特点：
      - 快
      - 流式读取
- DOM
   - 是W3C规定的XML编程接口
   - 一个xml文件要在缓存中以树形结构保存，读取
   - 用途
      - 定位浏览XML任何一个节点信息
      - 添加删除相应位置

   - minidom
      - minidom.parse(filename):加载读取的xml文件，也可以是xml代码
      - doc.documentElement:
      - node.getAttribute(attr_name):获取节点属性
      - node.getElementByTagName(tage_name):得到一个节点的对象集合
      - node.childnodes:
      - node.firstNodes:
      - node.attributes[tage_name]

   - etree
      - 以树形结构来表示xml
      - root.geeiterator:得到相应的可迭代的node集合
      - root.iter
      -
