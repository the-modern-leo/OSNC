FROM python:3.8-slim-bullseye
COPY . /opt/OSNC
WORKDIR /opt/OSNC
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip cache purge

EXPOSE 8080
CMD ["python" ,"/opt/ONSC/main.py"]