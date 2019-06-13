
## Install notebook
From jupyter/base-notebook:latest

## Install nbgrader
RUN pip install nbgrader

## Install nbgrader extensions
RUN jupyter nbextension install --sys-prefix --py nbgrader --overwrite
RUN jupyter nbextension enable --sys-prefix --py nbgrader
RUN jupyter serverextension enable --sys-prefix --py nbgrader

USER root
## Add the nbgrader_config.py to /home/jovyan/.jupyter/
ADD ./nbgrader/nbgrader_config.py  /home/jovyan/.jupyter

USER $NB_UID

## Add exchange directory
RUN mkdir -p /tmp/exchange
RUN chmod -R 777 /tmp/exchange

