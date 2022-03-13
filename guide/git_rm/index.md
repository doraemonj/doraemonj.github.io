# 如何删除Git文件、而保留本地文件


### 一、删除文件

把一个文件从Git版本控制中删除，同时保留本地文件：
1. 将该文件加入.gitignore中；
2. 命令行执行：

	​	```
	​	git rm file_path --cached
	​	```
3. 进行commit，将文件从版本库中删掉：

	​	```
	​	git commit -m "delete the file"
	​	```

### 二、删除文件夹

把一个文件夹从Git版本控制中删除，同时保留本地的文件夹，需加 `-r` 参数：

```git rm -r folder_path --cached```

把所有.gitignore中的文件从版本控制中删除，需先移除所有文件，再执行添加所有文件：

```git rm -r . --cached```

```git add .```

这样，gitignore中的文件会被忽略。

