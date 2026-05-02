import os
from pathlib import Path

ROOT = Path(".")
README = ROOT / "README.md"
START = "<!-- AUTO-GENERATED-TREE:START -->"
END   = "<!-- AUTO-GENERATED-TREE:END -->"

EXCLUDE = {
    ".git",
    "__pycache__",
    ".DS_Store"
}

EXCLUDE_PATHS = {
    ".github/workflows"
}

def should_skip(path: Path):
    txt = str(path).replace("\\", "/")
    for banned in EXCLUDE_PATHS:
        if txt.startswith(banned):
            return True
    for part in path.parts:
        if part in EXCLUDE:
            return True
    return False

def sorted_items(path):
    items = [p for p in path.iterdir() if not should_skip(p)]
    return sorted(items, key=lambda x: (x.is_file(), x.name.lower()))
def build_tree(path: Path, prefix=""):
    lines = []
    items = sorted_items(path)

    for i, item in enumerate(items):
        last = i == len(items) - 1
        connector = "└── " if last else "├── "
        lines.append(prefix + connector + item.name)
        if item.is_dir():
            extension = "    " if last else "│   "
            lines.extend(build_tree(item, prefix + extension))
    return lines
def generate_tree_block():
    lines = ["LinuxCommands"]
    lines.extend(build_tree(ROOT))
    tree = "\n".join(lines)
    return f"""{START}
<pre><code>
{tree}
</code></pre>
{END}"""

def update_readme():
    content = README.read_text(encoding="utf-8")
    if START not in content or END not in content:
        raise Exception("No se encontraron los marcadores AUTO-GENERATED-TREE en README.md")
    start_pos = content.index(START)
    end_pos = content.index(END) + len(END)
    new_block = generate_tree_block()
    updated = content[:start_pos] + new_block + content[end_pos:]
    README.write_text(updated, encoding="utf-8")

if __name__ == "__main__":
    update_readme()