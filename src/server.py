from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template
from flask.json import jsonify
from CoinInfo import CoinInfo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Aleke03072003@localhost:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coin_name =  db.Column(db.String)
    title = db.Column(db.String)
    body = db.Column(db.String)
    link =  db.Column(db.String)

    def __init__(self, coin_name, title, body, link):
        self.coin_name = coin_name
        self.title = title
        self.body = body
        self.link = link

    def __repr__(self):
        return '<Title %r>' % self.title

db.create_all()

@app.route("/coin", methods = ['POST', 'GET'])
def coin():
    if request.method == 'POST':
        coin_name = request.form['coin'].lower()

        db_articles = News.query.filter_by(coin_name = coin_name).all()

        if (db_articles):
            return render_template('form.html', articles = db_articles)

        coininfo = CoinInfo()
        articles = coininfo.get_paragraphs(coin_name)

        for article in articles:
            db.session.add(News(coin_name, article['title'], article['body'], article['link']))
        
        db.session.commit()

        return render_template('form.html', articles = articles)
       
    elif request.method == 'GET':
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)