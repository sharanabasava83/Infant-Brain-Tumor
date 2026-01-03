from flask import *
import os
from werkzeug.utils import secure_filename
import label_image

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)

@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')

 
  
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = load_image(file_path)
        result = result.title()
        d = {"Glioma Tumor":" Glioma is a type of tumor that occurs in the brain and spinal cord. Gliomas begin in the gluey supportive cells (glial cells) that surround nerve cells and help them function. Three types of glial cells can produce tumors.",
        "Meningioma Tumor":" → A meningioma is a tumor that forms in your meninges, which are the layers of tissue that cover your brain and spinal cord. They're usually not cancerous (benign), but can sometimes be cancerous (malignant). Meningiomas are treatable.",
        "No Tumor":" → Be Happy, There is was No Sign of Any Tumor in your MRI",
        "Pituitary Tumor":" → A pituitary tumor is a tumor that forms in the pituitary gland near the brain that can cause changes in hormone levels in the body. This illustration shows a smaller tumor (microadenoma). Pituitary tumors are abnormal growths that develop in your pituitary gland."}
        result = result+d[result]
        #result2 = result+d[result]
        #result = [result]
        #result3 = d[result]        
        print(result)
        #print(result3)
        os.remove(file_path)
        return result
        #return result3
    return None

if __name__ == '__main__':
    app.run()