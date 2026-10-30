
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    dados = int(request.form["dados"])
    transparencia = int(request.form["transparencia"])
    vies = int(request.form["vies"])
    seguranca = int(request.form["seguranca"])
    supervisao = int(request.form["supervisao"])

    total = dados + transparencia + vies + seguranca + supervisao

    if total <= 0:
        nivel = "BAIXO"
        recomendacao = (
            "O risco identificado é baixo. "
            "Mantenha os cuidados com privacidade, "
            "segurança e supervisão humana."
        )

    elif total <= 6:
        nivel = "MÉDIO"
        recomendacao = (
            "Revise os pontos que precisam de melhoria. "
            "Reforce a proteção dos dados, a transparência "
            "e a verificação de possíveis vieses."
        )

    else:
        nivel = "ALTO"
        recomendacao = (
            "O sistema exige uma revisão cuidadosa antes "
            "de ser utilizado. Avalie os riscos, reforce "
            "a segurança e garanta supervisão humana."
        )

    return render_template(
        "index.html",
        resultado=total,
        nivel=nivel,
        recomendacao=recomendacao
    )


if __name__ == "__main__":
    app.run(debug=True)
