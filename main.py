from flask import Flask, escape, request, render_template
from Demo.db import init_db
from models import Autor

app = Flask(__name__)
db_session = init_db()

@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/gravacoes')
def gravacoes():
    """
    Aqui deve ser implementada a listagem de categorias de gravações
    """
    categorias = []
    render_template('gravacoes.html', categorias=categorias)
    
@app.route('/gravacoes/<categoria>')
def categoria(categoria):
    """
    Aqui deve ser implementada a listagem de gravações
    """
    categoria = None
    render_template('categoria.html', categoria=categoria)


@app.route('/autores')
def autores():
    """
    Aqui deve ser implementada a listagem de autores
    """
    autores = db_session.query(Autor).all()
    
    return render_template('autores.html', autores=autores)
    

@app.route('/autores/<pk>')
def autor(pk):
    """
    Aqui devem ser implementados os detalhes do autor
    """
    autores = db_session.query(Autor).filter(Autor.id_autor == pk)[0]
    return render_template('autor.html', autor=autores)
    
    
