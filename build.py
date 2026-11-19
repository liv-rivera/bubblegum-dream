#!/usr/bin/env python3
"""Generate every Bubblegum Dream theme file from palette.json.

Edit palette.json, then run:  python3 build.py
"""
import json
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent
P = json.loads((ROOT / "palette.json").read_text())
ui, sx, st, term, charts = P["ui"], P["syntax"], P["status"], P["terminal"], P["charts"]
NAME = P["name"]
SLUG = "bubblegum-dream"


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n")
    print("wrote", rel)


def dump(obj):
    return json.dumps(obj, indent=2)


def rgb(hex_):
    h = hex_.lstrip("#")
    return "rgb({},{},{})".format(*(int(h[i:i + 2], 16) for i in (0, 2, 4)))


# --------------------------------------------------------------- VS Code
vscode_colors = {
    "foreground": ui["foreground"],
    "focusBorder": ui["bubblegumLight"],
    "selection.background": ui["selection"],
    "widget.shadow": "#d6478c22",
    "textLink.foreground": sx["rose"],
    "textLink.activeForeground": ui["bubblegum"],
    "editor.background": ui["background"],
    "editor.foreground": ui["foreground"],
    "editorGutter.background": ui["background"],
    "editorLineNumber.foreground": ui["subtle"],
    "editorLineNumber.activeForeground": ui["bubblegum"],
    "editorCursor.foreground": ui["bubblegum"],
    "editor.selectionBackground": ui["selection"],
    "editor.inactiveSelectionBackground": ui["highlight"],
    "editor.lineHighlightBackground": ui["highlightSoft"],
    "editor.findMatchBackground": "#f2cf6b88",
    "editor.findMatchHighlightBackground": "#f2cf6b44",
    "editor.wordHighlightBackground": "#b48ccf33",
    "editorBracketMatch.background": "#f59ac244",
    "editorBracketMatch.border": ui["bubblegumLight"],
    "editorIndentGuide.background1": ui["line"],
    "editorIndentGuide.activeBackground1": ui["bubblegumLight"],
    "editorWhitespace.foreground": ui["line"],
    "editorRuler.foreground": ui["line"],
    "editorBracketHighlight.foreground1": sx["bubblegum"],
    "editorBracketHighlight.foreground2": sx["lilac"],
    "editorBracketHighlight.foreground3": sx["periwinkle"],
    "editorBracketHighlight.foreground4": sx["mint"],
    "editorBracketHighlight.foreground5": sx["peach"],
    "editorBracketHighlight.foreground6": sx["butter"],
    "editorError.foreground": st["error"],
    "editorWarning.foreground": st["warning"],
    "editorInfo.foreground": st["info"],
    "editorGutter.addedBackground": st["success"],
    "editorGutter.modifiedBackground": st["info"],
    "editorGutter.deletedBackground": st["error"],
    "diffEditor.insertedTextBackground": "#5fb88a22",
    "diffEditor.removedTextBackground": "#dd4f5f22",
    "editorWidget.background": ui["surface"],
    "editorWidget.border": ui["line"],
    "editorSuggestWidget.background": ui["surface"],
    "editorSuggestWidget.selectedBackground": ui["highlight"],
    "editorHoverWidget.background": ui["surface"],
    "editorHoverWidget.border": ui["line"],
    "editorGroupHeader.tabsBackground": ui["sidebar"],
    "editorGroup.border": ui["line"],
    "tab.activeBackground": ui["background"],
    "tab.activeForeground": ui["foreground"],
    "tab.activeBorderTop": ui["bubblegum"],
    "tab.inactiveBackground": ui["sidebar"],
    "tab.inactiveForeground": ui["muted"],
    "tab.border": ui["line"],
    "activityBar.background": ui["activityBar"],
    "activityBar.foreground": ui["bubblegum"],
    "activityBar.inactiveForeground": ui["muted"],
    "activityBarBadge.background": ui["bubblegum"],
    "activityBarBadge.foreground": "#ffffff",
    "sideBar.background": ui["sidebar"],
    "sideBar.foreground": ui["foreground"],
    "sideBar.border": ui["line"],
    "sideBarTitle.foreground": ui["muted"],
    "sideBarSectionHeader.background": ui["activityBar"],
    "sideBarSectionHeader.foreground": ui["foreground"],
    "list.activeSelectionBackground": ui["selection"],
    "list.activeSelectionForeground": ui["foreground"],
    "list.inactiveSelectionBackground": ui["highlight"],
    "list.hoverBackground": ui["highlightSoft"],
    "list.focusOutline": ui["bubblegumLight"],
    "list.highlightForeground": ui["bubblegum"],
    "titleBar.activeBackground": ui["activityBar"],
    "titleBar.activeForeground": ui["foreground"],
    "titleBar.inactiveBackground": ui["sidebar"],
    "titleBar.inactiveForeground": ui["muted"],
    "statusBar.background": ui["statusBar"],
    "statusBar.foreground": ui["foreground"],
    "statusBar.noFolderBackground": "#e8d5f0",
    "statusBar.debuggingBackground": "#f9d3b8",
    "statusBarItem.remoteBackground": ui["bubblegum"],
    "statusBarItem.remoteForeground": "#ffffff",
    "panel.background": ui["background"],
    "panel.border": ui["line"],
    "panelTitle.activeForeground": ui["foreground"],
    "panelTitle.activeBorder": ui["bubblegum"],
    "panelTitle.inactiveForeground": ui["muted"],
    "button.background": ui["bubblegum"],
    "button.foreground": "#ffffff",
    "button.hoverBackground": sx["bubblegum"],
    "button.secondaryBackground": ui["highlight"],
    "button.secondaryForeground": ui["foreground"],
    "badge.background": ui["bubblegumLight"],
    "badge.foreground": ui["foreground"],
    "input.background": ui["elevated"],
    "input.border": ui["line"],
    "input.placeholderForeground": ui["subtle"],
    "inputOption.activeBorder": ui["bubblegum"],
    "dropdown.background": ui["elevated"],
    "dropdown.border": ui["line"],
    "checkbox.background": ui["elevated"],
    "checkbox.border": ui["line"],
    "progressBar.background": ui["bubblegum"],
    "scrollbarSlider.background": "#f59ac244",
    "scrollbarSlider.hoverBackground": "#f59ac277",
    "scrollbarSlider.activeBackground": "#d6478c88",
    "minimap.background": ui["background"],
    "breadcrumb.foreground": ui["muted"],
    "breadcrumb.focusForeground": ui["foreground"],
    "notifications.background": ui["surface"],
    "notifications.border": ui["line"],
    "quickInput.background": ui["surface"],
    "pickerGroup.foreground": ui["bubblegum"],
    "menu.background": ui["surface"],
    "menu.selectionBackground": ui["highlight"],
    "menu.selectionForeground": ui["foreground"],
    "gitDecoration.addedResourceForeground": sx["mint"],
    "gitDecoration.modifiedResourceForeground": sx["periwinkle"],
    "gitDecoration.deletedResourceForeground": sx["coral"],
    "gitDecoration.untrackedResourceForeground": sx["lilac"],
    "gitDecoration.ignoredResourceForeground": ui["subtle"],
    "gitDecoration.conflictingResourceForeground": sx["peach"],
    "terminal.background": term["background"],
    "terminal.foreground": term["foreground"],
    "terminalCursor.foreground": term["cursor"],
    "terminal.selectionBackground": term["selection"],
}
for k in ["black", "red", "green", "yellow", "blue", "white"]:
    vscode_colors["terminal.ansi" + k.capitalize()] = term[k]
    vscode_colors["terminal.ansiBright" + k.capitalize()] = term["bright" + k.capitalize()]
