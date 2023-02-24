""" Server instance and routes """
from flask import Flask, render_template, request
from machinetranslation import translator as tr

app = Flask(__name__)


@app.route("/englishToFrench")
def eng_to_fr():
    text_to_translate = request.args.get('textToTranslate')
    translated_text = tr.english_to_french(text_to_translate)

    return translated_text


@app.route("/frenchToEnglish")
def fr_to_eng():
    text_to_translate = request.args.get('textToTranslate')
    translated_text = tr.french_to_english(text_to_translate)

    return translated_text


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
