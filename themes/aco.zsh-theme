# ============================================================================
# ACO prompt: directory, git branch and an arrow that turns red after a failure.
# Only terminal palette colours are used, so the prompt follows aco-theme live
# (light/dark, and colour 12 is the accent).
# ============================================================================

ZSH_THEME_GIT_PROMPT_PREFIX="  %F{8}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%f"
ZSH_THEME_GIT_PROMPT_DIRTY=" %F{3}●"
ZSH_THEME_GIT_PROMPT_CLEAN=""

PROMPT='%F{12}%~%f$(git_prompt_info) %(?.%F{2}.%F{1})❯%f '
