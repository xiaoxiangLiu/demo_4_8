from flask import Flask, request

app = Flask(__name__)


@app.route('/index')
def index():
    print(request.path)  # 打印路径，/index
    print(request.url)  # 打印url，http://127.0.0.1:5000/index
    print(request.method)  # request的请求方法
    print(request.args.get(key="123"))  # 操作url中提交的参数可以使用这个方法（?key=value)取value
    print(request.form)  # 从POST和PUT请求解析的 MultiDict
    print(request.values)  # CombinedMultiDict，内容是form和args。 可以使用values替代form和args
    print(request.cookies)  # 获取request的cookie
    print(request.headers)  # request的请求头
    print(request.data)  # 包含了请求的数据，并转换为字符串
    print(request.files)  # 请求的发送的文件
    print(request)  # 请求本身
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
