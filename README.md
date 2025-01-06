<<<<<<< HEAD
# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```


To download your dataset

```
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```

This is changes made in neuro lab


Git commands

If you are starting a project and you want to use git in your project
```
git init
```
Note: This is going to initalize git in your source code.


OR

You can clone exiting github repo
```
git clone <github_url>
```
Note: Clone/ Downlaod github  repo in your system


Add your changes made in file to git stagging are
```
git add file_name
```
Note: You can given file_name to add specific file or use "." to add everything to staging are


Create commits
```
git commit -m "message"
```

```
git push origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name 

To push your changes forcefully.
```
git push origin main -f
```


To pull  changes from github repo
```
git pull origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name


.env file has
```
MONGO_DB_URL="mongodb://localhost:27017"
AWS_ACCESS_KEY_ID="aagswdiquyawvdiu"
AWS_SECRET_ACCESS_KEY="sadoiuabnswodihabosdbn"
```

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```


```

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
AWS_ECR_LOGIN_URI=
ECR_REPOSITORY_NAME=
BUCKET_NAME=
MONGO_DB_URL=
```
=======
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
>>>>>>> 22ddc4ff49ec59dae62f9f0c2b7428a6600301cc
