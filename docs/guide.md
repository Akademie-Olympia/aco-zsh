# Shell, CLI Commands & Productivity Aliases

The command-line environment centers on **Zsh** (`~/.config/zsh/zshrc` and `~/.config/zsh/aliases.zsh`) enhanced with **Oh My Zsh**, syntax highlighting in the desktop theme colours, asynchronous autosuggestions, FZF integration, and custom CLI tools (`aco` / `arch-dot` / `aco-arch-dotfiles` and `wallpaper`).

---

## Prompt & Environment (`zsh/zshrc`)

- **Default Editor**: `EDITOR="nvim"` and `VISUAL="nvim"`
- **Graphical Sudo Prompt**: `SUDO_ASKPASS="$HOME/.config/hypr/askpass.sh"` (uses `fuzzel --dmenu --password` in Wayland sessions)
- **PATH**: Automatically prepends `~/.local/bin` so custom CLI tools (`arch-dot`, `aco-arch-dotfiles`, `wallpaper`) are available everywhere.
- **Minimal Prompt**: directory in the accent colour, git branch (with a dot when dirty) and a `❯` that turns red after a failed command (`themes/aco.zsh-theme`). Only terminal palette colours are used, so it follows `aco-theme` live.
- **TUI Styling (`NEWT_COLORS`)**: named terminal colours for `nmtui` and other libnewt TUI utilities.

---

## Active Oh My Zsh Plugins & Keybindings

| Plugin / Integration | Keybinding / Trigger | Description |
| :--- | :--- | :--- |
| **`sudo`** | <kbd>Esc</kbd> <kbd>Esc</kbd> *(press Escape twice)* | Automatically prefixes the current or previous command line with `sudo` |
| **`zsh-autosuggestions`** | <kbd>→</kbd> *(Right Arrow)* or <kbd>End</kbd> | Accepts the inline historical command suggestion (rendered in muted Overlay0 `#6c7086`) |
| **`zsh-syntax-highlighting`** | Live while typing | Highlights valid commands in Pastel Blue (`#89b4fa`), aliases in Teal (`#94e2d5`), builtins in Mauve (`#cba6f7`), strings in Green (`#a6e3a1`), and invalid tokens in Red (`#f38ba8`) |
| **`fzf --zsh`** | <kbd>Ctrl</kbd> + <kbd>R</kbd> / <kbd>Ctrl</kbd> + <kbd>T</kbd> / <kbd>Alt</kbd> + <kbd>C</kbd> | Fuzzy search command history (`Ctrl+R`), insert file path (`Ctrl+T`), or fuzzy `cd` into directory (`Alt+C`) |
| **`zoxide init zsh --cmd j`** | **`j <query>`** / **`ji`** *(also `z` / `zi`)* | **Smart Directory Jump (`j` for jump)** powered under the hood by **zoxide**: jumps to the highest-ranked matching directory (`j`) or opens an interactive `fzf` directory picker (`ji`) |
| **`git`** | `gst`, `ga`, `gc`, `gp`, `gl`, ... | Standard Oh My Zsh Git aliases and completions |

---

## Custom CLI Programs (`/usr/bin`)

### 1. `aco` / `arch-dot` / `aco-arch-dotfiles` (Unified Ecosystem & Dotfiles Manager)

