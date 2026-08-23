from flask import Flask, render_template, request, redirect

app = Flask(__name__)
todos = [{"task": "להקים פייפליין ל-ArgoCD", "done": False}]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({"task": todo, "done": False})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)