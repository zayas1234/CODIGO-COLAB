from flask import Flask, render_template, request
import os
import fitz  # PyMuPDF

app = Flask(__name__)


def count_lines_words_chars(file_path):
    lines = 0
    words = 0
    chars = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines += 1
            words += len(line.split())
            chars += len(line)
    return {
        'lines': lines,
        'words': words,
        'characters': chars
    }

def create_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None

def append_to_file(file_path, content):
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content + "\n")
    except FileNotFoundError:
        return None

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def leer_pdf(ruta_pdf):
    texto = ""
    with fitz.open(ruta_pdf) as pdf:
        for pagina in pdf:
            texto += pagina.get_text()
    return texto

@app.route('/', methods=['GET', 'POST'])
def index():
    contenido_archivo = ""
    contenido_pdf = ""
    stats = None

    if request.method == 'POST':
        if 'archivo_texto' in request.files:
            archivo_texto = request.files['archivo_texto']
            if archivo_texto and archivo_texto.filename.endswith('.txt'):
                ruta_texto = f'temp/{archivo_texto.filename}'
                archivo_texto.save(ruta_texto)
                contenido_archivo = read_file(ruta_texto)
                stats = count_lines_words_chars(ruta_texto)

        elif 'archivo_pdf' in request.files:
            archivo_pdf = request.files['archivo_pdf']
            if archivo_pdf and archivo_pdf.filename.endswith('.pdf'):
                ruta_pdf = f'temp/{archivo_pdf.filename}'
                archivo_pdf.save(ruta_pdf)
                contenido_pdf = leer_pdf(ruta_pdf)

    return render_template('index.html', contenido_archivo=contenido_archivo, contenido_pdf=contenido_pdf, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
