# Zsh configuration

Oh My Zsh, autosuggestions, syntax highlighting, fzf, zoxide and shell helpers.

**[Full documentation](https://aco-zsh.readthedocs.io/en/latest/)** ·
[Design & dependencies](https://aco-zsh.readthedocs.io/en/latest/design/) ·
[Installation and updates](https://aco-arch-dotfiles.readthedocs.io/en/latest/arch-package/)

```bash
curl -fsSL https://raw.githubusercontent.com/Akademie-Olympia/aco-arch-dotfiles/main/install.sh | bash -s -- zsh
```

Package: `aco-arch-dotfiles-zsh`. Files: `~/.config/zsh/zshrc`, `aliases.zsh` and `themes/`.
`~/.zshrc` is backed up and linked on activation. The login shell and system services are never changed automatically. All aliases are in the manual.
Develop independently in this repository and push to `main`; after a successful registry build update with `sudo pacman -Syu`. Local builds: [PACKAGING.md](PACKAGING.md).

### Customisation

The entry point is `~/.config/zsh/zshrc`; aliases live in `aliases.zsh`. Test changes in a new shell. The login shell is not switched automatically; the shell guide explains the available helpers.

Your own changes in the activated user copy survive synchronisation; new differing defaults appear as `.pacnew`.
See [update and recovery](https://aco-arch-dotfiles.readthedocs.io/en/latest/verification/).

[![Package safety](https://github.com/Akademie-Olympia/aco-zsh/actions/workflows/package.yml/badge.svg)](https://github.com/Akademie-Olympia/aco-zsh/actions/workflows/package.yml)

[MIT licence](LICENSE).
