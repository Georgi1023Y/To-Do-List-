from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# I will store the tasks in a list called tasks.
tasks = []


# This is the home page route.
@app.route('/', methods=["POST", "GET"])
def to_do_list():
    if request.method == "POST":
        # Gets hold of the task description that user types in the form.
        task = request.form.get("task_description")
        if task:
            # Task is added to the list I already created.
            tasks.append(task)

    # Enumerates the tasks before passing them to the template.
    enumerated_tasks = enumerate(tasks)

    return render_template('index.html', tasks=enumerated_tasks)

# Route that will be used when we want to delete some task.
@app.route('/delete-task/<int:task_index>', methods=["GET"])
def delete_task(task_index):
    # Checks if there is a task with that index in our list called tasks. If there is the task is deleted from the list.
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        # Home page is updated if we delete the task from the list in that index.
        return redirect(url_for('to_do_list'))
    else:
        # If there isn't a task in the provided index this message will be shown.
        return 'Task not found', 404


if __name__ == '__main__':
    app.run(debug=True)