vscode_colors["terminal.ansiMagenta"] = term["purple"]
vscode_colors["terminal.ansiBrightMagenta"] = term["brightPurple"]
vscode_colors["terminal.ansiCyan"] = term["cyan"]
vscode_colors["terminal.ansiBrightCyan"] = term["brightCyan"]


def tc(name, scope, color, style=None):
    s = {"foreground": color}
    if style:
        s["fontStyle"] = style
    return {"name": name, "scope": scope, "settings": s}


token_colors = [
    tc("Comments", ["comment", "punctuation.definition.comment"], sx["comment"], "italic"),
    tc("Keywords & storage", ["keyword", "storage.type", "storage.modifier", "keyword.control"], sx["bubblegum"]),
    tc("Operators", ["keyword.operator", "punctuation.accessor"], sx["rose"]),
    tc("Strings", ["string", "string.quoted", "string.template"], sx["mint"]),
    tc("String escapes & regex", ["constant.character.escape", "string.regexp"], sx["teal"]),
    tc("Numbers & constants", ["constant.numeric", "constant.language", "constant.other"], sx["peach"]),
    tc("Functions", ["entity.name.function", "support.function", "meta.function-call"], sx["periwinkle"]),
    tc("Types & classes", ["entity.name.type", "entity.name.class", "support.type", "support.class", "entity.other.inherited-class"], sx["lilac"]),
    tc("Variables", ["variable", "variable.other"], ui["foreground"]),
    tc("Parameters", ["variable.parameter"], sx["rose"], "italic"),
    tc("this / self", ["variable.language"], sx["coral"], "italic"),
    tc("Properties & keys", ["variable.other.property", "support.type.property-name", "meta.object-literal.key"], sx["teal"]),
    tc("Decorators & annotations", ["meta.decorator", "entity.name.function.decorator", "storage.type.annotation"], sx["butter"]),
    tc("Tags", ["entity.name.tag"], sx["bubblegum"]),
    tc("Attributes", ["entity.other.attribute-name"], sx["lilac"], "italic"),
    tc("Punctuation", ["punctuation", "meta.brace"], ui["muted"]),
    tc("Imports & namespaces", ["entity.name.namespace", "entity.name.module", "keyword.control.import"], sx["lilac"]),
    tc("SQL keywords", ["keyword.other.DML.sql", "keyword.other.sql"], sx["bubblegum"]),
    tc("Markdown headings", ["markup.heading", "entity.name.section.markdown"], sx["bubblegum"], "bold"),
    tc("Markdown bold", ["markup.bold"], sx["rose"], "bold"),
    tc("Markdown italic", ["markup.italic"], sx["lilac"], "italic"),
    tc("Markdown links", ["markup.underline.link", "string.other.link"], sx["periwinkle"]),
    tc("Markdown code", ["markup.inline.raw", "markup.fenced_code"], sx["teal"]),
    tc("Inserted", ["markup.inserted"], sx["mint"]),
    tc("Deleted", ["markup.deleted"], sx["coral"]),
    tc("Invalid", ["invalid"], sx["coral"], "underline"),
]

