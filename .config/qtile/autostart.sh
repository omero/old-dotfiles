#! /bin/bash 
feh --bg-fill ~/Pictures/Wallpapers/escape_velocity.jpg &
# Reload .Xresources
xrdb -load ~/.Xresources &
# ------- Autostart apps ------
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# Picom
picom &
# Dunst
dunst &
# Clipman
xfce4-clipman &
# Bluethoot
blueman-applet &
# Nm-applet
nm-applet &

pasystray &

setxkbmap -layout us,es -option grp:alt_shift_toggle &
# # ------- Mouse/Touchpad fixes ------
# # Start libinput gestures
# libinput-gestures-setup start
# # Xinput configs (touchpad)
# xinput set-prop "DLL07BE:01 06CB:7A13 Touchpad" "libinput Natural Scrolling Enabled" 1
# xinput set-prop "DLL07BE:01 06CB:7A13 Touchpad" "libinput Click Method Enabled" 0 1
# xinput set-prop "DLL07BE:01 06CB:7A13 Touchpad" "libinput Disable While Typing Enabled" 0
# # ------- Keyboard fixes ------
# # Remap Caps-lock key to Escape, for using VIM
# setxkbmap -option caps:escape
# # Make US and DK keyboard layout togglable with Shift+Alt
# setxkbmap -layout us,es -option grp:alt_shift_toggle

