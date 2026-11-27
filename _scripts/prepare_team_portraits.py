"""Prepare the Team page portraits from the unmodified source photographs.

Run from the repository root with Python 3 and Pillow installed:
    python3 _scripts/prepare_team_portraits.py

Each crop is individually chosen after correcting EXIF orientation. Aim for a
centred head-and-shoulders portrait, eyes around 40% of the image height, and
some space above the hair. Keep the original colours and background. When
adding a portrait, review it in both the square and wide website crops.
"""

from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "assets/images/team/portraits"
SIZE = 640

# Source path, output filename, and square crop (left, top, side) in pixels.
PORTRAITS = (
    (
        "assets/images/bio/20230610-profile-00042.jpeg",
        "pablo-capilla-lasheras.jpg",
        (104, 10, 640),
    ),
    (
        "assets/images/team/Patricia_García_Florencio.jpeg",
        "patricia-garcia-florencio.jpg",
        (35, 179, 760),
    ),
    (
        "assets/images/team/Valentina_Kaid.jpeg",
        "valentina-kaid-soto.jpg",
        (385, 545, 500),
    ),
    (
        "assets/images/team/Vera_García.jpg",
        "vera-garcia-perez.jpg",
        (996, 610, 740),
    ),
)


def main():
    DESTINATION.mkdir(parents=True, exist_ok=True)
    for source, filename, (left, top, side) in PORTRAITS:
        with Image.open(ROOT / source) as original:
            image = ImageOps.exif_transpose(original)
            right, bottom = left + side, top + side
            if left < 0 or top < 0 or right > image.width or bottom > image.height:
                raise ValueError(f"Crop exceeds source dimensions: {source}")
            portrait = image.crop((left, top, right, bottom)).convert("RGB")
            portrait = portrait.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
            portrait.save(
                DESTINATION / filename,
                quality=88,
                optimize=True,
                progressive=True,
                icc_profile=image.info.get("icc_profile"),
            )
            print(f"Prepared {filename} ({SIZE} × {SIZE})")


if __name__ == "__main__":
    main()
