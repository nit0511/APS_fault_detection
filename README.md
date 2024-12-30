Git --version
git commit -m "This is our first verion"
git remote -v
git config --global user.email <User_email_Id>
git config --global user.name <User_name>
git log
git add .
git status

'''
Whenever you start any project, you need setup.py file. 
'''
'''
After we run pip install -r requirements.txt sucessfully, then sensor.egg-info folder is created inside sensor folder. It picked out sensor folder because sensor folder contains __init__.py file. And also if -e . (HYPHEN_E_DOT) was not there in requirements.txt at the end of libraries then sensor.egg-info folder would not have been created. becaues of -e . python knows that this particular file is python pakage. it is important to create setup.py file and add -e . in the requirement file and also create __init__.py file in the pakage folder.    if you are working on any project always mention -e . in your requirements.txt file, also create setup.py filea after that you will be able to install your source code as a library and whenever you do with you installation you will find there is a pakage sensor.egg-info will be created which will contain all the details about your source code. 
'''


Training Pipeline is composed of components arrangeed in specific order.
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation
6. Model Pusher

An artifact is a machine learning term that describes the output (a fully trained model, a model checkpoint, or a file) created by the training process.