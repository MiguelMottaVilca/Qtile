from libqtile.config import Key, Group , Match
from libqtile.command import lazy
from .keys import mod, keys


__groups = {
    1:Group("   " , matches = [Match(wm_class=["firefox"])]),
    2:Group("   " , matches = [Match(wm_class=["alacritty"])]),
    3:Group("   " , matches = [Match(wm_class=["code"])]),
    4:Group("   " , matches = [Match(wm_class=["Thunar"])]),
    5:Group(" 阮 " , matches = [Match(wm_class=["spotify"])]),
    6:Group("   "),
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k , g in __groups.items() if g.name == name ][0]

for i in groups:
    keys.extend([
        Key([mod], str(get_group_key(i.name)) ,lazy.group[i.name].toscreen() , 
            desc="Switch to group {}".format(i.name)),

        Key([mod,"shift"],str(get_group_key(i.name)) ,lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

