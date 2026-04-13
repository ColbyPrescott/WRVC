from pathlib import Path

this_dir = Path(__file__).resolve().parent
with open(__file__, "r") as infile:
    this_text = infile.read()

dirs = list(this_dir.glob("*.py"))
max_num = max(map(lambda dir: int("".join(filter(lambda char: char.isnumeric(), list(dir.stem)))), dirs))

for dir in dirs:
    max_num += 1
    with open(this_dir / f"goober{max_num}.py", "w") as outfile:
        outfile.write(this_text)