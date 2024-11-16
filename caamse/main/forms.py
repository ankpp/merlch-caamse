from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import FieldList
from wtforms import Form
from wtforms import FormField
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import EqualTo
from wtforms.validators import InputRequired
from wtforms.validators import Length
from wtforms.validators import Regexp


class BaseForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class IndexForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)