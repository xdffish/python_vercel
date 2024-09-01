from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Vercel!"

# 添加错误处理
@app.errorhandler(500)
def server_error(e):
    return "An internal error occurred: " + str(e), 500

# 移除这部分，因为Vercel会自动处理
# if __name__ == '__main__':
#     app.run()



#