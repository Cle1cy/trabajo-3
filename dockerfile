FROM ubuntu 
RUN apt update
RUN apt install python3.8 -y
RUN apt install python3-pip -y
RUN pip3 install flask
RUN pip3 install mysql-connector-python
COPY ejemplodblocal.py /
COPY app.py /
COPY static/* /static/
COPY templates/* /templates/
COPY usuario.py /
EXPOSE 80
CMD ["python3.8","app.py","usuario"]

