import os
from PIL import Image
import sys
from pathlib import Path

def create_responsive_sizes(img, base_name, output_dir, sizes):
    """Create multiple sizes of the same image for responsive design"""
    responsive_images = {}
    for size in sizes:
        width, height = size
        resized = img.copy()
        resized.thumbnail((width, height), Image.Resampling.LANCZOS)
        
        # Save as JPEG
        jpeg_path = os.path.join(output_dir, f"{base_name}_{width}w.jpg")
        resized.save(jpeg_path, 'JPEG', quality=85, optimize=True, progressive=True)
        
        # Save as WebP
        webp_path = os.path.join(output_dir, f"{base_name}_{width}w.webp")
        resized.save(webp_path, 'WEBP', quality=85, method=6)
        
        responsive_images[width] = {
            'jpeg': jpeg_path,
            'webp': webp_path
        }
    
    return responsive_images

def optimize_image(input_path, output_dir, quality=85):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Get base filename without extension
            base_name = Path(input_path).stem
            
            # Define responsive sizes (width, height)
            sizes = [
                (300, 300),  # Small
                (600, 600),  # Medium
                (900, 900),  # Large
                (1200, 1200) # Extra large
            ]
            
            # Create responsive versions
            responsive_images = create_responsive_sizes(img, base_name, output_dir, sizes)
            
            # Save original size optimized versions
            jpeg_path = os.path.join(output_dir, f"{base_name}.jpg")
            webp_path = os.path.join(output_dir, f"{base_name}.webp")
            
            # Save as JPEG
            img.save(jpeg_path, 
                    'JPEG',
                    quality=quality, 
                    optimize=True, 
                    progressive=True)
            
            # Save as WebP
            img.save(webp_path, 
                    'WEBP',
                    quality=quality,
                    method=6)  # Higher compression
            
            # Get file sizes
            original_size = os.path.getsize(input_path)
            optimized_size = os.path.getsize(jpeg_path)
            webp_size = os.path.getsize(webp_path)
            
            # Calculate savings
            savings = (original_size - optimized_size) / original_size * 100
            webp_savings = (original_size - webp_size) / original_size * 100
            
            print(f"\nOptimized: {os.path.basename(input_path)}")
            print(f"Original size: {original_size/1024:.1f}KB")
            print(f"Optimized JPEG size: {optimized_size/1024:.1f}KB (Savings: {savings:.1f}%)")
            print(f"WebP size: {webp_size/1024:.1f}KB (Savings: {webp_savings:.1f}%)")
            print("Responsive versions created:")
            for size, paths in responsive_images.items():
                print(f"- {size}w: {os.path.basename(paths['jpeg'])} and {os.path.basename(paths['webp'])}")
            
            return {
                'original': input_path,
                'optimized': jpeg_path,
                'webp': webp_path,
                'responsive': responsive_images
            }
            
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")
        return None

def generate_html_template(image_data):
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Optimized Images</title>
    <link rel="stylesheet" href="/static/css/optimized-images.css">
</head>
<body>
    <div class="image-grid">
"""
    
    for img_data in image_data:
        html_template += f"""
        <div class="image-container">
            <picture>
                <source type="image/webp" srcset="{img_data['webp_path']}">
                <img class="optimized-image" 
                     data-src="{img_data['jpg_path']}"
                     data-webp="{img_data['webp_path']}"
                     alt="{img_data['name']}"
                     loading="lazy">
            </picture>
        </div>
"""
    
    html_template += """
    </div>
    <script src="/static/js/image-loader.js"></script>
</body>
</html>
"""
    
    return html_template

def main():
    # Input and output directories
    input_dir = 'static/images'
    output_dir = 'static/images/optimized'
    
    # Supported image formats
    supported_formats = ('.jpg', '.jpeg', '.png')
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each image and generate HTML
    html_output = []
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_dir, filename)
            image_data = optimize_image(input_path, output_dir)
            if image_data:
                html_output.append(generate_html_template(image_data))
    
    # Save HTML template
    if html_output:
        with open(os.path.join(output_dir, 'image_templates.html'), 'w') as f:
            f.write("\n".join(html_output))
        print("\nHTML templates have been generated in image_templates.html")

if __name__ == "__main__":
    main() 