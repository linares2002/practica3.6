from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route("/dos", methods=["GET"])
def dos():
    return render_template("dos.html")


@app.route("/tres", methods=["GET"])
def tres():
    return render_template("tres.html")


@app.route("/index/<nombre>/<apellidos>")
def index(nombre, apellidos):
    return render_template("index.html", nom=nombre, ape=apellidos)


@app.route("/envio", methods=["POST"])
def envio():
    connection = pymysql.connect(host='db',
                                 user='root',
                                 password='cloud2023',
                                 database='medidas')
    a = request.form.get("a")
    b = request.form.get("b")
    topic = "insert into medidas.test(uno, dos) values({0},{1})".format(a, b)
    with connection.cursor() as cursor:
        connection.cursor().execute(topic)
        connection.commit()
    topic = "select * from medidas.test"
    with connection.cursor() as cursor:
        cursor.execute(topic)
        result = cursor.fetchall()
        for res in result:
            print("{0}, {1}, {2}".format(res[0], res[1], res[2]))
    connection.close()
    return render_template("envio.html", dato1=a, dato2=b)


app.run(host="0.0.0.0")



