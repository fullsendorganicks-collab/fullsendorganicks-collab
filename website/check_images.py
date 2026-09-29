"""Check that every WordPress image/video a page links to is already on the live site.

Run before sending any page or post:
    python3 website/check_images.py website/pages/<slug>.html [more files...]
With no arguments it checks every file in website/pages/.

"Already on the live site" = referenced by the live homepage or by an original page
from the WordPress export (website/originals/). Anything else was never uploaded,
shows as a broken "?" box, and must not be sent. Exit code 1 if any are found.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA = re.compile(r"wp-content/uploads/\d{4}/\d{2}/[^\"')\s]+")


def live_media():
    files = [os.path.join(HERE, "homepage.html")] + glob.glob(os.path.join(HERE, "originals", "*.html"))
    return {os.path.basename(u) for f in files for u in MEDIA.findall(open(f).read())}


def main(paths):
    live = live_media()
    paths = paths or sorted(glob.glob(os.path.join(HERE, "pages", "*.html")))
    bad = 0
    for p in paths:
        for u in sorted(set(MEDIA.findall(open(p).read()))):
            if os.path.basename(u) not in live:
                bad += 1
                print(f"NOT ON SITE  {os.path.basename(p)}  ->  {u}")
    print(f"{len(paths)} file(s) checked, {bad} image link(s) not on the live site")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
