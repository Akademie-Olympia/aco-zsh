"""Shared Sphinx settings for every ACO documentation site.

The canonical copy lives in ``aco-arch-dotfiles/docs/_aco`` and is copied into
each component repository by ``scripts/sync-docs-kit.py``. Do not edit the
copies; change the hub and run the script. A component ``conf.py`` is just::

    from _aco.base import configure
    configure(globals(), slug="aco-nvim", title="Neovim", description="...")
"""
import pathlib

from pygments.lexers.configs import IniLexer
from pygments.lexers.special import TextLexer
from sphinx.highlighting import lexers

KIT = pathlib.Path(__file__).resolve().parent
ORG = "Akademie-Olympia"

# (slug, short title, one line) – the ecosystem shown in every sidebar.
PROJECTS = [
    ("aco-arch-dotfiles", "Hub & Installer", "Installation, Pakete, Desktop, Cheatsheet"),
    ("aco-hypr", "Hyprland", "Fensterverwaltung, Sperrbildschirm, Screenshots"),
    ("aco-waybar", "Waybar", "Statusleiste und Powermenü"),
    ("aco-nvim", "Neovim", "Editor mit Plugins, LSP, Debugger"),
    ("aco-vim", "Vim", "Schlanke Vim-Konfiguration"),
    ("aco-tmux", "tmux", "Terminal-Multiplexer"),
    ("aco-zsh", "Zsh", "Shell, Aliase, Prompt"),
    ("aco-kitty", "Kitty", "Terminal"),
    ("aco-ghostty", "Ghostty", "Terminal"),
    ("aco-foot", "Foot", "Terminal"),
    ("aco-yazi", "Yazi", "Dateimanager im Terminal"),
    ("aco-fuzzel", "Fuzzel", "Anwendungsstarter"),
    ("aco-pcmanfm", "PCManFM", "Grafischer Dateimanager"),
    ("aco-libfm", "libfm", "Dateimanager-Bibliothek"),
    ("aco-gtk3", "GTK 3", "Theme und Einstellungen"),
    ("aco-gtk4", "GTK 4", "Theme und Einstellungen"),
    ("aco-wallpaper", "Wallpaper", "Hintergrundbilder"),
]


def configure(namespace, *, slug, title, language="en", exclude=(), suppress=(), extra_extensions=()):
    """Fill a Sphinx ``conf.py`` namespace with the shared ACO defaults."""
    lexers["conf"] = IniLexer()
    lexers["tmux"] = IniLexer()
    lexers["kitty"] = IniLexer()
    lexers["mermaid"] = TextLexer()

    namespace.update(
        project=slug,
        author="Akademie Olympia",
        copyright="2026, Akademie Olympia (ACO)",
        language=language,
        extensions=["myst_parser", "sphinx_copybutton", "sphinx_design", *extra_extensions],
        source_suffix={".md": "markdown"},
        myst_enable_extensions=["colon_fence", "deflist", "attrs_inline", "attrs_block", "fieldlist"],
        myst_heading_anchors=3,
        exclude_patterns=["_build", "Thumbs.db", ".DS_Store", ".venv", "_aco", *exclude],
        suppress_warnings=list(suppress),
        html_theme="furo",
        html_title=f"{title} · ACO",
        html_short_title=title,
        html_static_path=[str(KIT / "static")],
        html_css_files=["aco.css"],
        templates_path=[str(KIT / "templates")],
        html_sidebars={
            "**": [
                "sidebar/scroll-start.html",
                "sidebar/brand.html",
                "sidebar/search.html",
                "sidebar/navigation.html",
                "sidebar/aco-ecosystem.html",
                "sidebar/scroll-end.html",
            ]
        },
        html_context={"aco_projects": PROJECTS, "aco_current": slug},
        html_theme_options={
            "source_repository": f"https://github.com/{ORG}/{slug}",
            "source_branch": "main",
            "source_directory": "docs/",
            "navigation_with_keys": True,
            "top_of_page_buttons": ["view", "edit"],
            "light_css_variables": {
                "color-brand-primary": "#1e66f5",
                "color-brand-content": "#1e66f5",
                "font-stack": "Inter, 'Segoe UI', system-ui, -apple-system, sans-serif",
                "font-stack--monospace": "'JetBrains Mono', 'Fira Code', ui-monospace, monospace",
            },
            "dark_css_variables": {
                "color-brand-primary": "#89b4fa",
                "color-brand-content": "#89b4fa",
                "color-background-primary": "#1e1e2e",
                "color-background-secondary": "#181825",
                "color-background-border": "#313244",
                "color-foreground-primary": "#cdd6f4",
            },
            "footer_icons": [
                {
                    "name": "GitHub",
                    "url": f"https://github.com/{ORG}/{slug}",
                    "html": "GitHub",
                    "class": "",
                },
                {
                    "name": "ACO Hub",
                    "url": "https://aco-arch-dotfiles.readthedocs.io/en/latest/",
                    "html": "ACO Hub",
                    "class": "",
                },
            ],
        },
        pygments_style="friendly",
        pygments_dark_style="nord",
        copybutton_prompt_text=r"\$ |# |>>> ",
        copybutton_prompt_is_regexp=True,
    )
