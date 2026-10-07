from PIL import Image, ImageDraw
from os import getcwd

IMG_PATH: str = getcwd()+"/imgs"
BACKGROUND_STYLE: str = "Dark"
BORDER: int = 20

def build_wallpaper() -> None:
    try:
        background = Image.open(f"{IMG_PATH}/GarfBackground{BACKGROUND_STYLE}.png")
        comic = Image.open(f"{IMG_PATH}/GarfToday.png")
    except FileNotFoundError:
        print("Background or comic images could not be retrieved")
        img = Image.new("RGB", (800, 1280), (255, 255, 255))
        img.save("imgs/Wallpaper.png", "PNG")
        return

    wBackground, hBackground = background.size
    wComic, hComic = comic.size

    coords = ((wBackground-wComic) // 2,(hBackground-hComic) // 2)

    draw = ImageDraw.Draw(background)
    draw.rectangle(
        xy=(coords[0] - BORDER, 
            coords[1] - BORDER, 
            coords[0] + wComic + BORDER,
            coords[1] + hComic + BORDER),
        fill = (255, 255, 255),
        outline= (255, 255, 255),
        width = 0
    )
    background.paste(comic, coords)

    background.save("imgs/Wallpaper.png")
    return

if __name__ == "__main__":
    build_wallpaper()
