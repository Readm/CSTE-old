
# CSTE (beta)

## 开发接口

开发新的测试样例需要在testcases文件夹中建立新的文件夹后将所有相关文件放入，并编写一个'info'文件和'default.cfg'与框架交互。

支持多层文件夹，但一个test case文件夹中将不再认为有其他testcase。

**大作业**请直接在testcases下建立自己的文件夹。文件夹中包括组员名单和自己的说明文档。

要求：

必须有一个info文件，其中属性详见sample中的例子。

+ 必须属性
  + run_vul：运行漏洞程序的命令
  + run_check：运行检查程序的命令
  + compile：默认的编译命令
  + aslr：是否打开aslr
  + dep：是否打开数据不可执行（与默认编译选项中保持一致）
  + tag：简单的tag
  + release：大作业一律为no
+ 可选属性
  + intro：简单的介绍文字
  + run_exp：交互式攻击样例的攻击程序
  + log：日志文件
 
  
还必须一个default.cfg文件，配置当前运行是正常案例还是攻击情况，是否暂停等待attach等。详见代码部分。

Q：既然能够gdb中在main中设置断点，为什么要多此一举设置一个暂停等待attach？

A：因为调试状态下与直接运行的细节实现可能不同，导致调试通过而运行却不通过，堆漏洞中出现可能性更大。

check返回值：字符串，以'Success/Fail/Other'开头，后面接上细节说明。
