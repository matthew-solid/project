import os
import re


def fix_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Fix trailing whitespace
    content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)

    # Fix blank lines
    content = re.sub(r"\n\s*\n\s*\n", "\n\n", content)

    # Fix line length
    lines = content.split("\n")
    fixed_lines = []
    for line in lines:
        if len(line) > 79 and not line.startswith("#"):
            # Try to break at a comma or space
            if "," in line:
                parts = line.split(",")
                current_line = ""
                for part in parts:
                    if len(current_line + part + ",") > 79:
                        fixed_lines.append(current_line.rstrip())
                        current_line = "    " + part + ","
                    else:
                        current_line += part + ","
                fixed_lines.append(current_line.rstrip(","))
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)

    content = "\n".join(fixed_lines)

    # Ensure file ends with newline
    if not content.endswith("\n"):
        content += "\n"

    with open(file_path, "w") as f:
        f.write(content)


def main():
    # Fix Python files in src and tests directories
    for root, _, files in os.walk("."):
        if "src" in root or "tests" in root:
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    print(f"Fixing {file_path}")
                    fix_file(file_path)


if __name__ == "__main__":
    main()
