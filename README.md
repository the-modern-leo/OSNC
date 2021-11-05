# OSNC
Open Source Network Controller

Step 1: 
docker build '/Users/nickbradberry/PycharmProjects/OSNC/' -t onsc:latest

Step2:
docker run -v '/Users/nickbradberry/PycharmProjects/OSNC/':/opt/project -p 443:8443 onsc:latest 




Project is being built with the following features: 
A containerized web server. The webserver python Tornado 