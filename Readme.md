### To Run Flask Serer refer Api/FlaskApi.py. This import flask and defines an Rest API

First start using venv activate. Once venv is activated check what is pip version

`pip --version`

This should show that pip is from venv

you can also update pip using command

`python -m pip install upgrade pip`


you can manually install any python library package using command

`python -m pip install {package-name}`


You can install multiple packages by requriment.txt file as follows

-- requirement.txt File defines all the python plugin or library we need to use in PythonApp.

`pip install -r .\requirements.txt`

Set Following Environment Variables for project

1. FLASK_APP : Api/FlaskApi.py
2. FLASK_ENV : development
3. FLASK_DEBUG : 1

#### reference:

https://medium.com/@mushtaque87/flask-in-pycharm-community-edition-c0f68400d91e#:~:text=As%20we%20know%20there%20is,project%20and%20set%20it%20up.

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/


