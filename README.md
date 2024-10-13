# mutify
Music Player ad muting app for Linux. This requires playerctl and python3. Needless to say it also unmutes Ads when they are over. It also has Player controls and song title visibility along with ads muted. Make sure all the files are in one folder and addressed correctly where they are located in main.py. Now place .desktop file where all other application files are located.

desktop files, are generally a combination of meta information resources and a shortcut of an application. These files usually reside in /usr/share/applications/ or /usr/local/share/applications/ for applications installed system-wide, or ~/. local/share/applications/ for user-specific applications.

you may logout and login back if you don't see the application icon on UI. if that doesn't work restart the system. last option directly run main.py using your python compiler.

Make sure that you have all the python modules installed which are listed in main.py. If not then you can install them by running $pip install <module_name> in terminal. If Ad doesn't mute then check for the song title when Ad is being played and then replace the same with "Advertisement" in source_linux.sh. If you are using spotify then likely don't need to do anything because I have tested this on Spotify. If any problem regarding ad_count arises then it must be because export_omega.sh and main.py aren't running in same linux instances.

I would be glad to have feedbacks and errors (if any occurs) from you.
