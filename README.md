# Challenge Data 
## Introduction
This repository is destinated to  solve the data engineer challenge at Globant.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.

```bash
pip install -r requirements.txt
```

## Challenge #1
### Ponit 1 and 2
First start the REST API by running the following command
```bash
python src\app.py
```
And then run, in another command line:
```bash
python src\csvToJSONConverter.py
```

### Ponit 3
To run the third point, start the REST API by running the following command
```bash
python src\app.py
```
And then run, in another command line:
```bash
python src\backupToAVRO.py
```
At this point, a *GET* of the entire table is performed, to later transform it into an .AVRO file and save it in the /backup folder

### Ponit 4
To run the last point, start the REST API by running the following command
```bash
python src\app.py
```
And then run, in another command line:
```bash
python src\restoreTable.py
```
At this point, each .AVRO file made in the previous point is imported, then it is transformed into a python dictionary and finally saved again in the database

## Challenge #2

### Ponit 1 
First start the REST API by running the following command
```bash
python src\app.py
```
And then run, in the navigator the follow url: /employees-jobs-quarters