write(f"vscode/themes/{SLUG}-color-theme.json", dump({
    "$schema": "vscode://schemas/color-theme",
    "name": NAME,
    "type": "light",
    "semanticHighlighting": True,
    "colors": vscode_colors,
    "tokenColors": token_colors,
    "semanticTokenColors": {
        "parameter": {"foreground": sx["rose"], "italic": True},
        "property": sx["teal"],
        "type": sx["lilac"],
        "class": sx["lilac"],
        "enumMember": sx["peach"],
        "function": sx["periwinkle"],
        "method": sx["periwinkle"],
        "decorator": sx["butter"],
        "namespace": sx["lilac"],
    },
}))

write("vscode/package.json", dump({
    "name": SLUG,
    "displayName": NAME,
    "description": P["description"],
    "version": "1.0.0",
    "publisher": "bubblegum-dream",
    "license": "MIT",
    "engines": {"vscode": "^1.70.0"},
    "categories": ["Themes"],
    "keywords": ["pink", "pastel", "light", "bubblegum", "theme"],
    "galleryBanner": {"color": ui["background"], "theme": "light"},
    "contributes": {"themes": [{
        "label": NAME,
        "uiTheme": "vs",
        "path": f"./themes/{SLUG}-color-theme.json",
    }]},
}))

write("vscode/README.md", f"""# {NAME} for VS Code

Install the packaged theme: Extensions panel → `···` menu → **Install from VSIX…** → pick `{SLUG}-1.0.0.vsix`.
Then press **Ctrl + K, Ctrl + T** and choose **{NAME}**.
""")
write("vscode/LICENSE", (ROOT / "LICENSE").read_text())

# ------------------------------------------------------ Windows Terminal
write(f"windows-terminal/{SLUG}.json", dump({
    "name": NAME,
    "background": term["background"],
    "foreground": term["foreground"],
    "cursorColor": term["cursor"],
    "selectionBackground": term["selection"],
    **{k: term[k] for k in [
        "black", "red", "green", "yellow", "blue", "purple", "cyan", "white",
        "brightBlack", "brightRed", "brightGreen", "brightYellow",
        "brightBlue", "brightPurple", "brightCyan", "brightWhite"]},
}))

# -------------------------------------------------------- GNOME Terminal
ansi_order = ["black", "red", "green", "yellow", "blue", "purple", "cyan", "white"]
palette16 = [term[k] for k in ansi_order] + [term["bright" + k.capitalize()] for k in ansi_order]
write(f"gnome-terminal/{SLUG}.dconf", "\n".join([
    "[/]",
    f"visible-name='{NAME}'",
    "use-theme-colors=false",
    f"background-color='{rgb(term['background'])}'",
    f"foreground-color='{rgb(term['foreground'])}'",
    "bold-color-same-as-fg=true",
    "cursor-colors-set=true",
    f"cursor-background-color='{rgb(term['cursor'])}'",
    f"cursor-foreground-color='{rgb(term['brightWhite'])}'",
    "highlight-colors-set=true",
    f"highlight-background-color='{rgb(term['selection'])}'",
    f"highlight-foreground-color='{rgb(term['foreground'])}'",
    "palette=[" + ", ".join(f"'{rgb(c)}'" for c in palette16) + "]",
]))

