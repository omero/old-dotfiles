#!/bin/bash

if [[ $(hostname) == 'omers-blade' ]]; then
    ~/.screenlayout/dual-blade.sh
fi

# Set wallpaper
feh --bg-fill ~/Documents/Wallpapers/wallpaper.png &
dwmblocks &
# Reload .Xresources
xrdb -load ~/.Xresources &
picom --xrender-sync-fence &
# Dunst
dunst &
# Bluethoot
blueman-applet &
# Nm-applet
nm-applet &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#
#xrdb -merge $HOME/.Xresources &
