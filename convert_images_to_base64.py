#!/usr/bin/env python3
import base64
import re

# Read HTML file
with open('PRESENTAZIONE_PDF.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Convert images to base64
images = {
    'screenshot_home.png': 'file:///Users/colincetcheussieumendji/Desktop/COURSES%20UNIMORE/Technologie_Web/TaskFlow/screenshot_home.png',
    'screenshot_new_project.png': 'file:///Users/colincetcheussieumendji/Desktop/COURSES%20UNIMORE/Technologie_Web/TaskFlow/screenshot_new_project.png',
    'screenshot_dashboard.png': 'file:///Users/colincetcheussieumendji/Desktop/COURSES%20UNIMORE/Technologie_Web/TaskFlow/screenshot_dashboard.png'
}

for img_file, img_path in images.items():
    # Read and encode image
    with open(img_file, 'rb') as f:
        img_data = base64.b64encode(f.read()).decode('utf-8')

    # Create data URL
    data_url = f'data:image/png;base64,{img_data}'

    # Replace in HTML
    html_content = html_content.replace(img_path, data_url)
    print(f'✓ Converted {img_file} to base64')

# Write updated HTML
with open('PRESENTAZIONE_PDF_WITH_IMAGES.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('\n✓ HTML file with embedded images created: PRESENTAZIONE_PDF_WITH_IMAGES.html')
