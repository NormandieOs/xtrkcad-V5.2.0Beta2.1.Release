# Release Notes

Welcome to the XtrackCAD V5.2.0 Beta 2.1 release! 

Beta 2.1 has very few functional enhancements and quite a lot of bug fixes since Beta 2.0. 

The V5.2 release started out as just some simple functional enhancements of long-standing, like background images. The idea was to punt on all UI changes to the V6 GTK3 release.  But along the way and due to some sabaticals for developers, things kept getting added and tinkered with. Finally the major UI enhancements you will see were mapped out over the last six months and so we have an incremental enhacement to the UI as well.

Enjoy!

Martin and Dave and Adam, your volunteer developers.

PS The full change log is a file in the XtrkCAD download folder as CHANGELOG.md 

## Warning to Users

Please note - this software DOES contain bugs. Do not use it if that fact will bother you. All software contains bugs, of course, but beta software is our chance to find and remove as many of them as possible before unleashing it for all users. You, our beta test partners in this endeavor, are helping by exposing yourself to the risk of failure and then letting us know how it went. This is vital, you need to let us know when things are not happening as you would expect, or if they are (so we know someone is testing).

Take backups! Please. The files written by XTrackCAD 5.2.0 are versioned to only be read by 5.2.0, but it can also read files from earlier versions. If you get into trouble, please reach out, we may be able to help - but not if you didn't back-up.

We will fix important bugs you find by issuing perodic Beta updates. We may not change the code if what you would expect is impossible or would break what we are trying to achieve overall, but we promise that we will consider all your input as carefully as we can. Obviously if the program fails in some way, let us know. But also let us know when you can't work things out, or the way things seem to work seems irrational.  Exercise the Documentation as well (read the Help manual when you get stuck - there's a handy F1 shortcut to the pages for the current function now...)

To report bugs, please use the SourceForge bugs reporting page https://sourceforge.net/p/xtrkcad-fork/bugs/

To discuss the Beta, please use the user forum https://xtrackcad.groups.io/g/main/topics

# Notes on V5.2 UI Philosphy 

XtrackCAD is a veteran product. Conceived in a world of UNIX Vector Graphic UIs, and then ported to Windows as well, the way it worked was optimized for a hardware era where full redrawing the screen was a painful operation. Moving objects around required simplification for drawing and a overwrite approach. The chic UI style at the time was very modal - you picked a tool from a toolbar and then used it by selecting a target - Think Photoshop. Each command/tool was a world unto itself with different rules to master. Learning the program required a lot of practice, but rewarded you with lots of short-cuts and functions that required a sequence of actions. 

Now we are in 2020, our hardware is much more powerful even if we have a machine a few years old. We are used to more responsive and immersive UIs that try to anticipate the user and guide them. Many UIs have a more "pick an object and then take various actions" style. Partly out of necessity XTrackCAD will look familar to its loyal users and largely work the same way for them, but a major focus for the UI improvements has been to try and bridge the semantic gap towards commonly used consumer programs of today to smooth the on-ramp experience. Predictability is key - can I understand what will happen before doing it, and so learn by exploring? Am I able to navigate between common functions more easily, and do objects I see behave in ways that I might expect?

We combed through the user suggestions, thought back to our own first experiences, did surveys of other graphical design products and asked users directly about choices we could make. We also looked at all the feedback we could find online (good or bad) from railway/railroad modellers. This led us to understand that new users thought of XTrackCAD like a set of tracks waiting to be assembled and they were confused by simple things - *why do I have to select turnouts differently from flexible track*?  *Why is the program so fussy about how track lines up - shouldn't it just join*? *Why do some of my commands affect objects I can't even see on screen*? Meanwhile power users had other concerns. *Why can't I draw objects which are accurate like in a "real" CAD*? *Why can't I use Cornu for more than joining*? *Why are the parameter files so hard to pick between*?

There are several things we did not do in the UI because they would have been too complex on a divided Windows/GTK GUI base - those will have to wait for V6. But overall we hope that new users will find V5.2 more accessible, while power users will discover enhanced features that they can use (even ones that have always existed but were well hidden).

Our criteria then is this -> to have to use fewer clicks to get common tasks done, to make those remaining actions more accurate and with fewer side-effects. We want to support easy "snap it together" tracklaying as well as high-precision drawing creation. To allow for better annotation and tracing of real locations, to encourage more production of reusable parts by making finding them easier. Although a modern "look" will await the customization of V6, we wanted to do the best we can with the "classic" UI framework we have inherited standing on the shoulders of the giants who preceeded us.

