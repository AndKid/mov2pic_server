# mov2pic_server
利用python的Flask框架部署的server，用于爬取All In ONE http://www.wufafuwu.com/a/ONE_tupian/ 和图解电影网 http://www.k165.com/ 的内容，以json格式返回，客户端程序 [mov2pic_client](https://github.com/AndKid/mov2pic_client)
链接对应关系
------------
###All In One
http://mov2pic.duapp.com/background ------ http://www.wufafuwu.com/a/ONE_tupian/list_11_1.html 爬取随机图片  
http://mov2pic.duapp.com/bg_hdpi ------ http://www.wufafuwu.com/a/ONE_tupian/2016/0424/4731.html 爬取高清图片

###图解电影网
默认页（导航页首页）：http://mov2pic.duapp.com/ ------ http://www.k165.com/movies.html  
导航页：http://mov2pic.duapp.com/?uri=/movies/tag/3 ------ http://www.k165.com/movies/tag/3 ，uri为nav的值
* movie_des: 电影描述
* movie_img: 电影插图
* movie_title: 电影标题
* movie_url: 指向电影内容
* nav: 类别导航, "nav": {"/movies.html": "首页", "/movies/original/1": "原创", "/movies/tag/1": "恐怖", "/movies/tag/2": "悬疑", "/movies/tag/3": "喜剧", "/movies/tag/4": "情色", "/movies/tag/5": "血腥", "/movies/tag/6": "奇幻", "/movies/tag/7": "剧情"}

内容页：http://mov2pic.duapp.com/content?uri=/movies/1624.html ------ http://mov2pic.duapp.com/content?uri=/movies/1624.html ，uri为movie_url的值
* content: 包括文字描述和图片链接
* title: 电影标题
* next: 下一页分页

Flask相关命令
------------
```shell
(virtualenv venv)
. venv/Scripts/activate
pip freeze > requirement.txt
pip install -r requirement.txt

supervisord -c supervisor.conf                             通过配置文件启动supervisor
supervisorctl -c supervisor.conf status                    察看supervisor的状态
supervisorctl -c supervisor.conf reload                    重新载入 配置文件
supervisorctl -c supervisor.conf start [all]|[appname]     启动指定/所有 supervisor管理的程序进程
supervisorctl -c supervisor.conf stop [all]|[appname]      关闭指定/所有 supervisor管理的程序进程
```
博客链接
------------
[Mov2pic Server Introduction](http://andkid.github.io/2016/04/25/mov2pic_server/)
