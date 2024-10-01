from flask import Flask, render_template, url_for, send_file, abort
from PIL import Image
import os
from io import BytesIO

app = Flask(__name__)

# Directories
IMAGE_DIR = 'static/images'

# Sample product data
products = [
    {
        'id': 1,
        'name': 'Beautiful Landscape',
        'images': ['image_1.jpg', 'image_3.jpg'],
        'description': 'A stunning view of the mountains.'
    },
    {
        'id': 2,
        'name': 'Serene Beach',
        'images': ['image_2.jpg', 'image_4.jpg'],
        'description': 'A peaceful beach during sunset.'
    },
    # Add more products as needed
]

# List of background images
backgrounds = [
    {'id': 1, 'filename': 'background_1.jpg'},
    {'id': 2, 'filename': 'background_2.jpg'},
    # Add more backgrounds as needed
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product, backgrounds=backgrounds)
    else:
        return "Product not found", 404

@app.route('/combined_image/<image_filename>/<int:background_id>')
def combined_image(image_filename, background_id):
    # Find background
    background = next((b for b in backgrounds if b['id'] == background_id), None)

    if not background:
        abort(404)

    image_path = os.path.join(IMAGE_DIR, image_filename)
    background_path = os.path.join(IMAGE_DIR, background['filename'])

    try:
        with Image.open(background_path) as bg_img, Image.open(image_path) as prod_img:
            # Ensure images are in RGBA mode
            if bg_img.mode != 'RGBA':
                bg_img = bg_img.convert('RGBA')
            if prod_img.mode != 'RGBA':
                prod_img = prod_img.convert('RGBA')

            # Resize product image to fit
            prod_img.thumbnail((bg_img.width // 2, bg_img.height // 2))
            # Calculate position
            x = (bg_img.width - prod_img.width) // 2
            y = (bg_img.height - prod_img.height) // 2
            # Paste product image onto background
            bg_img.paste(prod_img, (x, y), prod_img)
            # Save to BytesIO
            img_io = BytesIO()
            bg_img.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png')
    except Exception as e:
        print(f"Error combining images: {e}")
        abort(500)

if __name__ == '__main__':
    app.run(debug=True)