# A fixed UUID keeps re-installs idempotent.
PROFILE_ID = str(uuid.uuid5(uuid.NAMESPACE_URL, "bubblegum-dream/gnome-terminal"))
write("gnome-terminal/install.sh", f"""#!/usr/bin/env bash
# Adds a "{NAME}" profile to GNOME Terminal without touching your other profiles.
set -euo pipefail
cd "$(dirname "$0")"
ID="{PROFILE_ID}"
BASE=/org/gnome/terminal/legacy/profiles:
dconf load "$BASE/:$ID/" < {SLUG}.dconf
LIST=$(dconf read "$BASE/list" || true)
if [[ -z "$LIST" ]]; then
  dconf write "$BASE/list" "['$ID']"
elif [[ "$LIST" != *"$ID"* ]]; then
  dconf write "$BASE/list" "${{LIST%]}}, '$ID']"
fi
if [[ "${{1:-}}" == "--default" ]]; then
  dconf write "$BASE/default" "'$ID'"
  echo "{NAME} installed and set as the default profile."
else
  echo "{NAME} installed. Pick it from the terminal's profile menu, or rerun with --default."
fi
""")

# ---------------------------------------------------------------- Superset
write(f"superset/{SLUG}.json", dump({
    "algorithm": "default",
    "token": {
        "colorPrimary": ui["bubblegum"],
        "colorLink": sx["rose"],
        "colorLinkHover": ui["bubblegum"],
        "colorInfo": st["info"],
        "colorSuccess": st["success"],
        "colorWarning": st["warning"],
        "colorError": st["error"],
        "colorTextBase": ui["foreground"],
        "colorTextSecondary": ui["muted"],
        "colorTextTertiary": ui["subtle"],
        "colorBgBase": ui["surface"],
        "colorBgLayout": ui["background"],
        "colorBgContainer": ui["surface"],
        "colorBgElevated": ui["elevated"],
        "colorFillSecondary": ui["highlight"],
        "colorFillTertiary": ui["highlightSoft"],
        "colorFillQuaternary": "#fef5f8",
        "colorBorder": ui["line"],
        "colorBorderSecondary": ui["lineSoft"],
        "controlItemBgActive": ui["highlight"],
        "controlItemBgHover": ui["highlightSoft"],
        "controlOutline": "rgba(214, 71, 140, 0.18)",
        "borderRadius": 10,
        "borderRadiusSM": 6,
        "borderRadiusLG": 14,
        "wireframe": False,
        "fontFamily": "Nunito, Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "fontUrls": ["https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap"],
    },
    "echartsOptionsOverrides": {"color": charts},
}))

# --------------------------------------------------------------- Web / CSS
css_vars = [
    ("bg", ui["background"]), ("surface", ui["surface"]), ("elevated", ui["elevated"]),
    ("fg", ui["foreground"]), ("muted", ui["muted"]), ("subtle", ui["subtle"]),
    ("line", ui["line"]), ("accent", ui["bubblegum"]), ("accent-text", sx["rose"]),
    ("accent-soft", ui["highlight"]), ("accent-light", ui["bubblegumLight"]),
    ("info", st["info"]), ("success", st["success"]), ("warning", st["warning"]), ("error", st["error"]),
]
css = [f"/* {NAME}: CSS variables for web pages and dashboards. Generated by build.py. */", ":root {"]
css += [f"  --bd-{k}: {v};" for k, v in css_vars]
css += [f"  --bd-chart-{i + 1}: {c};" for i, c in enumerate(charts)]
css += ["  --bd-radius: 10px;", "  --bd-font: Nunito, Inter, system-ui, sans-serif;", "}", ""]
css += ["/* Dark companion */", "@media (prefers-color-scheme: dark) {", "  :root:not([data-theme=\"light\"]) {"]
dark = {"bg": "#1f161b", "surface": "#2a1e25", "elevated": "#33242d", "fg": "#f6e6ee", "muted": "#c2a3b3",
        "subtle": "#9c8190", "line": "#43303a", "accent": "#f2a7c3", "accent-text": "#f2a7c3",
        "accent-soft": "#4a2a39", "accent-light": "#f7c4d8"}
css += [f"    --bd-{k}: {v};" for k, v in dark.items()]
css += ["  }", "}"]
write(f"web/{SLUG}.css", "\n".join(css))
write(f"web/{SLUG}-charts.json", dump({"name": NAME, "colors": charts}))
