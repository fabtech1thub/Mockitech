from PIL import Image

def resize_logo(input_path, output_path, size_factor=2):
    # Open the image
    with Image.open(input_path) as img:
        # Calculate new size
        new_width = int(img.width * size_factor)
        new_height = int(img.height * size_factor)
        
        # Resize image
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Save the resized image
        resized_img.save(output_path, quality=95)
        print(f"Logo resized successfully! New size: {new_width}x{new_height}")

if __name__ == "__main__":
    input_path = "static/images/MOCKITECH.png"
    output_path = "static/images/MOCKITECH_large.png"
    resize_logo(input_path, output_path) 