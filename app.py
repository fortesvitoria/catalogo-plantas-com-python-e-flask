from flask import Flask, render_template
from core.logica import CatalogoPlantas

# 2. Inicialização da Aplicação
app = Flask(__name__)
app.secret_key = 'chave-secreta'

# 3. Instância Única do Sistema
logica = CatalogoPlantas()

@app.route('/')
def home():
    lista_plantas = logica.get_plantas()
    return render_template("lista_plantas.html", plantas = lista_plantas)


if __name__ == "__main__":
    app.run(debug=True)