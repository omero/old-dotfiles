# -*- coding: utf-8 -*-
##### IMPORTS #####
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

##### DEFINING SOME VARIABLES #####
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                                    # My terminal of choice
myConfig = "/home/omers/.config/qtile/config.py"    # The Qtile config file location

##### KEYBINDINGS #####
keys = [
         ### The essentials
         Key(
             [mod], "Return",
             lazy.spawn(myTerm)                      # Open terminal
             ),
         Key(
             [mod, "shift"], "Return",              # Dmenu Run Launcher
             lazy.spawn("rofi -modi run,drun -show drun -columns 1 -width 24 -lines 8 -padding 45 -hide-scrollbar -show-icons -drun-icon-theme 'Papirus'")
             ),
         Key(
             [mod], "Tab",
             lazy.next_layout()                      # Toggle through layouts
             ),
         Key(
             [mod, "shift"], "q",
             lazy.window.kill()                      # Kill active window
             ),
         Key(
             [mod, "shift"], "r",
             lazy.restart()                          # Restart Qtile
             ),
         Key(
             [mod, "shift"], "c",
             lazy.shutdown()                         # Shutdown Qtile
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0)                       # Keyboard focus to screen(0)
             ),
         Key([mod], "e",
             lazy.to_screen(1)                       # Keyboard focus to screen(1)
             ),
         Key([mod], "r",
             lazy.to_screen(2)                       # Keyboard focus to screen(2)
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen()                      # Move monitor focus to next screen
             ),
         Key([mod], "comma",
             lazy.prev_screen()                      # Move monitor focus to prev screen
             ),
         ### Treetab controls
         Key([mod, "control"], "Up",
             lazy.layout.section_up()                # Move up a section in treetab
             ),
         Key([mod, "control"], "Down",
             lazy.layout.section_down()              # Move down a section in treetab
             ),
         ### Window controls
         Key(
             [mod], "Down",
             lazy.layout.down()                      # Switch between windows in current stack pane
             ),
         Key(
             [mod], "Up",
             lazy.layout.up()                        # Switch between windows in current stack pane
             ),
         Key(
             [mod, "shift"], "Down",
             lazy.layout.shuffle_down()              # Move windows down in current stack
             ),
         Key(
             [mod, "shift"], "Up",
             lazy.layout.shuffle_up()                # Move windows up in current stack
             ),
         Key(
             [mod], "Left",
             lazy.layout.grow(),                     # Grow size of current window (XmonadTall)
             lazy.layout.increase_nmaster(),         # Increase number in master pane (Tile)
             ),
         Key(
             [mod], "Right",
             lazy.layout.shrink(),                   # Shrink size of current window (XmonadTall)
             lazy.layout.decrease_nmaster(),         # Decrease number in master pane (Tile)
             ),
         Key(
             [mod], "n",
             lazy.layout.normalize()                 # Restore all windows to default size ratios 
             ),
         Key(
             [mod], "m",
             lazy.layout.maximize()                  # Toggle a window between minimum and maximum sizes
             ),
         Key(
             [mod, "shift"], "f",
             lazy.window.toggle_floating()           # Toggle floating
             ),
         ### Stack controls
         Key(
             [mod, "shift"], "space",
             lazy.layout.rotate(),                   # Swap panes of split stack (Stack)
             lazy.layout.flip()                      # Switch which side main pane occupies (XmonadTall)
             ),
         Key(
             [mod], "space",
             lazy.layout.next()                      # Switch window focus to other pane(s) of stack
             ),
         Key(
             [mod, "control"], "Return",
             lazy.layout.toggle_split()              # Toggle between split and unsplit sides of stack
             ),
         ### Dmenu scripts launched with ALT + CTRL + KEY
         #Key(
         #    ["mod1", "control"], "e",
         #    lazy.spawn("./.config/rofi/edit-configs.sh")
         #    ),
         ### My applications launched with SUPER + ALT + KEY
         Key(
             [mod, "mod1"], "e",
             lazy.spawn("./.config/rofi/edit-configs.sh")
             ),
         Key(
             [mod, "mod1"], "m",
             lazy.spawn("spotify")
             ),
         Key(
             [mod, "mod1"], "w",
             lazy.spawn("brave")
             ),
         Key(
             [mod, "mod1"], "s",
             lazy.spawn("deepin-screenshot")
             ),
         Key(
             [mod, "mod1"], "z",
             lazy.spawn("xrandr --output DisplayPort-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-A-0 --off --output DisplayPort-1 --off --output DisplayPort-2 --off")
             ),
         Key(
             [mod, "mod1"], "x",
             lazy.spawn("xrandr --output DisplayPort-0 --primary --mode 2560x1440 --pos 0x0 --rotate normal --output HDMI-A-0 --off --output DisplayPort-1 --off --output DisplayPort-2 --off")
             ),
         Key([], "XF86AudioNext", lazy.spawn("mpc next")),
         Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
         Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
         Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

         # general volume
         Key([], "XF86AudioRaiseVolume", lazy.spawn("/usr/bin/pulseaudio-ctl up 5")),
         Key([], "XF86AudioLowerVolume", lazy.spawn("/usr/bin/pulseaudio-ctl down 5")),
         Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),

]

