from flask import Blueprint,render_template
from flask_login import login_required,current_user

views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def firstpage():
    return render_template('1stpage.html')


@views.route('/home',methods=['GET','POST'])
@login_required
def home():
    return render_template('home.html',user=current_user)

@views.route('/shopnow',methods=['GET','POST'])
@login_required
def shop():
    return render_template('shopnow.html',user=current_user)

@views.route('/placeorder',methods=['GET','POST'])
@login_required
def placeorder():
    return render_template('placeorder.html',user=current_user)