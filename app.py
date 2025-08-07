from flask import Flask, render_template, request
from openrouter_utils import call_openrouter
from prompts import code_explanation_prompt, dsa_question_prompt, problem_generator_prompt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        feature = request.form.get("feature")
        user_input = request.form.get("user_input")
        topic = request.form.get("topic")
        difficulty = request.form.get("difficulty")

        if feature == "code_explain":
            prompt = code_explanation_prompt(user_input)
        elif feature == "dsa_question":
            prompt = dsa_question_prompt(user_input)
        elif feature == "problem_gen":
            prompt = problem_generator_prompt(topic, difficulty)
        else:
            prompt = "Invalid feature selected."

        response = call_openrouter(prompt)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
