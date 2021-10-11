from flask import Flask, render_template, request, redirect
import database as db

db.init()
app = Flask(__name__)

@app.route("/")
def index():
    list = db.list()
    return render_template("index.html", todo=list, id=1, title=2, description=3)

@app.route("/new", methods=["POST", "GET"])
def new():
    if request.method == "POST":
        task = request.form["task"]
        description = request.form["description"]
        db.register(task, description)
        return redirect("/")

    return render_template("form.html", title="New Task", headline="list.append(new)", button=".addTask()")

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    list = db.getData(id)
    if request.method == "POST":
        task = request.form["task"]
        description = request.form["description"]
        db.updateTitle(id, task)
        return redirect("/")

    return render_template("form.html", title="Edit Task", id=id, headline="list.insert(edit)", button=".saveTask()", task_val=list[2], desc_val=list[3])

@app.route("/delete/<int:id>")
def delete(id):
    db.delete(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(port=5500, debug=True)