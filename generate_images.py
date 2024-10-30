from PIL import Image, ImageDraw, ImageFont

# Options and basic setup
choices = ["stein", "papier", "schere", "echse", "spock"]
width, height = 200, 200  # Image size
bg_color = (255, 255, 255)  # White background
text_color = (0, 0, 0)      # Black text

# Generate an image for each choice
for choice in choices:
    # Create a blank image with white background
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Load a default font
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    # Center the text using textbbox
    text = choice.capitalize()
    text_box = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_box[2] - text_box[0], text_box[3] - text_box[1]
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # Save the image
    img.save(f"{choice}.png")
    print(f"Created {choice}.png")
