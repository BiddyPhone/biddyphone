from pathlib import Path
import warnings
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # Pillow may not be installed
    Image = ImageDraw = ImageFont = None


def create_logo(text: str = "BiddyPhone", *, font_path: str | None = None,
                size: tuple[int, int] = (400, 200),
                background: str = "white", font_size: int = 48,
                output_path: str = "logo.png") -> str:
    """Create a simple text-based logo image.

    Parameters
    ----------
    text: str
        Text to render.
    font_path: str | None
        Path to a .ttf font file. If ``None`` the function tries ``arial.ttf``.
    size: tuple[int, int]
        Image dimensions (width, height).
    background: str
        Background color for the image.
    font_size: int
        Size of the font used to render ``text``.
    output_path: str
        Where to save the generated image.

    Returns
    -------
    str
        Path to the saved logo image.
    """
    if Image is None:
        raise RuntimeError("Pillow is required to create logos.")

    candidate = Path(font_path) if font_path else Path("arial.ttf")
    if candidate.is_file():
        font = ImageFont.truetype(str(candidate), font_size)
    else:
        warnings.warn(
            f"Font file '{candidate}' not found. Using default font.",
            UserWarning,
        )
        font = ImageFont.load_default()

    img = Image.new("RGB", size, color=background)
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)
    draw.text(position, text, fill="black", font=font)
    img.save(output_path)
    return output_path


if __name__ == "__main__":
    # Example usage
    create_logo()
