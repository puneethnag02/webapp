from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
        return "Hello this is my first project in Designed and implemented an automated CI/CD pipeline using Jenkins and Docker on AWS EC2 to deploy a Python-based web application. Achieved automated container build and deployment from GitHub source changes, demonstrating real-world DevOps practices in cloud infrastructure!"

    if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5000)

