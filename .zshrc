eval "$(starship init zsh)"

# ZSH Facts
HISTFILE=${HOME}/.zsh_history
HISTSIZE=20000
SAVEHIST=${HISTSIZE}
COMPLETION_WAITING_DOTS=true
setopt extended_history
setopt hist_expire_dups_first
setopt inc_append_history


source ${HOMEBREW_PREFIX}/share/zsh-autosuggestions/zsh-autosuggestions.zsh

# direnv
eval "$(direnv hook zsh)"

# golang
export GOPATH="$HOME/.go"; export GOROOT="$HOME/.local/share/go"; export PATH="$GOPATH/bin:$PATH"; # g-install: do NOT edit, see https://github.com/stefanmaric/g

# alias exa 
alias ls="exa --icons --group-directories-first --time-style=long-iso --git"
alias tree="exa --tree --icons"

# nvm
export NVM_DIR="$HOME/.nvm"
    [ -s "$(brew --prefix)/opt/nvm/nvm.sh" ] && . "$(brew --prefix)/opt/nvm/nvm.sh" # This loads nvm

# ssh agent to use gpg
eval $(ssh-agent)
if [ ! -n "$SSH_CLIENT" ]; then
  gpgconf --launch gpg-agent

  if [ "${gnupg_SSH_AUTH_SOCK_by:-0}" -ne $$ ]; then
      export SSH_AUTH_SOCK="$(gpgconf --list-dirs agent-ssh-socket)"
  fi

  GPG_TTY=$(tty)
  export GPG_TTY
  # only necessary if using pinentry in the tty (instead of GUI)
  echo UPDATESTARTUPTTY | gpg-connect-agent > /dev/null 2>&1
fi

# gcp
# The next line updates PATH for the Google Cloud SDK.
source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.zsh.inc"
# The next line enables shell command completion for gcloud.
source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.zsh.inc"


export PATH=${PATH}:${HOME}/.bin
export PATH=${PATH}:${HOME}/.local/bin

