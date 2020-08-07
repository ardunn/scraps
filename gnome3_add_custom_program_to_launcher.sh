
# Adding a custom command to gnome launcher
# You need to place a `.desktop` file in one of the following locations

~/.local/share/applications
/usr/share/applications

# The file should look somewhat like this:
[Desktop Entry]
Name=Obsidian
Exec=/home/dude/system/Obsidian-0.8.1.AppImage
StartupNotify=true
Terminal=false
Type=Application
Icon=/home/dude/system/obsidian.png

# The Exec field is the most important part. Is just needs to be a command (e.g., a .sh file, MIME executable), not necessarily an AppImage.

