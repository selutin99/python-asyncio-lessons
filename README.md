# python asyncio lessons

## Table of contents
- [Overview](#Overview)
- [Documentation](#Documentation)
- [Git info](#Git-info)
- [Local Development](#Local-development)
- [Other useful info](#Other-useful-info)

## Overview
Repository with code examples of event loops, 
async/await mechanism based on [YouTube course](https://www.youtube.com/watch?v=ZGfv_yRLBiY&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8)

## Documentation
* Documentation by asyncio library:
[link](https://docs.python.org/3/library/asyncio.html)
* Python Concurrency From the Ground Up: LIVE!: 
[link](https://us.pycon.org/2015/schedule/presentation/374/)

## Git info
* For each issue, a separate branch is created with the name "feature/[name_of_feature]" (without []);
* After the work is completed, a pull request is created to the master branch;

## Local development
* Check you have Python 3.7.2 installed by typing on commandline `python --version`
* Install environment
```
pip install virtualenv
virtualenv venv
CALL venv/Scripts/activate (on Windows)
source venv/bin/activate (on Linux)
pip install -r requirements.txt
```
* Run lessons scripts from directory `lessons/*.py`

## Other useful info
The code of the examples belongs to [Oleg Molchanov](https://www.youtube.com/channel/UCD5_waDcGBhof9xuA1qovTQ)
