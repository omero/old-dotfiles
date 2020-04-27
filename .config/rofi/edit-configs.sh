declare options=("alacritty
bash
bspwm
picom
dunst
neovim
polybar
qtile
sxhkd
vim
xresources
yadm
zsh
quit")

choice=$(echo -e "${options[@]}" |rofi  -dmenu -i -p 'Edit config file: ')

case "$choice" in
	quit)
		echo "Program terminated." && exit 1
	;;
	alacritty)
		choice="$HOME/.config/alacritty/alacritty.yml"
	;;
	bash)
		choice="$HOME/.bashrc"
	;;
	bspwm)
		choice="$HOME/.config/bspwm/bspwmrc"
	;;
	picom)
		choice="$HOME/.config/picom.conf"
	;;
	dunst)
		choice="$HOME/.config/dunst/dunstrc"
	;;
	neovim)
		choice="$HOME/.config/nvim/init.vim"
	;;
	polybar)
		choice="$HOME/.config/polybar/config"
	;;
	qtile)
		choice="$HOME/.config/qtile/config.py"
	;;
	sxhkd)
		choice="$HOME/.config/sxhkd/sxhkdrc"
	;;
	vim)
		choice="$HOME/.vimrc"
	;;
	xresources)
		choice="$HOME/.Xresources"
	;;
	yadm)
		choice="$HOME/.config/yadm/bootstrap"
	;;
	zsh)
		choice="$HOME/.zshrc"
	;;
	*)
		exit 1
	;;
esac
alacritty -e nvim "$choice"

