## 前提条件  
##### 本部分是为了确保项目可以运行
1. 本项目使用的工具以及版本 (其它版本没有测试)
    * hadoop3.2.1
    * spark2.2.1
    * mysql8
    * python3
    * 用到的python模块可用pip工具下载，命令：pip install *
2. 必要的扩展工具
    * 请把项目中的jdbc文件放在spark安装目录的jars文件下

## 使用方法
1. 进入FruitFree文件夹
2. 在命令行中设置临时变量
   * windows
        1. set FLASK_APP=flaskr
        2. set FLASK_ENV=development (调试模式)
        3. 进入flaskr目录，修改config.py文件夹，设置数据库账号密码
        4. flask init-db (初始化数据库)
   * linux
        1. export FLASK_APP=flaskr
        2. export FLASK_ENV=development
        3. 进入flaskr目录，修改config.py文件夹，设置数据库账号密码
        4. flask init-db
3. 进入compute目录，修改config.py文件夹，设置数据库账号密码
4. 执行所有py文件（到这里数据都在数据库中了)
5. flask run 
6. 浏览器输入 127.0.0.1：5000