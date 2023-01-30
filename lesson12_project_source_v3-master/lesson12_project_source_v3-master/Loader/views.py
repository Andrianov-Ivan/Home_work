import logging

from flask import Blueprint, render_template, request

from Loader.utils import save_picture

from main.views import PostHandler
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def create_new_post_page():
    return render_template('post_form.html')

@loader_blueprint.route('/post', methods=['POST'])
def create_new_post():
    picture = request.form.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return "Не все поля заполнены"
    picture_path = save_picture(picture)
    if not picture_path:
        logging.info('Заружено не изображение')
        return 'Заружено не изображение'

    post_handler = PostHandler('posts.json')
    new_post = {'pic': picture_path, 'content': content}
    post_handler.add_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
