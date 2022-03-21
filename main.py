import datetime

from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # db_session.global_init("db/blogs.db")
    db_session.global_init(f"{input()}")
    db_sess = db_session.create_session()
    # --------------------------------------
    user = User()
    user.name = "Ridley"
    user.surname = 'Scott'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    user.name_p = 'van1'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Ridley"
    user.surname = 'Scott1'
    user.age = 22
    user.position = 'captain1'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scrtijott_chief@mars.org3'
    user.name_p = 'van2'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Ridley"
    user.surname = 'Scott2'
    user.age = 23
    user.position = 'captain2'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scoyuitytt_chief@mars.org2'
    user.name_p = 'van3'
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Ridley"
    user.surname = 'Scott3'
    user.age = 24
    user.position = 'captain3'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chsadfief@mars.org1'
    user.name_p = 'van4'
    db_sess.add(user)
    db_sess.commit()

    user = db_sess.query(User).filter(User.id == 1).first()
    job = Jobs(team_leader=1, job="deployment of residential modules 1 and 2", work_size=15, collaborators='2, 3',
               start_date=datetime.datetime.now(), is_finished=True)
    user.jobs.append(job)
    db_sess.commit()

    user = db_sess.query(User).filter(User.id == 2).first()
    job = Jobs(team_leader=2, job="good idea", work_size=5, collaborators='4, 5',
               start_date=datetime.datetime.now(), is_finished=False)
    user.jobs.append(job)
    db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
