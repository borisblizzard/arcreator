   #-----------------------------------#
   |      How to setup ARC editor      |
   |      By: Soulshaker3              |
   |      Edited By: KK20              |
   #-----------------------------------#

   This README was designed for Windows users who may have trouble getting Welder, ARC's editor, set up properly. While a .bat and .sh file within the project are supposed to download these dependencies for you, it did not work entirely for us. We recorded this process to be a reference for anyone else who may happen to have the same issues as we did. Note that this was done on Windows 7.

   To setup Welder there's a few steps you should follow:
      1) Download ARC from Github
      2) Download and install Visual Studio C++
      3) Download and install Python and all its dependencies

   #------------------------------#
   |      1) Downloading ARC      |
   #------------------------------#

   To download ARC it's actually pretty straight forward. Just go to ARC's Github repository ( https://github.com/borisblizzard/arcreator) and, on the bottom of the page, you'll see a button saying "Download ZIP". 
   
   Example here: http://i.imgur.com/vC6fGic.png
   
   Click on it, wait for the download to finish and extract the folder to somewhere you'd like. For this step, that's all you need to do. Let's proceed to downloading and installing Visual Studio C++.

   #----------------------------------------------------------#
   |      2) Downloading and Installing Visual Studio C++     |
   #----------------------------------------------------------#
   
   For those of you wondering, you won't actually have to use this program, but there's no pre-compiled version of Cython and you'll need it when building the whole thing.

   So go to this link: https://go.microsoft.com/?linkid=9709949&clcid=0x409&wt.mc_id=o~msft~vscom~download-body~dn469506&campaign=o~msft~vscom~download-body~dn469506

   Create/Use your existing live account and login to Microsoft's Website. They will ask you some info before you download it, just fill your name and country and proceed with the download.

   Example here: http://i.imgur.com/iFF8bZp.png

   If it goes to your account page without downloading just click open the link again and click the same button; this time it won't ask you for information.

   After downloading, just install it like any normal program and that's it for this point. Now to the tricky one.

   #----------------------------------------------------#
   |      3) Intalling Python and its dependencies      |
   #----------------------------------------------------#

   The first thing obviously is to install python. Because Welder uses a specified version of python (3.4), any other version isn't recommended to use as it might cause imcompatibility.
   
   So go to Python's download page ( https://www.python.org/downloads/release/python-340/ ) and download according to your to your OS. Get the 32-bit version, NOT the 64-bit (that's important).
   
   After downloading it, install it, making sure to enable the option to prepend Python to the system Path variable.

   Image Reference: http://puu.sh/iUDwl/01b8cedc45.png

   After that, check if Python's folder and Python's Script folder are pointed in your 'Path' system variable.
   
   To do that go to "My Computer", then right click "Properties"(1) , click "Advanced system options"(2) and then in "Environment variables"(3).
   
   Example here (excuse the non-english): http://i.imgur.com/QoQ0weq.png
   
   Then in "System Variables" look for one called "Path" and check, at the end of it, if it has your Python path and Python's Scripts Path. For example mine is C:\Python34\ so in the end of the file it should appear "C:\Python34\;C:\Python34\Scripts\".
   
   After that open your Command Line in administrator mode and type "python" to ensure you got that right. If it tells you your Python Version and some data about it, you're good to go. Type "exit()" to go back,
   
   Finally we just have to install all the dependencies of ARC. To do that it's pretty simple--we just have to run a command "pip install xxx", where xxx is the add-on we want to install.
   
   So type these (or copy-paste) in your command line in order:
          pip install setuptools
	  pip install cython
	  pip install pyitect
          pip install numpy
	  pip install pillow
	  pip install pyglet
	  pip install https://github.com/Ryex/Rabbyt/archive/0.8.3-3-cythonpy3.zip
	  pip install http://wxpython.org/Phoenix/snapshot-builds/wxPython_Phoenix-3.0.3.dev1820+49a8884-cp34-none-win32.whl
	  pip install pywin32
	  
   After this, if you haven't encountered any errors, you should be good to go. To check, you can run
          pip list
   to see if all your add-ons have successfully installed.

   One such example looks like this: http://puu.sh/iVDXJ/207b830ef8.png

   To test if everything's working, go to your ARC folder > editor > welder > Editor and run 
          python main.py
   
   If the welder doesn't throw any error and looks like this ( http://i.imgur.com/qncUs2M.png ) you're good to go. Congrats you've sucessfully setup Welder.