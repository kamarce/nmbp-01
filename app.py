from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect("dbname=FTS_db user=postgres password=postgres")
cur = conn.cursor();
cur.execute('SELECT title from movie')
print(cur.fetchall())


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
