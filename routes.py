
from flask import Blueprint, render_template
from controllers.users import add_user_function
from config import config
from my_logging import logger
main= Blueprint('main',__name__)



@main.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@main.route('/add-user', methods=['GET','POST'])
def add_user():
    logger.debug("This is a debug messagefdfgf.")
    print(config.DATABASE_URL)
    # data= add_user_function()
    # print('data')
    return render_template("users.html", data=[])
