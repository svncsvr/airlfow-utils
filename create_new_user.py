import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user = PasswordUser(models.User())
user.username = input("please input username : ")
user.email = input("please input user email address : ")
user.password =  input("please input user password: ")
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()
