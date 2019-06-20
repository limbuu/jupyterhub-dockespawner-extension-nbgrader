
## Install notebook
From jupyter/base-notebook:latest

## Install nbgrader
#RUN conda install nbgrader=0.5*
RUN pip install nbgrader


## Install nbgrader extensions
RUN jupyter nbextension install --sys-prefix --py nbgrader --overwrite
RUN jupyter nbextension enable --sys-prefix --py nbgrader
RUN jupyter serverextension enable --sys-prefix --py nbgrader

USER root
## Add the nbgrader_config.py to /home/jovyan/.jupyter/
ADD ./nbgrader/nbgrader_config.py  /home/jovyan/.jupyter

## updating system
RUN rm -rf /var/lib/apt/lists/partial
RUN apt-get update -o Acquire::CompressionTypes::Order::=gz
RUN apt update -y

## Add a script in temp path for pull course assignments from github

RUN mkdir -p /tmp/script
ADD ./script/githubpuller.sh /tmp/script
RUN chmod +x /tmp/script/githubpuller.sh
RUN chmod -R 777 /tmp/script/githubpuller.sh

## Insatll OS dependencies for instructor
RUN apt-get install -y git && apt-get install -y nano

USER $NB_UID

## Add exchange directory
RUN mkdir -p /tmp/exchange
RUN chmod -R 777 /tmp/exchange


## Use following for connecting to mysql databases inplace of SQLite
## Install mysql-connector-python
RUN pip install mysql-connector-python

## Install pymysql
RUN pip install PyMySQL



