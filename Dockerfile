######################  Build stage ######################
FROM python:3.9-slim as build

# create app directory
WORKDIR /opt/project

#move the requirements to the app directory
COPY requirements.txt /opt/project

# install OS and python packages, then clean up
RUN apt-get -y update && apt-get -y install gcc graphviz-dev libsasl2-dev pkg-config \
    && pip install -r requirements.txt

######################  Run Stage ######################
FROM python:3.9-slim
WORKDIR /opt/project
COPY --from=build /root /root
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY requirements.txt /opt/project
RUN apt-get -y update && apt-get -y install gcc graphviz-dev libsasl2-dev pkg-config \
    && pip install -r requirements.txt

COPY . /opt/project

EXPOSE 8443

CMD ["python3", "web_interface.py"]