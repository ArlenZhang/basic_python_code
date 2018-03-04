'''
	Scrapy应用框架：一个为了爬取网站数据，提取结构性数据而编写的应用框架，数据挖掘、信息处理或存储历史数据等程序中。
运用anaconda在shell界面进入arlenTF环境下并用如下pip指令进行安装
       conda install scrapy 安装最新版本
	scrapy抓取网站需要四个步骤：
		1. 创建一个Scrapy项目
		2. 定义一个Item容器
		3. 编写爬虫
		4. 存储内容
	了解Scrapy框架和它的组件之间的交互，组件之间的数据流，画图见file
'''
#在shell里面创建scrapy项目 ：scrapy startproject Learn32 在对应的C:\Users\arlen\Documents\Learn32即为新建的项目

#在items文件下定义容器，保存爬取到的数据，首先要知道资源的链接、资源描述、资源内容三者建模
'''
	联系对象：http://blog.csdn.net/database_zbye/article/details/8607638
	对该网址下面的每一个推荐学习课程的链接、描述、内容的下载存储
'''

#编写爬虫文件

'''
	到此为止我们先进入文件夹用scrapy crawl pSpider 命令爬取之后再根目录下多了一个文件即为爬取的网页源代码内容，这里
框架就会找名字为pSpider的蜘蛛爬取网页
'''

#从网页文件中提取数据，之前用的是正则表达式，这里用基于XPath和CSS的表达式机制--ScrapySelectors
'''
	用scrapyshell打开具体网址
	scrapy shell "xxx" 
	response.selector.xpath('')=response.xpath()
	response.selector.('')
	response.selector.re('')
	
XPath(): '//title'找到title html标签，extract()提取内容输出，(//title/text()')提取title里面的文本内容
xpath怎么避免多余元素的错误过滤？通过class的值得使用增进筛选 (//title[@class='course']/text()).extract()即可。

到分析代码中修改文件获取指定数据，将shell代码回归生产线
'''

#存放到items里面去





