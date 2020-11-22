# NotionHook

**A YOUTUBE EXPLANATION VIDEO WILL COME SOON!**

These scripts uses [notion-py](https://github.com/jamalex/notion-py).

With these files you can save in notion a backup of your commit messages, url and time.

* Move the files in .git/hooks folder inside your project folder, or the one you configured by `git config --global core.hooksPath`.
* open the terminal, navigate in the folder and execute python3 ./setHooks.py
* paste your token and the url of the database view.
* Now every commit will be saved into your database view:
<img width="1125" alt="image" src="https://user-images.githubusercontent.com/3796324/99914556-6ef81700-2cfe-11eb-8307-ef67ef93a645.png">
**Please use the exact same column names!**
