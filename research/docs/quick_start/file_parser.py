#! /usr/bin/env python

"""
A simple file parser to get rid of duplicate ``` python lines
"""

from pathlib import Path

current_dir = Path(__file__).parent
filepath = current_dir / "Pandas QS.qmd"


def main():
    with open(filepath, "r", encoding="utf-8") as f:
        lines= f.readlines()

    with open(filepath, "w", encoding="utf-8") as f:
        line_num = 0
        for line in lines:
            if line.strip() == "``` python":
                line_num += 1
                if line_num % 2 == 0:
                    f.write("```\n")
                else:
                    f.write(line)
            else:
                f.write(line)


if __name__ == "__main__":
    main()
