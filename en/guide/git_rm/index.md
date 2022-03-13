# How to Delete a Git File or Folder While Keeping the Local Ones


### 一、Delete a file

To remove a file from Git version control while keeping the local file.

1. Add the file to .gitignore.
2. Execute in command line:

​		```
​	git rm file_path --cached
​	```

3. 进行commit，将文件从版本库中删掉：

​		```
​	git commit -m "delete the file"
​	```

### 二、Delete a folder

To remove a folder from Git version control while retaining the local folder, add the `-r` argument:

​		```git rm -r folder_path --cached```

To remove all files in .gitignore from version control, you need to remove all files first, and then do the following to add all files.

​		```git rm -r . --cached```

​		```git add .```

This way, files in gitignore will be ignored.


