# In GNOMe, changing scroll speed of a mouse is not supported through the gui

# From https://askubuntu.com/questions/255890/how-can-i-adjust-the-mouse-scroll-speed

# Find the correct peripheral to edit, the ID will be an integer
xinput list

# List parameters from peripheral (example id=12)
xinput list-props 12

# Change the scroll speed parameter (this is using an MX Master 3)
xinput set-prop 12 'libinput Scrolling Pixel Distance' 30

# You can also put this in .profile to apply it automatically
# Note the parameter name must appear exactly as it appears in the list-props command
