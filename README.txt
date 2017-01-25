	Git command code

创建库：
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