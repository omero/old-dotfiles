" --- Auto-install vim-plug if not already installed --- "
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source ~/.vimrc
endif 

" --- Plugin section --- "
call plug#begin('~/.vim/plugged')

" --- Status line --- "
Plug 'vim-airline/vim-airline'

" --- Theming --- "
Plug 'artanikin/vim-synthwave84'
Plug 'vim-airline/vim-airline-themes'

" --- Completion and syntax --- "

" Editing and usability
Plug 'jiangmiao/auto-pairs'

" --- Programming Languages ---
Plug 'sheerun/vim-polyglot'
"Plug 'davidhalter/jedi-vim'

" Initialize plugin system
call plug#end()


filetype plugin indent on    " required
syntax on
" gruvbox italic fix (must appear before colorscheme)
" let g:gruvbox_italic = 1
colorscheme synthwave84
" Airline powerline fonts fix
let g:airline_powerline_fonts = 1
" Airline theme
" let g:airline_theme = 'synthwave84'

" User-specific Settings.

" ---Sets---
" 
set encoding=utf-8      		" UTF-8 Support
set tabstop=4                   " 4 spaces will do
set shiftwidth=4                " control indentation for >> bind
set expandtab                   " spaces instead of tabs
set autoindent                  " always set autoindenting on
set relativenumber              " relative line numbers
set number                      " hybrid numbering with both rnu and number
set hidden                      " hide buffers instead of closing them
set ignorecase                  " ignore case when searching
set smartcase                   " ignore case if all lowercase
set nobackup                    " don't need swp files
set noswapfile                  " don't need swp files
"set showmatch                   " Show matching braces when over one
set backspace=indent,eol,start  " allow backspacing everything in insert
set hlsearch                    " highlight searches
set incsearch                   " search as typing
set laststatus=2		        " for lightline.vim plugin


" Use comma as leader
let g:mapleader = ','
" make it possible to write danish letters
let g:AutoPairsShortcutFastWrap=''

" ---Re-mappings---
" 
" Ctrl-C for yanking to register, Ctrl+P to paste from clipboard
vnoremap <C-c> "*y :let @+=@*<CR>
map <C-p> "+P
" since I constantly write accidentally mess these up when going fast
command WQ wq
command Wq wq
command W w
command Q q
" w!! to write with sudo even if not opened with sudo
cmap w!! w !sudo tee >/dev/null %
"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
" Bind to clear search
nmap <leader>/ :nohlsearch<CR>


