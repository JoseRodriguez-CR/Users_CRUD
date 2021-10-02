from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    users=User.get_all()
    #id= users.id
    #print(id)
    return render_template("Read.html", users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("Create.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("Show.html", user=User.get_one(data))   


@app.route('/user/edit/<int:id>')
def edit(id):
    data= {
        "id":id
    }
    return render_template("Edit.html", user=User.get_one(data))

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/users')

@app.route('/user/update',methods=['POST'])
def update():
    print(request.form)
    User.update(request.form)
    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)