import db
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "clave_super_secreta"


db.init_db()

@app.route("/")
def home():
    tareas = db.get_tareas()
    return render_template("index.html", tareas = tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    texto = request.form["texto"]

    if db.agregar_tarea(texto):
        flash("Tarea agregada correctamente ✅")
    else:
        flash("Texto inválido ❌")

    return redirect("/")


@app.route("/terminar/<int:id>", methods=["POST"])
def terminar(id):
    if db.terminar_tarea(id):
        flash("Tarea marcada como hecha ✅")
    else:
        flash("No se encontró esa tarea ❌")

    return redirect("/")


@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    if db.eliminar_tarea(id):
        flash("Tarea eliminada 🗑️")
    else:
        flash("No se encontró esa tarea ❌")

    return redirect("/")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    tarea = db.get_tarea_por_id(id)

    if tarea is None:
        return "Tarea no encontrada", 404

    if request.method == "POST":
        nuevo_texto = request.form["texto"]
        db.editar_tarea(id, nuevo_texto)
        return redirect("/")

    return render_template("editar.html", tarea=tarea)


if __name__ == "__main__":
    app.run(debug = True)