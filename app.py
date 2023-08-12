from flask import Flask, request,send_file,render_template
from http import HTTPStatus
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST','PUT','DELETE'])
def upload():
    image_file = request.files['image']
    
    image_path = 'uploads/' + image_file.filename
    image_file.save(image_path)
    
    

    # Call your Python function here, passing the image path as an argument
    output_path=compress_image(image_path,image_file.filename)
    print("Your file is compressed and is downloading...")
    
    send_file(output_path, as_attachment=True)
    return send_file(output_path, as_attachment=True),os.remove(output_path),os.remove(image_path)
    #return 'Image uploaded and processed successfully!'
    

def compress_image(image_path,filename):
    image = Image.open(image_path)
    output_path="uploads/compressed"+filename
    image.save(output_path, optimize=True, quality=50)
    return output_path

# Example usage
#image_path = "/Users/atul/Desktop/image compression/image.jpg"  # Replace with your image file path
#output_path = "/Users/atul/Desktop/IMG1.jpeg"  # Replace with desired output path
#compression_level = 70  # Adjust the value as desired (0-100)





if __name__ == '__main__':
    app.run(debug=True)