Adam R

PS If you can't "track" with the new Select method, you can get back "Classic" Select with -

- Options->Command->Select Add and uncheck Select None
- Toggle Magnetic Snap Off

# Install Notes

## Mac OSX

Mac OSX installs an app package which you drag into the Applications folder.  In order to run it, you need to have installed XQuartz from http://www.xquartz.org first. Please remember to log on and off after installing XQuartz for the first time.

On Mojave and earlier, the program may not work on first run after trying to run it - Go to Preferences->Security and Select "Run Anyway". 

On Catalina, XTrackCAD will not work by double-clicking the app - You have to right-select it in Finder inside the Applications folder and select "Open". The app loses access to certain high-risk/high-security folders including Downloads, Documents and Music folders - if you have material you need to use in those areas, copy them into other folders.

## Windows

XTrackCAD v5.2 is a 32 bit application. To suport new features the package comes with three DLLs. Two of them (zlib and zip) require vcruntime140.dll, which is not included in the package. So you'll have to get a 32bit version of that DLL and install it in your path.

Try https://www.microsoft.com/en-US/download/details.aspx?id=48145

## Linux

Installing the Debian package (xtrkcad-setup-5.2.0Beta2.0-1.x86_64.deb) or the RPM package (xtrkcad-setup-5.2.0Beta2.0-1.x86_64.rpm) will install in /usr/local/bin/ and /usr/local/share/.
Super-user access will be required to install this.
Be aware that you don't invoke any other existing *xtrkcad* installation when running the program.

The debian package is new (and experimental).

Installing the shell archive xtrkcad-setup-5.2.0Beta2.0-1.x86_64.sh will install in the current directory.  You will be given the choice of whether to install the bin/ and share/ directories in the current directory or in a subdirectory (xtrkcad-setup-5.2.0Beta2.0-1.x86_64/).
You must set the environment variable XTRKCADLIB to the location of the share/xtrkcad directory:<br>
``export XTRKCADLIB=`pwd`/share/xtrkcad or

``export XTRKCADLIB=`pwd`/xtrkcad-setup-5.2.0Beta2.0-1.x86_64/share/xtrkcad

To run *xtrkcad* you will need to run it from a terminal window.  For the shell archive, the installed bin/ directory must be in your path or the path to the bin/ directory must be specified.
We're working on integrating *xtrkcad* with the menu system.

*webkitgtk* is not used for displaying help.  Instead your system browser will be used.

The dependency of libzip-dev may be required if you are not installing from a package designed for the Linux variant 

### Update Aug 4th, 2020

I've added the capability to integrate XTrkCad with the Ubuntu/Debian sytems
Now, double clicking on a .xtc file in the file browser will launch xtrkcad.
And the XTrkCad file icon will appear for .xtc files in the file browser.
Also, XTrkCad appears on the system menu under Graphics.
You can also add XTrkCad shortcut on your desktop.

Caveat: I have seen bug #350 (Hang on calling wFlush from wSetSplashInfo) fairly often.
If this bites you, you will have to kill xtrkcad and try again.
Please post your system configuration as a comment to bug #350.

This has been tested on Ubuntu (16.04) (I'll update soon)
I don't know if this works on RPM systems.  Volunteers?

You will need to install xdg-util and its dependencies.

Steps:<br>
1. download xtrkcad.xml and xtrkcad.desktop to /usr/local/share/xtrkcad/applications/

2. run the following commands<br>
        INSTALLDIR=/usr/local/share/xtrkcad<br>
        xdg-mime install --novendor ${INSTALLDIR}/applications/xtrkcad.xml<br>
        xdg-mime default ${INSTALLDIR}/applications/xtrkcad.desktop application/x-xtrkcad<br>
        xdg-desktop-menu install --novendor ${INSTALLDIR}/applications/xtrkcad.desktop<br>
        xdg-icon-resource install --context mimetypes --novendor --size 64 ${INSTALLDIR}/pixmaps/xtrkcad.png application-x-xtrkcad<br>


3. if you want a icon on your desktop also do<br>
         xdg-icon-resource install --novendor --size 64 ${INSTALLDIR}/pixmaps/xtrkcad.png xtrkcad<br>
         xdg-desktop-icon install --novendor ${INSTALLDIR}/applications/xtrkcad.desktop<br>

Good luck

