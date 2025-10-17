# 1. Importações
from flask import Flask, render_template, request, redirect, url_for, flash
from core.logica import CatalogoPlantas

# 2. Inicialização da Aplicação
app = Flask(__name__)
app.secret_key = 'chave-secreta'

# 3. Instância Única do Sistema
logica = CatalogoPlantas()

# 4. Rota para lista de plantas
@app.route('/')
def lista_plantas():
    lista_plantas = logica.get_plantas()
    return render_template("lista_plantas.html", plantas = lista_plantas)

# 5. Rota para adicionar plantas
@app.route('/add_plantas', methods=['GET','POST'])
def add_plantas():

    if request.method == 'POST':
        # Pega os dados do formulário
        nome = request.form['nome']
        especie = request.form['especie']
        ambiente = request.form['ambiente']
        origem = request.form['origem']
        regar = request.form['regar']
        imagem = request.form['imagem']

        # Chama o método em logica para adicionar e salvar a planta
        sucesso = logica.add_planta(nome, especie, ambiente, origem, regar, imagem)

        if sucesso:
            # Envia uma mensagem de sucesso para o usuário
            flash("Planta cadastrada com sucesso!", "success")
            return redirect(url_for('lista_plantas'))
        else:
            flash("Essa espécie já está cadastrada no sistema. Por favor, tente novamente.", "error")
            return redirect(url_for('add_plantas'))


    return render_template("add_plantas.html")

# 6. Inicando programa
if __name__ == "__main__":
    app.run(debug=True)