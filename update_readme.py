import os
import re


def generate_tree(startpath, ignore_patterns=None):
    """
    Generate a tree representation of the folder structure

    Args:
        startpath: The starting directory path
        ignore_patterns: List of directories or files to ignore

    Returns:
        String representation of the folder structure with emojis
    """
    if ignore_patterns is None:
        ignore_patterns = [
            ".git",
            "__pycache__",
            ".vscode",
            ".idea",
            "venv",
            "env",
            "node_modules",
        ]

    output = []
    prefix = "/"
    output.append(prefix)

    for root, dirs, files in os.walk(startpath):
        # Skip ignored directories
        dirs[:] = [
            d for d in dirs if d not in ignore_patterns and not d.startswith(".")
        ]

        level = root.replace(startpath, "").count(os.sep)
        indent = "│   " * level

        if level > 0:
            subdir = os.path.basename(root)
            output.append(f"{indent}├── 📂 {subdir}/")

        sub_indent = "│   " * (level + 1)
        for f in sorted(files):
            if f not in ignore_patterns and not f.startswith("."):
                output.append(f"{sub_indent}└── 📄 {f}")

    return "\n".join(output)


def update_readme(readme_path, tree_content):
    """
    Update the README.md file with the current folder structure

    Args:
        readme_path: Path to the README.md file
        tree_content: The generated tree structure content
    """
    try:
        with open(readme_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Find and replace the structure section
        pattern = r"```\n/(.*?)\n```"
        replacement = f"```\n{tree_content}\n```"
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print("✅ README.md has been updated with the current folder structure!")
    except FileNotFoundError:
        print(f"❌ Error: {readme_path} not found.")
    except Exception as e:
        print(f"❌ Error updating README: {str(e)}")


if __name__ == "__main__":
    print("🔍 Scanning repository structure...")

    # Generate the folder tree
    tree = generate_tree(".")

    # Update the README
    update_readme("README.md", tree)

    print(
        "🚀 Structure update complete! Your README now reflects the current repository structure."
    )
    print("💡 Tip: Run this script whenever you make changes to your folder structure.")
