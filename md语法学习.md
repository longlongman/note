标题

this is an H1           <!--setext风格-->
=============
this is an H2
-------------

# 这是H1                  <!--atx风格-->
## 这是H2
### 这是H3
#### 这是H4
##### 这是H5
###### 这是H6

区块引用

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

嵌套引用

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

> ## 这是一个标题。
> 
> 1. 这是第一行列表项。
> 2. 这是第二行列表项。
> 
> 给出一些例子代码：
> 
>     return shell_exec("echo $input | $markdown_script");

列表

* Red
* Green
* Blue

+ Red
+ Green
+ Blue

- Red
- Green
- Blue

有序列表

1. bird
2. mchale
3. parish

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

代码区块

这是一个普通的段落
    
    这是一个代码区块
        龙思宇
            龙思宇

分隔线

***
---
* * *
- - -
___
_ _ _

区段元素
链接

This is [an example](http://example.com/ "Title") inline link.<!--内联式-->

[This link](http://example.net/) has no title attribute

This is [an example][id] reference-style link.<!--参考式-->

[id]: http://example.com/  "Optional Title Here"

强调

*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

小段代码

Use the `printf()` function.
