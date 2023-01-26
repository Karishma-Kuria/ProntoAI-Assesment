## This repo contains a script file which will run certain Git commands when provided with the local git repository path.

### Clone the repo
```sh
git clone https://github.com/Karishma-Kuria/ProntoAI-Assesment.git
cd ProntoAI-Assesment
```

### Setup virtual environment and install requirements
```sh
python3 -m venv project
source project/bin/activate
pip install -r requirements.txt
```

### If you don't use any virtual environment to run Python project you can directly install requirements
```sh
pip install -r requirements.txt
```
### Once the requirment is installed in your local machine pass the local git repository path to the gitScript.py  script and run it as follows
```sh
python gitScript.py <path to the local git repository>
```

For instance if the path of the local git repository is /Users/Test/ProntoAI/AIProject/ pass it to the script file as follows
```sh
python gitScript.py /Users/Test/ProntoAI/AIProject/
```

### Or as 
```sh
python gitScript.py "/Users/Test/ProntoAI/AIProject/"
```
### If you don not pass the local git repository path as argument to the script as shown above you will get below error
<img width="395" alt="image" src="https://user-images.githubusercontent.com/91119374/214723675-68c4c69a-e2fc-4721-987b-caf8b015c7d7.png">

### If the path passed as argument to the script does not exists you will get the below error
<img width="487" alt="image" src="https://user-images.githubusercontent.com/91119374/214723381-7223a3c8-a0f1-4e86-899d-c5309df41355.png">

### If the path passed as argument to the script does not contains a git repo you will get the below error
<img width="370" alt="image" src="https://user-images.githubusercontent.com/91119374/214749265-389c3bb3-907d-447a-b460-561d45f8b02f.png">

### Once the path is correct and the git repository exists you will get the below output

<img width="154" alt="image" src="https://user-images.githubusercontent.com/91119374/214723132-066e81f8-159d-4029-a454-afcc295e3d22.png">



