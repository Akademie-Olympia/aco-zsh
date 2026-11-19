# Arch package

Package: `aco-arch-dotfiles-zsh`. The recipe is in `packaging/arch/PKGBUILD`.
Edit this repository and push to `main`. The central registry checks main branches
every five minutes and publishes automatically versioned, signed packages after
a successful build. GitHub may delay scheduled runs.

Installation: https://github.com/Akademie-Olympia/aco-arch-dotfiles#installation

With sibling checkouts, build using:
`bash ../aco-arch-dotfiles/packaging/arch/build.sh aco-arch-dotfiles-zsh`.
To request an immediate registry build: `gh workflow run packages.yml -R Akademie-Olympia/aco-arch-dotfiles`.
