from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Vercel!"

# 移除这部分，因为Vercel会自动处理
if __name__ == '__main__':
    app.run()