Provided by `aco-arch-dotfiles-core` as `/usr/bin/aco`, `arch-dot`, and
`aco-arch-dotfiles`. Updates use Pacman exclusively; there are no runtime subtree
pulls or Git clones. See [package setup and activation](https://aco-arch-dotfiles.readthedocs.io/en/latest/arch-package/).

| Command | Action |
| :--- | :--- |
| `aco update` | Run `sudo pacman -Syu`, then safely synchronize user copies |
| `aco sync` | Synchronize defaults only, e.g. after running Pacman yourself |
| `aco status` | Inspect activation and user configuration paths |
| `aco list` | List installed dotfiles packages |
| `aco keys` / `aco docs` | Show documentation locations |
| `aco commands` | Show package-management commands |
| `aco scripts` | Show available helper binaries |
| `aco install [module ...]` / `aco links [module ...]` | Activate installed modules without sudo |
| `aco deactivate [module ...]` | Restore previous settings |
| `aco packages [package ...]` | Install selected packages with `pacman -Syu --needed` (default: metapackage) |
| `aco path` | Print the editable user configuration directory |
| `aco help` | Display help message and subcommands |

### 2. `wallpaper` (Multi-Monitor Wallpaper Manager)

Provided by `aco-arch-dotfiles-wallpaper`; prefers the activated user script
`~/.config/wallpaper/wallpaper.sh` (alias: `wp`):

| Command | Action |
| :--- | :--- |
| `wallpaper` *(or `wp`)* | Launch interactive Fuzzel TUI (choose target monitor + wallpaper) |
| `wallpaper list [--monitor MON] [--plain]` | List all wallpapers (`★` = global default, `●` = monitor override) |
| `wallpaper set <name\|path> [--monitor MON \| --all]` | Set global default, per-monitor override, or apply everywhere (`--all`) |
| `wallpaper default [<name\|path>]` | Show or set the global default wallpaper |
| `wallpaper monitor <MON> [<name\|path>\|default]` | Show, set, or remove a per-monitor override |
| `wallpaper clear <MON> \| --all` | Clear override for `<MON>` or all monitors |
| `wallpaper current` | Show saved state and active wallpapers per connected monitor |
| `wallpaper next` / `wallpaper prev` / `wallpaper random` | Cycle to next, previous, or random wallpaper |
| `wallpaper add <file>... [--move] [--set]` | Copy/move images into the user library and optionally apply |
| `wallpaper apply` / `wallpaper reload` | Apply saved state / restart `hyprpaper` and re-apply |
| `wallpaper dirs` / `wallpaper open` / `wallpaper doctor` | Show configured directories / open in file manager / run diagnostics |

---

## Custom Aliases & Shell Functions (`zsh/aliases.zsh`)

### Dotfiles & Maintenance Aliases

| Alias | Command Executed | Purpose |
| :--- | :--- | :--- |
| `dotfiles` | `cd "${XDG_DATA_HOME:-$HOME/.local/share}/arch-dotfiles/config"` | Jump to editable configuration copies |
| `cfg-update` | `aco update` | Full system upgrade and user sync |
| `cfg-links` | `aco-arch-dotfiles-config activate` | Activate installed modules |
| `wp` | `wallpaper` | Short alias for the wallpaper manager |

### Text Editors & Interactive Fuzzy Openers

| Alias / Function | Implementation | Purpose |
| :--- | :--- | :--- |
| `nv` | `nvim` | Open [Neovim (`aco-nvim`)](https://aco-nvim.readthedocs.io/en/latest/) |
| `v` | `vim` | Open standalone [Vim (`aco-vim`)](https://aco-vim.readthedocs.io/en/latest/) |
| `fznv [args]` | `fzf --height=40% --layout=reverse --border --prompt='nvim > '` -> `nvim` | Fuzzy-find a file interactively and open it in Neovim |
| `fzv [args]` | `fzf --height=40% --layout=reverse --border --prompt='vim > '` -> `vim` | Fuzzy-find a file interactively and open it in Vim |

### Smart Directory Jumping with `j` (Powered by `zoxide`)

Directory navigation uses the short command **`j`** (for **jump**), backed under the hood by **`zoxide`** (`eval "$(zoxide init zsh --cmd j)"`):

| Command | Action |
| :--- | :--- |
| **`j <pattern>`** *(or `z <pattern>`)* | **Jump (`j`)** directly to the highest-ranked directory matching `<pattern>` based on frecency (`zoxide` database) |
| **`ji`** *(or `zi`)* | Open an **interactive `fzf` directory picker** over your `zoxide` history and jump to the selection |
| **`j -`** *(or `z -`)* | Jump back to the previous directory |

### Yazi Directory-Tracking Wrapper (`y`)

The `y` shell function wraps `yazi` (`yazi "$@" --cwd-file="$tmp"`). When you navigate through directories in Yazi and press <kbd>q</kbd> to quit, your current Zsh shell automatically `cd`s into the last directory you visited:

```bash
y [path]
```

### tmux Session Shortcuts

See the full [tmux-config Documentation](https://aco-tmux.readthedocs.io/en/latest/) for internal tmux bindings.

| Alias | Command Executed | Purpose |
| :--- | :--- | :--- |
| `tm` | `tmux new-session -A -s main` | Attach to primary session `main` (or create it if not running) |
| `tn <name>` | `tmux new-session -s <name>` | Create a new named tmux session |
| `ta <name>` | `tmux attach -t <name>` | Attach to an existing named tmux session |
| `tl` | `tmux list-sessions` | List all active tmux sessions |

### Colorized System Utilities

| Alias | Command Executed |
| :--- | :--- |
| `ls` | `ls --color=auto` |
| `ll` | `ls -lah --color=auto` |
| `la` | `ls -A --color=auto` |
| `grep` | `grep --color=auto` |
| `diff` | `diff --color=auto` |
| `ip` | `ip -color=auto` |
