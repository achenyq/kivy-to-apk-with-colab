# kivy-to-apk-with-colab
<h3 align="center">This repository contains a tool that converts python written code with the <strong>kivy framework</strong> into an application utilizing Google Colab and Buildozer </h3>
<a href="https://colab.research.google.com/drive/1UmusJDXGtswvM5Bu9ikf6b_rYGklP4Hn?usp=sharing\" target=\"_parent\"><img src="https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Colab\"/></a>

---

### Overview
- [Overview](#overview)
- [Built With](#Built-With)
- [How to use](#How-to-us)
- [Features](#features)
- [Reformat and check](#reformat-and-check)
- [Bugs or Opinion](#bugs-or-opinion)

### Built With
<p> This section is the list of languages used in this project.</p>
<p align="center" >
  <img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="sqlite"  margin="20px" width="70" height="70"/>
</p>

### How to use
- To set up this tool, you just need to enter Google Colab and execute the commands step by step.The First step is to open the Google colab. Then import your python file and see to that you rename your file name(both python and .kv file)to “main.py and main.kv”.And also see to that you import all the necessary files such as images and .kv file.
- Execute all commands until you reach the ‘!buildozer init’ command to creating “buildozer.spec” file to set the setting of project if you dont know how to complete this file there's a sample in <a href="https://github.com/Novin1380/kivy-to-app-with-colab/blob/main/buildozer.spec">here!</a>
```bash
!buildozer init
```
- In the next step you should run “!buildozer -v android debug” command to starting build, immediately after the execution, we will get an question like “Are you sure you want to continue [y/n]?”.click yes.And after some time you will again get an question.Click yes and finally one more question and click yes for that too. Then wait until the proccess finish( it take you about 15-20 minutes )
```bash
!buildozer -v android debug
```
**_Notice:_** If you encounter an error at this stage, execute the ‘!buildozer android clean’ command
```bash
!buildozer android clean
```
**_Notice:_** If you still encounter an error, the problem may be with the ‘buildozer.spec’ file. Check the “buildozer.spec/requirements in line 40” ,“log” and the ‘buildozer.spec’ file, correct any mistakes, execute the ‘!buildozer android clean’ command and try again.
- Now After completing proccess, we can see the our APK file in the Bin Folder. Right click on it and download it! Once downloaded completely that’s it
- After all step you can use this command to clean buildozer log and restart it for another proccess
```bash
!buildozer android clean
```  

### features
- [x] _This file is currently the most up-to-date for converting Kivy to APK using Google Colab and Buildozer, and it has been fully tested and works effectively._ at **Date:4/5/2024**


### Reformat and check
💡Its important that you should have google accounts to test it.

### Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo or google colab

---

**_Notice:_** _If you are using this file please don't change it and let other peaples enjoy it_

<h6 align="center">be kind with each other and share your problems solution to makes better world!</h6>
<h5 align="center">just enjoy! 👋</h5>
