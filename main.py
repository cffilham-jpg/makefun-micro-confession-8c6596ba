"""Write Moch an unsent two-part confession to the requested output directory.
The deletion detail was chosen because it is specific, addressee-bound, and too honest
to have sent.
"""

import os
from pathlib import Path


LINE = "To: Moch\nI remember everything you deleted. I never told you."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 260:
    raise ValueError("The entry must be at most 260 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
