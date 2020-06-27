这是hazewu的分支


1、首次连接
git init //初始化仓库
git add .(文件name) //添加文件到本地仓库
git commit -m “first commit” //添加文件描述信息
git remote add origin + 远程仓库地址 //链接远程仓库，创建主分支
git pull origin master // 把本地仓库的变化连接到远程仓库主分支
git push -u origin master //把本地仓库的文件推送到远程仓库

如果不行
git push -f origin master	//强制推送

2、git如何新建分支 

git checkout master	//切换到基础分支，如主干
git checkout -b panda	//创建并切换到新分支

git add filename	//更新分支代码并提交
git commit -m "init panda"
git push origin panda

3、删除某分支的某文件
git pull origin master   //把github上的master上的文件重新拉下来
git rm -r --cached xxx	//删除某文件
git commit -m "备注：delete xxx"		//提交
git push -u origin master	//更新远程Github仓库的master

4、更新某分支的某文件
git checkout wzz	//切换到该分支
git add filename
git commit -m "备注"	//会根据filename，更新具有相同名字的文件
git push origin wzz	

5、如何把master的内容更新到分支
git checkout master	//切换到master
git pull origin	master	//把master中的内容拉到本地
git checkout wzz	//切换到分支下
git merge master	//合并master到分支
git status		//检查一下
git push origin wzz	//push到远程分支