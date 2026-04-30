from flask import Flask, request

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    page = "<h1>My Notes App</h1>"
    
    page += """
    <form method='POST'>
        <input type='text' name='note' placeholder='Write a note'>
        <button type='submit'>Add</button>
    </form>
    """

    for note in notes:
        page += f"<p>{note}</p>"

    return page

if __name__ == "__main__":
    app.run(debug=True)