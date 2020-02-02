# BJFU-info-push
本程序通过python3.7编写部署

# 运行效果
![运行效果图](https://github.com/840922704/BJFU-info-push/blob/master/%E8%BF%90%E8%A1%8C%E6%95%88%E6%9E%9C%E5%9B%BE.jpg)

# 使用方法
需要更改py中的邮件模块，填入相应的邮件地址和密码即可运行。

如果要自动定时运行，定时运行时间间隔即是检测间隔：

1.如果本身有python环境，添加到crontab -e中即可。

2.如果像本项目初始状态一样在docker中运行了Linux隔离Anaconda文件，且本文件夹挂载到了docker中anaconda的python文件夹下，参考带绝对路径的bash自动执行脚本，通过crontab -e添加定时即可。

# 已实现功能
目前实现自动检测教务处网站并推送最新的一篇通知（同一时间内有两篇则只推送最新的一篇）。

调用了sqlite3进行比对。
