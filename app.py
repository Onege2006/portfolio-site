from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)



# === Страницы ===
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certificate')
def certificate():
    return render_template('certificate.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        conn = sqlite3.connect('messages.db')
        c = conn.cursor()
        c.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()
        return redirect('/contact')
    return render_template('contact.html')

@app.route('/messages')
def messages():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    msgs = c.fetchall()
    conn.close()
    return render_template('messages.html', messages=msgs)

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    message = request.form['message']
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()
    return redirect('/contact')


# === Запуск ===
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

