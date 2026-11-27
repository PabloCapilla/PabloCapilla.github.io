"""Create web-sized About gallery images, preserving the source photographs.

Run with Python 3 and Pillow installed:
    python3 _scripts/prepare_bio_gallery.py

Correct orientation, retain original framing and colour profiles, and keep the
photographer credit in the three new images as well as in the page caption.
"""

from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/images/bio"
DESTINATION = SOURCE / "gallery"
PHOTOGRAPHER = "Daniel Leopoldsberger"
PHOTOS = (
    ("20230610-profile-00042.jpeg", "profile.jpg", None),
    ("tagging_scops_owls_Daniel_Leopoldsberger (23).JPG", "scops-owl-nestbox.jpg", PHOTOGRAPHER),
    ("tagging_scops_owls_Daniel_Leopoldsberger (24).JPG", "scops-owl-fieldwork.jpg", PHOTOGRAPHER),
    ("tagging_scops_owls_Daniel_Leopoldsberger (52).JPG", "scops-owl-night-fieldwork.jpg", PHOTOGRAPHER),
)


def main():
    DESTINATION.mkdir(parents=True, exist_ok=True)
    for source, filename, photographer in PHOTOS:
        with Image.open(SOURCE / source) as original:
            image = ImageOps.exif_transpose(original).convert("RGB")
            image.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            credit = Image.Exif()
            if photographer:
                credit[315] = photographer
                credit[33432] = f"Copyright {photographer}"
            image.save(
                DESTINATION / filename,
                quality=85,
                optimize=True,
                progressive=True,
                icc_profile=image.info.get("icc_profile"),
                exif=credit,
            )
            print(f"Prepared {filename}: {image.width} × {image.height}")


if __name__ == "__main__":
    main()
