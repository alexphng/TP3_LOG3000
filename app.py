"""
Application web pour une calculatrice simple.
Ce fichier gère les routes HTTP et affiche l'interface
Il reçoit les expressions mathématiques envoyées par l'utilisateur 
et effectue le calcul au moyen du module operators.py
"""
from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Calcule l'opération de l'expression mathématique
    simple contenant deux nombres et un opérateurs donnée en paramètre
    Args:
        expr (str): expression mathématique sous forme de chaîne.
    Returns: 
        float: résultat de l'expression mathématique
    Raises:
        ValueError: Si l'expression est vide, mal formatée,
        contient plusieurs opérateurs ou des valeurs non numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Affiche l'interface de la calculatrice et gère la soumission d'une expression
    Méthodes HTTP:
        GET: affiche la page d'accueil
        POST: récupère l'expression et essai de la calculer.
    Returns: 
        une page html pour l'interface de la calculatrice
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)