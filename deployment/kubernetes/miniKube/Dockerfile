# Nginx image for a web server
FROM ubuntu

# File Author/ Maintainer
MAINTAINER SrinivasPG <spg349@nyu.edu>

# Install Nginx
RUN apt-get update \
&&  apt-get install -y nginx git-all \
&&  apt-get clean
RUN rm -v /etc/nginx/nginx.conf

# Fetching the latest source code from the github repo of devOps
RUN git clone https://github.com/gcallah/DevOps /usr/share/nginx/html/DevOps
#COPY DevOps /use/share/nginx/html
#RUN cd DevOps && git submodule init && git submodule update

VOLUME /usr/share/nginx/html

VOLUME /etc/nginx

COPY conf /etc/nginx/nginx.conf

# Expose ports
#EXPOSE 80

# Start Nginx Service
CMD service nginx start




