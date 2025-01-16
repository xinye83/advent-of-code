from pathlib import Path

data = (Path(__file__).parent / (Path(__file__).stem + ".in")).read_text().strip("\n")

# --- part 1 ---
