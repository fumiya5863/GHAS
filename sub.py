from flask import Flask, request, render_template_string
import html

app = Flask(__name__)

@app.route("/")
def index():
    user_input = request.args.get("input", "")
    safe_user_input = html.escape(user_input)
    return render_template_string(f"<p>入力された内容: {safe_user_input}</p>")

if __name__ == "__main__":
    app.run(debug=True)