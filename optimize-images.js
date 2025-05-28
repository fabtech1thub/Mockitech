const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const inputDir = 'static/images';
const outputDir = 'static/images/optimized';

// Create output directory if it doesn't exist
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// Get all image files
const imageFiles = fs.readdirSync(inputDir).filter(file => {
    const ext = path.extname(file).toLowerCase();
    return ['.jpg', '.jpeg', '.png', '.webp'].includes(ext);
});

// Process each image
async function optimizeImages() {
    for (const file of imageFiles) {
        const inputPath = path.join(inputDir, file);
        const outputPath = path.join(outputDir, file);

        try {
            // Get image metadata
            const metadata = await sharp(inputPath).metadata();

            // Optimize based on file type
            if (file.toLowerCase().endsWith('.png')) {
                await sharp(inputPath)
                    .png({ quality: 80, compressionLevel: 9 })
                    .toFile(outputPath);
            } else {
                await sharp(inputPath)
                    .jpeg({ quality: 80, progressive: true })
                    .toFile(outputPath);
            }

            console.log(`Optimized: ${file}`);
        } catch (error) {
            console.error(`Error processing ${file}:`, error);
        }
    }
}

optimizeImages(); 