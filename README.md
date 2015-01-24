# Twitter-clone

K_twitter_app will enable users to login to their accounts and do some basic Twitter like operations,

Functionalities of this App are:

1.signUp

2.sign-in

3.View a basic timeline

4.compose and post a tweet(100 charecter)

5.View the Profiles of other users

6.Shows all the tweets

7.Followers

8.Following

9.Time ,tweet posted

Step of installing SetUp in Ubuntu

step 1:python is already there in ubuntu.You have to install pip

sudo apt-get install python-pip

pip install -U pip

Step 2: Install Django 
sudo apt-get install python-django

now in terminal follow the path of project and run using command 

"python manage.py runserver"

In any browser run project with "http:\\127.0.0.1:8000"



Step of installing SetUp in Windows(7,8, or XP)

Step 1:Download python
https://www.python.org/downloads/
       
Description:This will install "pip" also. 
You can see it here "C:\Python27\Scripts"
Or if needed ,save script get-pip.py(https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py) 
and run with command "C:\> python get-pip.py" in cmd

Step 2:Add Path to "system"
Go to system properties(either by control panal or  right click on my computer icon on Desktop)
choose "Advance"
choose "Path" then edit
Add "C:\Python27;" and "C:\Python27\Scripts" (in python is python 2.7)
logoff you computer and start again
       
  Step 3:Install virtualenv and virtualenvwrapper
  C:\> pip install virtualenv
  C:\> pip install virtualenvwrapper-powershell
         

  Step 4:Download Django package
  "https://github.com/django/django/zipball/master" download zipped and extract it
  Here you'll find setup.py
  Follow the path of setup.py and run using cmd " C:\>python setup.py install" this'll install Django


now in cmd follow the path of project and run using command 

"python manage.py runserver"

in any browser run project with "http:\\127.0.0.1:8000"

