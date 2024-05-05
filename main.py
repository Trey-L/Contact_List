from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        contacts.append({
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone']
        })
        return redirect(url_for('index'))
    return render_template('add_contact.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_contact(index):
    if request.method == 'POST':
        contacts[index]['name'] = request.form['name']
        contacts[index]['email'] = request.form['email']
        contacts[index]['phone'] = request.form['phone']
        return redirect(url_for('index'))
    return render_template('edit_contact.html', index=index, contact=contacts[index])

@app.route('/delete/<int:index>')
def delete_contact(index):
    del contacts[index]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
