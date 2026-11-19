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

RTD = "https://{}.readthedocs.io/en/latest/"
DOCS = "aco-docs"  # one Read the Docs project for all small components

# (key, short title, one line, URL, page prefix) – the ecosystem shown in every sidebar.
# Components with their own site use RTD.format(key). Small components live in the shared
# aco-docs project; their prefix highlights the entry while one of their pages is open.
PROJECTS = [
    ("aco-arch-dotfiles", "Hub & Installer", "Installation, packages, desktop, cheatsheet", RTD.format("aco-arch-dotfiles"), ""),
    ("aco-hypr", "Hyprland", "Window management, lock screen, screenshots, monitors", RTD.format("aco-hypr"), ""),
    ("aco-nvim", "Neovim", "Editor with plugins, LSP and debugger", RTD.format("aco-nvim"), ""),
    ("aco-vim", "Vim", "Lean Vim configuration", RTD.format("aco-vim"), ""),
    ("aco-tmux", "tmux", "Terminal multiplexer", RTD.format("aco-tmux"), ""),
    ("aco-zsh", "Zsh", "Shell, aliases, prompt", RTD.format("aco-zsh"), ""),
    ("aco-kitty", "Kitty", "Terminal", RTD.format("aco-kitty"), ""),
    ("aco-ghostty", "Ghostty", "Terminal", RTD.format("aco-ghostty"), ""),
    ("aco-docs", "Waybar", "Status bar and power menu", RTD.format(DOCS) + "waybar/", "waybar"),
    ("aco-docs", "Wallpaper", "Wallpaper switcher", RTD.format(DOCS) + "wallpaper/", "wallpaper"),
    ("aco-docs", "Fuzzel", "Launcher and shared menu", RTD.format(DOCS) + "fuzzel/", "fuzzel"),
    ("aco-docs", "Foot", "Lightweight terminal", RTD.format(DOCS) + "foot/", "foot"),
    ("aco-docs", "Yazi", "Terminal file manager", RTD.format(DOCS) + "yazi/", "yazi"),
    ("aco-docs", "PCManFM", "Graphical file manager", RTD.format(DOCS) + "pcmanfm/", "pcmanfm"),
    ("aco-docs", "libfm", "File manager library settings", RTD.format(DOCS) + "libfm/", "libfm"),
    ("aco-docs", "GTK 3", "Theme and settings", RTD.format(DOCS) + "gtk3/", "gtk3"),
    ("aco-docs", "GTK 4", "Theme and settings", RTD.format(DOCS) + "gtk4/", "gtk4"),
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
