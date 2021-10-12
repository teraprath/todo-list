from flask import Flask, render_template, request, redirect, url_for
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
    if not db.check(id):
        return redirect('404')
    list = db.getData(id)
    if request.method == "POST":
        task = request.form["task"]
        description = request.form["description"]
        db.updateTitle(id, task)
        db.updateDescription(id, description)
        return redirect("/")

    return render_template("form.html", title="Edit Task", id=id, headline="list.insert(edit)", button=".saveTask()", task_val=list[2], desc_val=list[3])

@app.route("/delete/<int:id>")
def delete(id):
    if not db.check(id):
        return redirect('404')
    db.delete(id)
    return redirect("/")

@app.route("/test")
def test():
    return render_template("test.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(port=5500, debug=True)