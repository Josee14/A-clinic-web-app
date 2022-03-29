from flask import Blueprint
from flask import current_app
from app import create_app
from app import login_manager
from models import *
from forms import *
from utils import *
from decorators import admin_required, moderator_required, permission_required

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    abort,
)
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
from werkzeug.routing import BuildError
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from PIL import Image

app = create_app()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ------------------------------- MAIN APP ROUTES -----------------------------



# Home
@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    form = MakeAppointment()
    
    if request.method == 'POST' and form.validate_on_submit():
        # try:
        phone_no = form.phone_no.data
        date = form.date.data.strftime('%Y-%m-%d')
        doctor = form.doctor.data
        message = form.message.data
        user_id = current_user.id

        print(phone_no,date,doctor,message)
        
        new_appointment = Appointments(
            phone_no=phone_no,
            date=date,
            doctor=doctor,
            message=message,
            user_id=user_id
        )
        db.session.add(new_appointment)
        db.session.commit()
        flash("Appointment Received!", "success")
        return redirect(url_for('index'))

        # except:
        #      flash("An Error occured!", "danger")

    return render_template("index.html",
        title="CLINICA | Home",
        form=form
        )


@app.route("/dashboard", methods=("GET", "POST"), strict_slashes=False)
@login_required
def dashboard():

    return render_template("dashboard.html",
        title="CLINICA | Dashboard",
        )

@app.route("/dashboard/users", methods=("GET", "POST"), strict_slashes=False)
@admin_required
@login_required
def users():
    users = User.query.order_by(User.id.asc()).all()
    appointments = Appointments.query.order_by(Appointments.id.asc()).all()

    return render_template("users.html",
        title="CLINICA | Dashboard",
        users=users,
        appointments=appointments
        )

@app.route("/dashboard/appointments", methods=("GET", "POST"), strict_slashes=False)
@login_required
def appointments():
    appointments = Appointments.query.order_by(Appointments.id.asc()).all()


    return render_template("appointment.html",
        title="CLINICA | Dashboard",
        appointments=appointments
        )


@app.route("/dashboard/appointments/toggle/<int:appointment_id>", methods=("GET", "POST"), strict_slashes=False)
@admin_required
@login_required
def toggle_appointments(appointment_id):
    appointment = Appointments.query.filter_by(id=appointment_id).first()

    appointment.status = not appointment.status
    db.session.commit()

    return redirect(url_for('appointments'))



if __name__ == "__main__":
    app.run(debug=True)
