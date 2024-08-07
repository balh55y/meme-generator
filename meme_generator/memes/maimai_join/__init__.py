from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def maimai_join(images: list[BuildImage], texts, args):
    frame = BuildImage.open(img_dir / "0.png")

    def make(img: BuildImage) -> BuildImage:
        img = img.convert("RGBA").square().resize((400, 400))
        return frame.copy().paste(img, (50, 50), alpha=True, below=True)

    return make_jpg_or_gif(images[0], make)


add_meme(
    "maimai_join", maimai_join, min_images=1, max_images=1, keywords=["旅行伙伴加入"]
)
