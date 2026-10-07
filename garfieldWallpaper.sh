#!/bin/bash

export XDG_DATA_DIRS="/usr/share/cinnamon:/usr/share/gnome:/usr/local/share:/usr/share:$XDG_DATA_DIRS"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "$DIR/code/main.py"

IMAGE_PATH="$DIR/imgs/Wallpaper.png"

echo $IMAGE_PATH

gsettings set org.cinnamon.desktop.background picture-uri "file://$IMAGE_PATH"

echo "Wallpaper Changed!"
