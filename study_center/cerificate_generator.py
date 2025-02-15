from PIL import Image, ImageDraw, ImageFont
import os

class Certificates:
    @staticmethod
    def generateCertificate(path, text, x, y, text_size, thickness):
        img = Image.open(f"{os.getcwd().replace('\\', '/')}{path}")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("motserrat.ttf", size=int(text_size))
        dims = Certificates.get_text_dimensions(text, font)
        draw.text(xy=(x-dims[0]/2, y-dims[1]/2,), text=text, fill=(0, 0, 0), font=font, stroke_width=thickness)
        img.save(f"{os.getcwd().replace('\\', '/')}/media/certificates/{rf"{x}_{y}_{text_size}_{thickness}_{text}_{path[path.rindex('/')+1:]}".replace('/', '__').replace('\n', '__').replace('\\', '__')}.png".replace(' ', '-'))
        return f"/media/certificates/{rf"{x}_{y}_{text_size}_{thickness}_{text}_{path[path.rindex('/')+1:]}".replace('/', '__').replace('\n', '__').replace('\\', '__')}.png".replace(' ', '-')

    @staticmethod
    def get_text_dimensions(text_string, font):
        ascent, descent = font.getmetrics()

        text_width = font.getmask(text_string).getbbox()[2]
        text_height = font.getmask(text_string).getbbox()[3] + descent

        return (text_width, text_height)