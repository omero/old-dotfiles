eval "$(starship init zsh)"

# ZSH Facts
HISTFILE=${HOME}/.zsh_history
HISTSIZE=20000
SAVEHIST=${HISTSIZE}
COMPLETION_WAITING_DOTS=true
setopt extended_history
setopt hist_expire_dups_first
setopt inc_append_history

# WSL gpg specific
source $HOME/.gpg-agent-detect.sh


alias vim="nvim"
eval "$(direnv hook zsh)"

# export BROWSER=google-chrome-stable

# go variables
export GOPATH=~/go
export PATH=$PATH:/usr/local/go/bin
export KO_DOCKER_REPO="quay.io/omero"

# nvm
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}"  ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh"  ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

source <(/home/omers/.google-cloud-sdk/bin/kubectl completion zsh)

#Internal pantheon configs
# Cert
export PANTHEON_CERT="$HOME/certs/omar.aguirre@getpantheon.com.pem"

export GOPRIVATE=github.com/pantheon-systems/*

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/home/omers/.google-cloud-sdk/path.zsh.inc' ]; then . '/home/omers/.google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/home/omers/.google-cloud-sdk/completion.zsh.inc' ]; then . '/home/omers/.google-cloud-sdk/completion.zsh.inc'; fi
