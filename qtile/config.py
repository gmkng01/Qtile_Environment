# ********************************                          IMPORTS                                ********************************
import os
import subprocess
from libqtile import hook
from libqtile import qtile
from colors import gruvbox, nord_fox, gruvbox2
from libqtile.lazy import lazy
from libqtile.core.manager import Qtile
from libqtile import bar, layout, widget
from libqtile.backend.base import Window
from libqtile.config import Click, Drag, Group, Key, Match, Screen
# import iwlib  # type: ignore
# import psutil  # type: ignore
# from spotify import Spotify
# from libqtile.utils import send_notification
# from datetime import datetime
# from typing import TYPE_CHECKING
# from libqtile.log_utils import logger


mod = "mod4"
mod1 = "mod1"
trml = "terminator"
browser = 'firefox'
# MUSIC_CTRL = "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player."

# Additional Functions -------------***********-----------

# Brightness Up 
def brightup():
  qtile.cmd_spawn('brightnessctl set +1%')
  

# Brightness Down
def brightdown():
  qtile.cmd_spawn('brightnessctl set 1%-')

# Menu
def menu():
  qtile.cmd_spawn('/home/abhi/.config/rofi/launchers/type-1/launcher.sh')

# ********************************-------------------------------Key_bidings-------------------------------********************************
keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(trml),
             desc='Launches My Terminal'
             ),
         Key([mod1, "shift"], "c",
             lazy.spawn("google-chrome-stable"),
             desc='Launches My Chrome'
             ),
         Key([mod1], "s",
             lazy.spawn("spotify"),
             desc='Launches My Spotify'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn("/home/abhi/.config/rofi/launchers/type-1/launcher.sh"),
             desc='Run Launcher'
             ),
         Key([mod, "shift"], "x",
             lazy.spawn("shutdown -P now"),
             desc='Shut Down'
             ),
         Key([mod, "shift"], "r",
             lazy.spawn("reboot"),
             desc='Reboot'
             ),
         Key([mod1], "f",
             lazy.spawn("firefox"),
             desc='Firefox'
             ),
         Key([mod1], "d",
             lazy.spawn("discord"),
             desc='Discord'
             ),
         Key([mod1], "t",
             lazy.spawn("telegram-desktop"),
             desc='Telegram'
             ),
         Key([mod1], "c",
             lazy.spawn("code"),
             desc='VS Code'
             ),
         Key([mod1], "n",
             lazy.spawn("pcmanfm"),
             desc='File Manager'
             ),         
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod1], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),

         ### Window controls           
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),

         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod1], "Tab",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc ='Toggle between split and unsplit sides of stack'
             ),
         
         # Sound
         Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
         Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
         Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),
         
         # Brightness
         Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +5%')),
         Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 5%-')),
        
         # ScreenShots
         Key([], "Print", lazy.spawn("scrot -q 100 -e 'mv $f /home/abhi/Pictures'")),
         Key(["control"], "Print", lazy.spawn('xfce4-screenshooter')),
         Key(["control", "shift"], "Print", lazy.spawn("scrot -q 100 -s -e 'mv $f /home/abhi/Pictures'"))
]

# Drag floating layouts.
my_mouse = [Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
            Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
            Click([mod], "Button2", lazy.window.bring_to_front())]


# Grouping I created -*-

groups = [
    Group('1', label=" ", matches = [Match(wm_class = "firefox")], layout='bsp'),
    Group('2', label=" ", matches = [Match(wm_class = "Code")], layout='max'),
    Group('3', label=" ", layout='bsp'),
    Group('4', label=" ", matches = [Match(wm_class = "pcmanfm")], layout='bsp'),
    Group('5', label=" ", matches = [Match(wm_class = "discord"), Match(wm_class="TelegramDesktop")], layout='bsp'),
    Group('6', label="", matches = [Match(wm_class = "vysor")], layout='bsp'),
    ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 0,
                "margin": [15,15,15,15],
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
    # layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(**layout_theme),
    # layout.TreeTab(
    #      font = "Ubuntu",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
    #      section_fontsize = 10,
    #      border_width = 2,
    #      bg_color = "1c1f24",
    #      active_bg = "c678dd",
    #      active_fg = "000000",
    #      inactive_bg = "a9a1e1",
    #      inactive_fg = "1c1f24",
    #      padding_left = 0,
    #      padding_x = 0,
    #      padding_y = 5,
    #      section_top = 10,
    #      section_bottom = 20,
    #      level_shift = 8,
    #      vspace = 3,
    #      panel_width = 200
    #      ),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=15,
    padding=0,
)
extension_defaults = widget_defaults.copy()


