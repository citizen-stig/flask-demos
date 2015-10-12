import random
from flask import Flask, render_template
from models import db, User, \
    WorkType, AuthorRate
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://flask:flask@localhost:5432/flask'

db.app = app
db.init_app(app)


@app.route('/')
def index():
    for i in range(5):
        some_key = str(random.randint(1000000, 9000000))
        work_type = WorkType(name='work_type' + some_key)
        db.session.add(work_type)
        for j in range(8):
            some_other_key = str(random.randint(1000000, 9000000))
            user = User(username='user' + some_key + some_other_key)
            db.session.add(user)
            rate = AuthorRate(
                amount=1 + random.random(),
                work_type=work_type,
                author=user)
            db.session.add(rate)
    db.session.commit()
    print('========')
    rates = AuthorRate.query
    print(rates)
    rates = rates.limit(10)
    print('+++++++')
    print(rates)
    print('=========')
    rates = rates.offset(0)
    return render_template('limit.html', rates=rates)


if __name__ == '__main__':
    db.create_all()
    app.run(port=5000, host='0.0.0.0')
