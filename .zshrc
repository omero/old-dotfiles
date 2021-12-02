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

alias vim="nvim"
eval "$(direnv hook zsh)"

#pip variables
export PATH="$HOME/Library/Python/3.9/bin:/opt/homebrew/bin:$PATH"

# go variables
export GOPATH=~/go
PATH=${PATH}:${GOPATH}/bin
export PATH=$PATH:/usr/local/go/bin
export KO_DOCKER_REPO="quay.io/omero"

# nvm
#export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}"  ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
#[ -s "$NVM_DIR/nvm.sh"  ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

export NVM_DIR="$HOME/.nvm"
    [ -s "$(brew --prefix)/opt/nvm/nvm.sh" ] && . "$(brew --prefix)/opt/nvm/nvm.sh" # This loads nvm
#    [ -s "$(brew --prefix)/opt/nvm/etc/bash_completion.d/nvm" ] && . "$(brew --prefix)/opt/nvm/etc/bash_completion.d/nvm" # This loads nvm bash_completion

#source <(${HOME}/.google-cloud-sdk/bin/kubectl completion zsh)

#Internal pantheon configs
# Cert
export PANTHEON_CERT="$HOME/certs/omar.aguirre@getpantheon.com.pem"

export GOPRIVATE=github.com/pantheon-systems/*

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
# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/omers/.google-cloud-sdk/path.zsh.inc' ]; then . '/Users/omers/.google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/omers/.google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/omers/.google-cloud-sdk/completion.zsh.inc'; fi
