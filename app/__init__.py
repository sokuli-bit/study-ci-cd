import os

import openai
from flask import Flask, redirect, render_template, request, url_for

from app import gpt, tool

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
print("무야호~")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        print(tool.sub(45, 9))
        characteristic = request.form["characteristic"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=gpt.generate_prompt(characteristic),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()
