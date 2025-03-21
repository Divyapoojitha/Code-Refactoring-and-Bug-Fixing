from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
        # Redirect to avoid form resubmission on page refresh
        return redirect(url_for('index'))
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
