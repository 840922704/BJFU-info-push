# BJFU-info-push
本程序通过python3.7编写部署

主程序为Auto_push.py，目前实现自动检测教务处网站并推送最新的一篇通知（同一时间内有两篇则只推送最新的一篇）

如果要自动定时运行，定时运行时间间隔即是检测间隔：
1.如果本身有python环境，添加到crontab -e中即可。
2.如果像本项目初始状态一样在docker中运行了Linux隔离Anaconda文件，且本文件夹挂载到了docker中anaconda的python文件夹下，参考带绝对路径的bash自动执行脚本，通过crontab -e添加定时即可。
