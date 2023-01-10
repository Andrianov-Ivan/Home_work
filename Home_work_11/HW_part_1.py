from flask import Flask, request, render_template
import os



app = Flask(__name__)

@app.route('/')
def page_index():

    page_content = f""" 
    <h1>Андрианов Иван Николаевич</h1>
    
    <img src="./1.jpg" width="300" />
    <p><strong>Привет я пользуюсь <mark>GitHub</mark> и вот ссылка на</strong> 
    <th id="about-color"> </th>
    <a href="https://github.com/Andrianov-Ivan" class="site" target="_blank">мою станицу</a></p> 
    <a href="github.com/Andrianov-Ivan.html"></a>
    <p>На этой странице будут публиковаться <ins>мои проекты</ins></p>
    <p>Проекты будут <em>обновляться систематически</em></p>
    <p><del>Обо всех обновлениях</del></p>
    <div>
    <th id="about-color"> </th>
    <br>Для обращений пишите на мой <a href="https://andreyanovi@yandex.ru" class="site" target="_blank">
    электронный адрес</a></br>
    <a href="andreyanovi@yandex.ru.html"></a>
    </div>
    """

    return page_content


app.run()
