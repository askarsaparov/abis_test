from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        abort(400, 'No file part')

    file = request.files['file']

    if file.filename == '':
        abort(400, 'No selected file')

    # Binar ma'lumotni o'qish
    file_data = file.read()

    # Binar ma'lumotni fayl sifatida saqlash
    with open('uploaded_file.bin', 'wb') as f:
        f.write(file_data)

    return 'File successfully uploaded', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
