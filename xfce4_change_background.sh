# Changing the background on XFCE 4 DE for Linux Mint 19.1 with LightDM

# first, put the background in /usr/share/backgrounds/common

# change lightdm
sudo vim /etc/lightdm/slick-greeter.conf

# change main background
nitrogen


# update wallblur
sudo vim ~/system/wallblur/wallblur_nopywall.sh

