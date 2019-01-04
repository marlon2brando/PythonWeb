# XPath
- 在 XML中文件查找信息的一套规则、语音，根据xml的元素或者属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp

# xpath 开发工具
- 开源XPath的表达式工具：XMLQuire
- Chrome插件，XPath Helper
- Firefox :XPath Checker

# 选取节点
- nodename: 选择子节点的所有子节点
- /  : 从根节点开始选取
- // : 选取节点，不考虑位置，一般组成列出返回
- .  : 选取当前节点
- .. : 选取当前节点的父节点
- @  : 选取属性

- XPath 中查找一般按照路径方法查找

# 谓语 -predicates
- []
- [1]
- [last()]
- [position() < 3]

- @