"""Legacy entrypoint kept for backward compatibility.

Please use: python -m news_crawler.cli
"""

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from news_crawler.cli import main


if __name__ == "__main__":
    main()
