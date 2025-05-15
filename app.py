from flask import Flask
from flask import render_template,request,redirect
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html",tasks=tasks)


@app.route('/about')
def about():
    return "Hello Yash Jain here,this is made using Flask"

tasks=[]

@app.route('/delete', methods=['POST'])
def delete_task():
    task_to_delete = request.form.get('task')
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
    return redirect('/')

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task') #get task
    if task and task.strip(): #check list
        tasks.append(task.strip())  # Add clean task to the list
    # Redirect to home page to show updated tasks
    return redirect('/')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task and new_task.strip():
            tasks[index] = new_task.strip()
        return redirect('/')
    else:
        task_to_edit = tasks[index]
        return render_template('edit.html', index=index, task=task_to_edit)
        
if __name__ == '__main__':
    app.run(debug=True)
