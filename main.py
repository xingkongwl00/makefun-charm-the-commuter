from pathlib import Path

"""Write one playful forecast line for a city that isn't to /output/entry.txt."""

JOKE = "Rain in Nimmerport, with a chance of lowercase seagulls. Commute accordingly."

# The grader reads the entry from this exact absolute path.
OUTPUT_DIR = Path("/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ENTRY_PATH = OUTPUT_DIR / "entry.txt"
ENTRY_PATH.write_text(JOKE, encoding="utf-8")
