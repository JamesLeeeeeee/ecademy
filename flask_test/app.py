from flask import Flask, render_template
import pymysql

# #데이터베이스 접근
db= pymysql.connect(host='192.168.111.100',
                    user='user',
                    passwd='1234!@#$',
                    db='testdb',
                    charset='utf8'
                    )
cursor= db.cursor()
sql='''select * from testtb limit 10'''
cursor.execute(sql)
result=cursor.fetchall()
app = Flask(__name__)

student_data = {
    1: {"name": "슈퍼맨", "score": {"국어": 90, "수학": 65}},
    2: {"name": "배트맨", "score": {"국어": 75, "영어": 80, "수학": 75}}
}

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'

@app.route('/rendering')
def render():
    return '''
    <h1>이건 h1 제목</h1>
    <p>이건 p 본문 </p>
    <a href="https://flask.palletsprojects.com">Flask 홈페이지 바로가기</a>
    '''
@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/inheritance')
def inheritance():
    return render_template('inheritance.html',
                           template_students= student_data)

@app.route("/student/<int:id>")
def student(id):
    return render_template("student.html",
            template_name=student_data[id]["name"],
            template_score=student_data[id]["score"])
@app.route('/sql')
def sql():
    return result
if __name__ == '__main__':
    app.run(debug=True)