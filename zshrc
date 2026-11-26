# ============================================================================
# ~/.config/zsh/zshrc - Hauptkonfiguration für Zsh
# ============================================================================

export ZSH="${ZSH:-$HOME/.oh-my-zsh}"
if [[ ! -f "$ZSH/oh-my-zsh.sh" && -f /usr/share/arch-dotfiles/oh-my-zsh/oh-my-zsh.sh ]]; then
    export ZSH=/usr/share/arch-dotfiles/oh-my-zsh
fi
if [[ "$ZSH" == /usr/share/arch-dotfiles/oh-my-zsh ]]; then
    export ZSH_CUSTOM="${XDG_CONFIG_HOME:-$HOME/.config}/zsh"
fi
export PATH="$HOME/.local/bin:$PATH"
export EDITOR="nvim"
export VISUAL="nvim"
export SUDO_ASKPASS="$HOME/.config/hypr/askpass.sh"

# Prompt: themes/aco.zsh-theme (folgt dem Desktop-Theme über die Terminalfarben)
ZSH_THEME="aco"

# Schnelle Updates ohne Rückfrage
zstyle ':omz:update' mode auto
if [[ "$ZSH" == /usr/share/arch-dotfiles/oh-my-zsh ]]; then
    # Pacman owns this pinned copy; never update it from an interactive shell.
    zstyle ':omz:update' mode disabled
fi

# Plugins (inkl. Fisch-ähnlicher Autovervollständigung & Syntax-Highlighting)
plugins=(
    git
    sudo
    zsh-autosuggestions
    zsh-syntax-highlighting
)
if [[ "$ZSH" == /usr/share/arch-dotfiles/oh-my-zsh ]]; then
    # These two plugins come from Arch packages instead of runtime git clones.
    plugins=(git sudo)
fi

if [[ -f "$ZSH/oh-my-zsh.sh" ]]; then
    source "$ZSH/oh-my-zsh.sh"
fi

# ============================================================================
# FARBEN FÜR PLUGINS & TOOLS
# ============================================================================
# Nur Terminal-Palettenfarben (0-15): sie kommen aus aco-theme und wechseln
# live mit Hell/Dunkel. 8 = gedämpft, 12 = Akzent, 11 = orange.
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=8"

typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[command]='fg=12,bold'
ZSH_HIGHLIGHT_STYLES[alias]='fg=6,bold'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=5,bold'
ZSH_HIGHLIGHT_STYLES[function]='fg=12,bold'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=1,bold'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=2'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=2'
ZSH_HIGHLIGHT_STYLES[path]='underline'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=11'
ZSH_HIGHLIGHT_STYLES[option]='fg=3'

# Farbschema für TUI-Programme wie nmtui (benannte Terminalfarben)
export NEWT_COLORS='
root=white,black
border=blue,black
window=white,black
shadow=black,black
title=cyan,black
button=black,blue
actbutton=black,cyan
compactbutton=white,black
checkbox=white,black
actcheckbox=black,blue
entry=white,black
disentry=gray,black
label=cyan,black
listbox=white,black
actlistbox=black,blue
sellistbox=black,cyan
actsellistbox=black,cyan
textbox=white,black
acttextbox=black,blue
emptyscale=black,black
fullscale=blue,blue
helpline=cyan,black
roottext=blue,black
'

# ============================================================================
# FZF, Zoxide Shell-Integration & Aliases laden
# ============================================================================
if command -v fzf >/dev/null 2>&1; then
    source <(fzf --zsh)
fi

if command -v zoxide >/dev/null 2>&1; then
    # Initialize zoxide with 'j' (jump) & 'ji' (interactive fzf jump), plus standard 'z' & 'zi'
    eval "$(zoxide init zsh --cmd j)"
fi

if [[ -f "$HOME/.config/zsh/aliases.zsh" ]]; then
    source "$HOME/.config/zsh/aliases.zsh"
fi

if [[ "$ZSH" == /usr/share/arch-dotfiles/oh-my-zsh ]]; then
    source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
    source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
fi

# Added by Antigravity CLI installer
export PATH="$HOME/.local/bin:$PATH"
