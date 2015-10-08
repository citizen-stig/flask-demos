from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.model.form import InlineFormAdmin
from sqlalchemy import inspect
from sqlalchemy.orm import class_mapper
from models import db, User, UserNote
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'testing_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.db'

db.app = app
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


class ModelFormWithAuthorship(InlineFormAdmin):

    def on_model_change(self, form, model):
        user = User.query.first()
        print('++++++')
        print(model.body)
        hista = inspect(model).attrs.body.history
        print(hista.has_changes())
        inspr = inspect(model)
        attrs = class_mapper(model.__class__).column_attrs  # exclude relationships
        for attr in attrs:
            hist = getattr(inspr.attrs, attr.key).history
            print(attr.key, hist.has_changes())
        print('++++')

class UserModelView(ModelView):
    inline_models = (ModelFormWithAuthorship(UserNote),)


admin = Admin(app, url='/admin', name='MyAdmin', template_mode='bootstrap3')
admin.add_view(UserModelView(User, db.session))


if __name__ == '__main__':
    db.create_all()
    app.run(port=5151)
