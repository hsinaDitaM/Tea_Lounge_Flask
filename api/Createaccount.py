from flask_wtf import Form
from CreateAccount import name,uid,password,phone_num,date
from wtforms.validators import ValidationError, DataRequired
class registration(input):
    username = name(label="Username",validator=[DataRequired()])
    userid = uid(label="id",validator=[DataRequired()])
    password = password(label="Password",validator=[DataRequired()])
    phone = phone_num(label="PhoneNumber",validator=[DataRequired()])
    birthday = date(label="Birthday",validator=[DataRequired()])
