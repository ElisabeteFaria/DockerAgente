from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import sys
import yaml

app = Flask(__name__)

#Configurações mysql
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

#Cria objeto MySQL
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #fetch data
        noteParam = request.form
        titulo = noteParam['titulo']
        nota = noteParam['nota']
        print("titulo: ", (titulo), file=sys.stderr)
        print("nota: ", (nota),  file=sys.stderr)
        print("Primeiro", file=sys.stderr)
        cur = mysql.connection.cursor()
        print("Segundo", file=sys.stderr)
        cur.execute("INSERT INTO notas(titulo, nota) VALUES(%s, %s)", (titulo, nota))
        print("Terceiro", file=sys.stderr)
        mysql.connection.commit()
        print("Quarto", file=sys.stderr)
        cur.close()
        print("Quinto", file=sys.stderr)
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81,debug=True)
