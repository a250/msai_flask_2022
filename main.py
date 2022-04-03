from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

import datetime

app = Flask(__name__)



data = {'menu': [
                    {'name':'Main page', 'link':'/'}, 
                    {'name':'New post', 'link':'/newpost'}
                ],
        'blogs': {}
       }


@app.route("/")
def index(data=data):
    
    return render_template('index.html', data=data)

@app.route("/postdetails/<b_id>")
def postdetails(b_id=None, data=data):
    print(b_id)
    blog_id = b_id
    blog_item = data['blogs'][int(b_id)]
    # print(blog_item[b_id])
    return render_template('details.html', blog_item=blog_item, data=data)

@app.route("/newpost")
def newpost(data=data):
    return render_template('newpost.html', data=data)

@app.route('/addblog', methods=['POST'])
def addblog():
    if request.method == 'POST':
        print(request.form['subject'], request.form['body'])
        return do_post(request.form['subject'], request.form['body'])

def do_post(subject, body):
    if not data['blogs']:
        blg_id = 1
    else:
        blg_id = max(data['blogs'].keys())+1
    
    blg_sbj = subject
    blg_bdy = body
    blg_dte = datetime.date.today().strftime("%d-%m-%Y")
    blg_url = f'postdetails/{blg_id}'
    
    item = {'id': blg_id, 
            'subject': blg_sbj,
            'text': blg_bdy,
            'date': blg_dte,
            'url': blg_url
           }
    data['blogs'][blg_id] = item
    return redirect(url_for('index'))