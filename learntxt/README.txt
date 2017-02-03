	Git command code

# ------------------------------------------------------
iconv -f gb18030 -t utf-8 README.txt -o README.txt # 用utf-8读取windo的txt文件。

# ------------------------------------------------------
创建配置与库：
git config --global user.name "rootpip"
git config --global user.email "306127031@qq.com"
# git config命令的--global参数，用了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。
git init /path/(optional) # 命令一个目录变成Git可以管理的仓库

# ------------------------------------------------------
代码提交：
git add file # 把文件添加到仓库
git commit -m "...(file or modified description)" # 把文件提交到仓库

$ git add file1.txt
$ git add file2.txt file3.txt
$ git commit -m "add 3 files."

# ------------------------------------------------------
查询库：
git status # 命令可以让我们时刻掌握仓库当前的状态
git diff # 查看difference，显示的格式正是Unix通用的diff格式

# ------------------------------------------------------
版本回退：
git log # 命令显示从最近到最远的提交日志
git log --pretty=oneline # 提交日志友好显示模式
HEAD HEAD^ HEAD^^ HEAD~100 # 分别表示 当前版本 上一个版本 上上个版本 往上100个版本
git reset --hard HEAD^ # 回到上一个版本
git reset --hard commit_id # 回到commit_id版本，版本号不必写全
git reflog # 用来记录你的每一次命令

# ------------------------------------------------------
撤销修改：
git checkout -- file
"""命令git checkout -- readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情况：一种是readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；一种是readme.txt已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。总之，就是让这个文件回到最近一次git commit或git add时的状态。"""
git reset HEAD file # 可以把暂存区的修改撤销掉（unstage），重新放回工作区

# ------------------------------------------------------
删除：
git rm file # 用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失最近一次提交后你修改的内容。


