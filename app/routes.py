from flask import render_template, flash, redirect, url_for
from sqlalchemy import desc, asc

from app.forms import RemindForm
from app.models import User, Action
from datetime import datetime
from app import app, db, scheduler # ,socketio
import requests
import base64
google_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode=driving&key='+base64.b64decode('QUl6YVN5QVFCNGVpQ251UDhSWHQweFBMWW1zQ0RxcldYNGlGS0dj').decode('utf-8')
uber_url = 'https://rr1iky5f5f.execute-api.us-east-1.amazonaws.com/api/estimate/time?start_longitude={}&start_latitude={}'

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

def hit_api(api,email,_from,_to):
    now = datetime.now()
    action = Action(time=now, api=api, email=email)
    db.session.add(action)
    db.session.commit()
    if api=='google':
        url = google_url
        resp = requests.get(url.format(_from, _to)).json()
        return resp['rows'][0]['elements'][0]['duration']['value']
    elif api=='uber':
        url = uber_url
        _from,_to = _from.split(',')
        resp = requests.get(url.format(_from, _to)).json()
        return int(list(filter(lambda x:x['display_name']=='uberGO',resp['times']))[0]['estimate'])
    else:
        return 0

@app.route('/remind',methods=['GET'])
def remindUser():
    form = RemindForm()
    events = Action.query.order_by(desc(Action.time)).all()
    return render_template('form.html', title='Remind', form=form,events=events)

@app.route('/remind',methods=['POST'])
def remindPost():
    form = RemindForm()
    if form.validate_on_submit():
        email = form.email.data
        time = datetime.now().strftime('%Y-%m-%d ') + form.time.data
        _from = form.source.data.replace(' ', '')
        _to = form.destination.data.replace(' ', '')
        avgtime = hit_api('google', email, _from, _to)
        user = User(email=email, source=_from, destination=_to, time=datetime.strptime(time, '%Y-%m-%d %H:%M'),
                    traveltime=avgtime)
        db.session.add(user)
        db.session.commit()
    return redirect(url_for('remindUser'))

def get_next_mail():
    now = datetime.now()
    pmax = 5
    users = User.query.order_by(asc(User.time)).filter(User.level>0).limit(10)
    for user in users:
        timeleft = int(user.time.timestamp()-now.timestamp())
        ptime = 3600/pow(2,pmax-user.level)
        if timeleft>ptime and user.checked==0:
            resp = hit_api('uber',user.email,user.source,user.destination)
            if timeleft-resp<300 and timeleft>0:
                resp = hit_api('mail',user.email,None,None)
                user.level = 0
                db.session.commit()
                return
            else:
                resp = hit_api("google",user.email,user.source,user.destination)
                user.traveltime = resp
                user.level -=1
                db.session.commit()
        if timeleft<ptime:
            if user.checked==0:
                user.level -= 1
            if user.checked==1:
                user.checked = 0
            db.session.commit()

scheduler.add_job(func=get_next_mail, trigger="interval", minutes=1)
scheduler.start()