##### GROUPS #####
group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("MUS", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("VID", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 15,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

##### THE LAYOUTS #####
layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         fontsize = 12,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
     layout.Floating(**layout_theme)
]

##### COLORS #####
colors = [["#37375B", "#37375B"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Overpass",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####

def init_widgets_list():
    widgets_list = [
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.GroupBox(font="Overpass Semi-Bold",
                        fontsize = 12,
                        margin_y = 1,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Prompt(
                        prompt=prompt,
                        padding=10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 40,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.WindowName(
                        foreground = colors[6],
                        background = colors[0],
                        padding = 0
                        ),
               widget.TextBox(
                        text='',
                        background = colors[0],
                        foreground = colors[4],
                        padding=0,
                        fontsize=25
                        ),
               widget.TextBox(
                        text=" ",
                        padding = 2,
                        foreground=colors[2],
                        background=colors[4],
                        fontsize=20
                        ),
               widget.Pomodoro(
                        foreground=colors[2],
                        background=colors[4],
                        color_inactive=colors[2],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=25
                        ),
               widget.TextBox(
                        text=" 🌡",
                        padding = 2,
                        foreground=colors[2],
                        background=colors[5],
                        fontsize=11
                        ),
               widget.ThermalSensor(
                        foreground=colors[2],
                        background=colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=25
                        ),
               widget.TextBox(
                        text=" ⟳",
                        padding = 2,
                        foreground=colors[2],
                        background=colors[4],
                        fontsize=14
                        ),
               widget.Pacman(
                        execute = "pamac-manager",
                        update_interval = 1800,
                        foreground = colors[2],
                        background = colors[4]
                        ),
               widget.TextBox(
                        text="Updates",
                        padding = 5,
                        foreground=colors[2],
                        background=colors[4]
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=25
                        ),
               widget.TextBox(
                        text=" 🖬",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Memory(
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=25
                        ),
               widget.CPU(
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=25
                        ),
               widget.TextBox(
                       text=" Vol:",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 0
                        ),
               widget.Volume(
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5 
                        ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=25
                        ),
               widget.CurrentLayoutIcon(
                        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                        foreground = colors[0],
                        background = colors[4],
                        padding = 0,
                        scale=0.7
                        ),
               widget.CurrentLayout(
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=25
                        ),
               widget.Clock(
                        foreground = colors[2],
                        background = colors[5],
                        format="%A, %B %d - [ %H:%M ]"
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[0],
                        background = colors[5]
                        ),
               widget.Systray(
                        background=colors[0],
                        padding = 5
                        ),
              ]
    return widgets_list

##### SCREENS ##### (TRIPLE MONITOR SETUP)

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=25)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.95, size=25)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=25))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
