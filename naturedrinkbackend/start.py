import os
cmd = "python3 manage.py test"
os.system(cmd)
cmd = "python3 manage.py runserver 0.0.0.0:8000"
os.system(cmd)
