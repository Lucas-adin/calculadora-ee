
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html', resultado=None)


@app.route('/calcular', methods=['POST'])
def calcular():
    perguntas = [
        'dados',
        'transparencia',
        'vies',
        'seguranca',
        'supervisao'
    ]

    pontuacao_respostas = {
        'nao': 2,
        'parcial': 1,
        'sim': 0
    }

    total = 0

    for pergunta in perguntas:
        resposta = request.form.get(pergunta)

        if resposta not in pontuacao_respostas:
            return "Responda todas as perguntas corretamente.", 400

        total += pontuacao_respostas[resposta]

    if total <= 3:
        nivel = "Baixo"
        mensagem = "O sistema apresenta baixo risco ético."
        recomendacao = "Continue monitorando os critérios éticos da IA."

    elif total <= 6:
        nivel = "Médio"
        mensagem = "O sistema apresenta risco ético moderado."
        recomendacao = "Revise os critérios que precisam de melhorias."

    else:
        nivel = "Alto"
        mensagem = "O sistema apresenta alto risco ético."
        recomendacao = "Priorize a correção dos problemas identificados e realize uma nova avaliação."

    return render_template(
        'index.html',
        resultado=total,
        nivel=nivel,
        mensagem=mensagem,
        recomendacao=recomendacao
    )


if __name__ == '__main__':
    app.run(debug=True)
