from init import *
from flask import render_template, session, send_file, redirect, request, url_for, g
from flask_sqlalchemy import SQLAlchemy
from models import *
from io import BytesIO


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user_page')
def user_page():
    return render_template("user_page.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    newFile = Files(name=file.filename, data = file.read())
    db.session.add(newFile)
    db.session.commit()
    status = "File: " + file.filename + " was saved!"
    return render_template("user_page.html", status=status)

@app.route('/download', methods=['POST'])
def download():
    download_file = request.form['download_file']
    download_file = download_file.strip()
    file_data = Files.query.filter_by(name=download_file).first()
    if file_data:
        return send_file(BytesIO(file_data.data), attachment_filename=download_file, as_attachment=True)
    else:
        stauts = "No file: " + download_file + " found!"
        return render_template("user_page.html", status=stauts)


@app.route('/guest', methods=['GET', 'POST'])
def guest():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['user'] != '':
            session['user'] = request.form['user']
            return redirect(url_for('chatroom'))
    return render_template('guest.html')


@app.route('/chatroom')
def chatroom():
    user = session.get('user', '')
    if user == '':
        return redirect(url_for('.index'))
    return render_template('chatroom.html')


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('index.html')


