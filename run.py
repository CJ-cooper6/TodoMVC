from backend import create_app
from flask import redirect

app = create_app()

@app.route('/redirect')
def redirect_example():
    # 使用 redirect 函数进行重定向
    return redirect('http://localhost:5173')


if __name__ == '__main__':
    app.run(debug=True)
