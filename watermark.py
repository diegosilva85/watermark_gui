from PIL import Image, ImageFont, ImageDraw, ImageTk


class Watermark:
    def __init__(self, image_path, text):
        self.image = Image.open(image_path)
        aspect_ratio = self.image.size[0] / self.image.size[1]
        target_width = min(700, int(700 * aspect_ratio))
        target_height = min(700, int(700 / aspect_ratio))
        resized_image = self.image.resize((target_width, target_height))
        draw = ImageDraw.Draw(resized_image)
        draw_original = ImageDraw.Draw(self.image)
        font_size = int(self.image.size[0] / 10)
        font = ImageFont.truetype(font="arial.ttf", size=font_size)
        watermark_color = (128, 128, 128, 128)
        draw.text((10, 10), text, font=font, fill=watermark_color)
        draw_original.text((10, 10), text, font=font, fill=watermark_color)
        self.image.convert("RGB")
        self.image_tk = ImageTk.PhotoImage(resized_image)