# ********************************                          BAR                               ********************************
screens = [ 
    Screen(top=bar.Bar
           (
                    [
                    widget.TextBox(
                        text='',
                        background = gruvbox['fg0'],
                        foreground = gruvbox['white'],
                        fontsize = 33,
                        mouse_callbacks = {'Button1': menu,},
                        padding = 4,
                        ),
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['white'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),
                    
                    widget.GroupBox(
                            active=gruvbox['my_yellow'],
                            inactive=gruvbox2['dark-gray'],
                            highlight_method='line',
                            block_highlight_text_color=gruvbox2['dark-red'],
                            borderwidth=0,
                            highlight_color=gruvbox['white'],
                            background=gruvbox['white'],
                            fontsize = 25,
                            margin_y = 1,
                            margin_x = 1,
                            padding_y = 0,
                            padding_x = 3,
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg0'],
                            foreground = gruvbox['white'],
                            padding = 0,
                            fontsize = 30
                    ),

                    # widget.TextBox(
                    #         text = '',
                    #         font = "JetBrainsMono Nerd Font Mono",
                    #         # background = gruvbox['fg1'],
                    #         foreground = gruvbox['fg'],
                    #         padding = 0,
                    #         fontsize = 25
                    # ),

                    # widget.Backlight(
                    #             # background = colors[0],
                    #             # foreground = colors[2],
                    #             backlight_name = 'intel_backlight',
                    #             brightness_file = 'brightness',
                    #             fontsize = 11
                    # ),

                    # widget.Mpris2(
                    #         # format = "{xesam:title} - ({xesam:artist})",
                    #         format = "{xesam:title}",
                    #         playing_text = " 契 {track}",
                    #         paused_text  = "  {track}",
                    #         width = 400,
                    #         scroll_delay = 5,
                    #         scroll_interval = 0.25,
                    #         scroll_step = 15,
                            
                    #     ),

                    # Spotify(
                    #     mouse_callbacks={
                    #         "Button1": lazy.spawn(f"{MUSIC_CTRL}PlayPause"),
                    #         "Button3": spawn_or_focus("spotify"),
                    #     } ),
                    
                    # widget.Spacer(),

                    # widget.TextBox(
                    #         text = '',
                    #         font = "JetBrainsMono Nerd Font Mono",
                    #         # background = gruvbox['fg1'],
                    #         foreground = gruvbox['fg'],
                    #         padding = 0,
                    #         fontsize = 25
                    # ),

                    # widget.TextBox(
                    #         text = '',
                    #         font = "JetBrainsMono Nerd Font Mono",
                    #         # background = gruvbox['fg1'],
                    #         foreground = gruvbox['fg0'],
                    #         padding = 0,
                    #         fontsize = 30
                    # ),

                    widget.CurrentLayout(
                            background=gruvbox['fg0'],
                            foreground=gruvbox['fg9']
                    ),

                    widget.WindowCount(
                            text_format=' {num}',
                            background=gruvbox['fg0'],
                            foreground=gruvbox['fg9'],
                            show_zero=True,
                    ),
                    
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30,
                    ),
                        
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                        #     background = gruvbox['fg1'],
                            foreground = gruvbox['fg'],
                            padding = 0,
                            fontsize = 25
                    ),

                    widget.Spacer(),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                        #     background = gruvbox['fg1'],
                            foreground = gruvbox['fg'],
                            padding = 0,
                            fontsize = 25
                    ),

                    widget.TextBox(
                        text='',
                        # background = gruvbox['fg1'], 
                        # foreground = colors[2],
                        fontsize = 12,
                        mouse_callbacks = {'Button1': brightup, 'Button3': brightdown},
                        padding = 0
                        ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['white'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.CPU(
                            format=' {freq_current}GHz {load_percent}%',
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(trml + ' -e bashtop')},
                            background=gruvbox['white'],
                            foreground=gruvbox['fg0']
                            ),
                    
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['white'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.Memory(
                            format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(trml + ' -e bashtop')},
                            background=gruvbox['fg0'],
                            foreground=gruvbox['yellow']
                            ),
                    
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg0'],
                            foreground = gruvbox['white'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.Net(
                            format = ' {down} ↓↑{up}',
                            background=gruvbox['white'],
                            foreground=gruvbox2['dark-gray']
                    ), 
               
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['white'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.Volume(
                            background=gruvbox['fg0'],
                            foreground=gruvbox['dark-magenta'],
                            fmt = ' {}',
                            mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg0'],
                            foreground = gruvbox['white'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.Clock(
                            foreground = gruvbox2['dark-gray'],
                            background = gruvbox['white'],
                            format=' %b%d,%a-%H:%M',
                            
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['white'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.Systray(
                            background=gruvbox['fg0'],
                            foreground = gruvbox['fg0'],
                            icon_size = 22,
                    )
                                       
            ],
               background=gruvbox['bg'], size=26, margin=[10, 10, 0, 10],
        )
    )
]

# screens = [ Screen() ]

dgroups_key_binder = None
dgroups_app_rules = []  
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True



# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])