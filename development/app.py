#
# Requires Flask to be installed
#
import os
from flask import Flask, render_template

# Create the application
app = Flask('Galleria', static_folder="../",
    static_url_path="/static", template_folder="./")

# Set the directory where images are stored
image_dir = os.path.join(os.path.dirname(__file__), 'images')


@app.route("/")
def index():
    """
    Run this function for the index page of the web application.

    Images on the filesystem are expected to be in the format for thumbnails:
        image#-200px.jpg

    And this format for large size:
        image#-1600px.jpg
    """
    images = {}
    for filename in os.listdir(image_dir):
        # if the filename does not start with image, it's not a 
        # valid gallery image
        if not filename.startswith('image'):
            continue

        # let's find the scale size
        name, size = filename.split('-')
        if name not in images:
            images[name] = {}
        if size.startswith('200px'):
            # thumbnail
            images[name]['thumb'] = filename
        else:
            # full size
            images[name]['image'] = filename
    # render the app.html template with the image data we gathered
    return render_template('app.html', images=images.values())

if __name__ == "__main__":
    app.run()
