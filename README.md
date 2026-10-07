# Garfield Wallpaper (Linux Mint)

This repository contains a simple project which allows you to update you wallpaper whenever you startup your computer. 

Not too long ago I made my change from Windows to Linux Mint and decided that some small customization would allow me to touch some parts of the system, if at least superficially. 

Hopefully I can allow myself to enter soon into more ricing options and I'll post them here. 



## Contents
This is the file structure of the project:
```
.
├── code
│   ├── builder.py
│   ├── grabber.py
│   └── main.py
├── imgs
│   ├── GarfBckgroundClear.png
│   └── GarfBackgroundDark.png
├── garfieldWallpaper.sh
└── README.md <-- (you are here)
```

### Code
Within code we have two main scripts that will do the workload and 

**builder:** This file makes use of the daily comic and the background and joins them to display the image

**grabber:** Extracts the daily comic by visiting the Garfield comic website and extracting the url of the daily image. 



### Imgs
This folders contains two backgrounds for the wallpaper, one in light mode and another for dark mode. If your instalation includes <code> org.cinnamon.desktop.background picture-uri-dark </code> you may add to <code> garfieldWallpaper.sh</code> that option to easily change between the modes. However this will require building both versions.  

Appart from that, this folder will hold the daily comic and the current wallpapers for their use. 

## Use
To use this project, simply downloaded and set the bash as a custom command in your startup applications menu, ensure that there is some delay to properly load your computer.

I have decided not to use either cron or anacron since they may get skipped while the computer is not working or not update when the computer is opened.

Please note that since the program is fetching information from the web, if we do not have network connection when at startup the task will fail. 

## FAQ
**Why?**
I just really like Garfield, alot.

**Can I use it with different versions of Linux?**
You can use this project in different versions of Linux or even Windows if it supports Python, Bash, has a command to update the desktop background from terminal and can schedule jobs at startup.
