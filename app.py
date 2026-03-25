from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = "secret_key_for_flash_messages"

tasks = []

# Load compliments from file
with open('compliments.txt') as f:
    compliments = [line.strip() for line in f.readlines()]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form.get('task')
        if task_content:
            tasks.append({'task': task_content, 'done': False})
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

@app.route('/complete/<int:task_id>')
def complete(task_id):
    tasks[task_id]['done'] = not tasks[task_id]['done']
    if tasks[task_id]['done']:
        # Show a random compliment when task is completed
        flash(random.choice(compliments))
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
