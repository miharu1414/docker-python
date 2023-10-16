FROM python:3.11

RUN apt-get update
RUN pip install --upgrade pip
RUN python -m pip install jupyterlab
