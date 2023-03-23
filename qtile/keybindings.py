from libqtile import qtile

import subprocess
from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy

mod = "mod4"
mod1 = "mod1"
terminal = "terminator"



def backlight(action):
    def f(qtile):
        brightness = int(subprocess.run(['xbacklight', '-get'],
                                        stdout=subprocess.PIPE).stdout)
        if brightness != 1 or action != 'dec':
            if (brightness > 49 and action == 'dec') \
                                or (brightness > 39 and action == 'inc'):
                subprocess.run(['xbacklight', f'-{action}', '10',
                                '-fps', '10'])
            else:
                subprocess.run(['xbacklight', f'-{action}', '1'])
    return 

my_keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(terminal),
             desc='Launches My Terminal'
             ),
         Key([mod1, "shift"], "c",
             lazy.spawn("google-chrome-stable"),
             desc='Launches My Chrome'
             ),
         Key([mod1,], "s",
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