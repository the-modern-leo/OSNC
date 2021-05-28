### Build stage
FROM python:3.6-slim as python-build

# create app directory
WORKDIR /opt/project

#move the requirements to the app directory
COPY requirements.txt /opt/project

# install OS and python packages, then clean up
RUN apt-get -y update && apt-get -y install gcc graphviz-dev libsasl2-dev pkg-config \
    && pip install -r requirements.txt

### Run stage
FROM python:3.6-slim
WORKDIR /opt/project

# reinstall python packages without dev files
COPY --from=python-build /root /root
COPY --from=python-build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY requirements.txt /opt/project
RUN apt-get -y update && apt-get -y install graphviz gcc libldap-2.4-2 libsasl2-2 iputils-ping make\
    && pip install -r requirements.txt \
    && rm -rf /root/.cache

# set timezone, add any extra CA/intermediate certs to the image and fix OpenLDAP so it will create CA certs correctly
ENV TZ=America/Denver

# add the rest of the project files (database setup needs */db.py files)
COPY . /opt/project

