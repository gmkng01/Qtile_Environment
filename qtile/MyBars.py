from libqtile import qtile
from libqtile import widget
from libqtile.bar import Bar
from colors import gruvbox
from unicodes import right_arrow, left_arrow, left_half_circle, lower_left_triangle
from spotify import Spotify

terminal = "terminator"
mera_bar = Bar([
    # lower_left_triangle(gruvbox['fg0'], gruvbox['fg1']),
                    widget.TextBox(
                            text = '',
                            font = "Ubuntu Mono",
                            background = gruvbox['fg0'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                        #     fontsize = 40
                            ),
                    widget.TextBox(
                            text = '◣',
                            font = "Ubuntu Mono",
                            background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 40
                            ),
                    widget.GroupBox(
                            disable_drag=True,
                            active=gruvbox['gray'],
                            inactive=gruvbox['dark-gray'],
                            highlight_method='line',
                            block_highlight_text_color=gruvbox['cyan'],
                            borderwidth=0,
                            highlight_color=gruvbox['fg1'],
                            background=gruvbox['fg1'],
                            fontsize = 16,
                            margin_y = 1,
                            margin_x = 3,
                            padding_y = 0,
                            padding_x = 7,),

                    # lower_left_triangle(gruvbox['fg1'], gruvbox['fg0']),
                    widget.TextBox(
                            text = '◣',
                            font = "Ubuntu Mono",
                            background = gruvbox['fg0'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 40
                            ),
                    widget.CurrentLayout(
                            background=gruvbox['fg0'],
                            foreground=gruvbox['fg9']
                            ),

                    # lower_left_triangle(gruvbox['fg0'], gruvbox['bg0']),
                    widget.TextBox(
                            text = '◣',
                            font = "Ubuntu Mono",
                            background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 40
                            ),
                    widget.WindowCount(
                            text_format='缾 {num}',
                            background=gruvbox['bg0'],
                            foreground=gruvbox['fg9'],
                            show_zero=True,
                            ),

                    # lower_left_triangle(gruvbox['tfg1'], gruvbox['tfg0']),║
                    widget.TextBox(
                            text = '◣',
                            font = "Ubuntu Mono",
                            background = gruvbox['tfg0'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 40
                            ),
                    widget.WindowName(
                            foreground=gruvbox['fg9'],
                            background=gruvbox['tfg0']
                            ),

                    # lower_left_triangle(gruvbox['fg0'], gruvbox['fg1']),
                #     widget.CPU(
                #             format=' {freq_current}GHz {load_percent}%',
                #             mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                #             background=gruvbox['fg1'],
                #             foreground=gruvbox['dark-green']
                #             ),
                #     lower_left_triangle(gruvbox['fg1'], gruvbox['fg0']),
                #     widget.Memory(
                #             format='  {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                #         #     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                #             background=gruvbox['fg0'],
                #             foreground=gruvbox['yellow']
                #             ),

                    lower_left_triangle(gruvbox['tfg0'], gruvbox['fg1']),
                    widget.Net(
                            format = ' {down} ↓↑ {up}',
                            background=gruvbox['fg1'],
                            foreground=gruvbox['dark-blue']
                            ),

                    lower_left_triangle(gruvbox['fg1'], gruvbox['fg0']),
                    widget.Clock(
                            background=gruvbox['fg0'],
                            foreground=gruvbox['dark-magenta'],
                            format='  %a, %b %d - %H:%M'
                            ),

                    lower_left_triangle(gruvbox['fg0'], gruvbox['fg1']),                 
                    widget.Volume(
                            foreground = gruvbox['red'],
                            background = gruvbox['fg1'],
                            fmt = ' {}',
                            mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
                            ),

                    lower_left_triangle(gruvbox['fg1'], gruvbox['fg0']),
                    widget.Systray(
                            background=gruvbox['fg0'],
                            icon_size = 22,
                            ),
                    lower_left_triangle(gruvbox['fg0'], gruvbox['fg1']),
                    
            ],
               background=gruvbox['tbg'], size=26, margin=[8, 8, 1, 8],
        )

# Brightness Up 
def brightup():
  qtile.cmd_spawn('brightnessctl set +5%')
# Brightness Down
def brightdown():
  qtile.cmd_spawn('brightnessctl set 5%-')

def menu():
  qtile.cmd_spawn('/home/abhi/.config/rofi/launchers/type-1/launcher.sh')

mera_bar1 = Bar([
                #     widget.TextBox(
                #             text = '',
                #             font = "JetBrainsMono Nerd Font Mono",
                #             background = gruvbox['fg0'],
                #             foreground = gruvbox['fg1'],
                #             padding = 0,
                #             fontsize = 30
                #     ),
                    widget.TextBox(
                        text='',
                        background = gruvbox['fg0'],
                        # foreground = gruvbox['fg0'],
                        fontsize = 25,
                        mouse_callbacks = {'Button1': menu,},
                        padding = 4,
                        ),
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),
                    
                    widget.GroupBox(
                            active=gruvbox['fg9'],
                            inactive=gruvbox['dark-gray'],
                            highlight_method='line',
                            block_highlight_text_color=gruvbox['dark-red'],
                            borderwidth=0,
                            highlight_color=gruvbox['tbg'],
                            background=gruvbox['fg1'],
                            fontsize = 15,
                            margin_y = 1,
                            margin_x = 1,
                            padding_y = 0,
                            padding_x = 3,
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg'],
                            padding = 0,
                            fontsize = 25
                    ),
                    widget.Backlight(
                                # background = colors[0],
                                # foreground = colors[2],
                                backlight_name = 'intel_backlight',
                                brightness_file = 'brightness',
                                fontsize = 11
                    ),
                        
                    
                    widget.Spacer(),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg'],
                            padding = 0,
                            fontsize = 25
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),

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
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30,
                    ),
                        
                    widget.TextBox(
                            text = '',
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
                        # background = colors[0],
                        # foreground = colors[2],
                        fontsize = 12,
                        mouse_callbacks = {'Button1': brightup, 'Button3': brightdown},
                        padding = 0
                        ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            # background = gruvbox['fg1'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.CPU(
                            format=' {freq_current}GHz {load_percent}%',
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                            background=gruvbox['fg1'],
                            foreground=gruvbox['dark-green']
                            ),
                    
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg1'],
                            foreground = gruvbox['fg0'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.Memory(
                            format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')},
                            background=gruvbox['fg0'],
                            foreground=gruvbox['yellow']
                            ),
                    
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg0'],
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.Net(
                            format = ' {down} ↓↑{up}',
                            background=gruvbox['fg1'],
                            foreground=gruvbox['dark-blue']
                    ), 
               
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg1'],
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
                            foreground = gruvbox['fg1'],
                            padding = 0,
                            fontsize = 30
                    ),

                    widget.Clock(
                            foreground = gruvbox['red'],
                            background = gruvbox['fg1'],
                            format=' %b%d,%a-%H:%M',
                            
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = gruvbox['fg1'],
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
               background=gruvbox['bg'], size=26, margin=[0, 0, 0, 0],
        )