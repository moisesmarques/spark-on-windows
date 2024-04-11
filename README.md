# spark-on-windows
How to run pyspark on Windows OS

## Step 1: Install Java
Download and install Java from [here](https://www.oracle.com/java/technologies/javase-jdk8-downloads.html)

## Step 2: Install Python
Download and install Python from [here](https://www.python.org/downloads/)

## Step 3: Install PySpark using pip
pip install pyspark

## Step 4: Clone winutils from github
git clone https://github.com/cdarlint/winutils.git

## Step 5: Set Environment Variables
- JAVA_HOME: C:\Program Files\Java\jdk1.8.0_251
- HADOOP_HOME: \source\repos\winutils/hadoop-3.x.x (CHANGE TO WHERE YOU CLONED winutils)
- PYSPARK_PYTHON: Python3.x\python.exe (CHANGE TO WHERE YOU INSTALLED PYTHON)

## Step 6: Update PATH
- %JAVA_HOME%\bin
- %HADOOP_HOME%\bin
- %PYSPARK_PYTHON%

## Step 7: Logout and Login on Windows

## Step 8: Run the test code
```python spark.py```



