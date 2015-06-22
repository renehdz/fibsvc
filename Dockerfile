FROM ubuntu:14.04
MAINTAINER Rene Hernandez "renehdz@gmail.com"

RUN apt-get update

RUN apt-get install -y curl python-pip
RUN pip install bottle==0.12.8
RUN pip install WebTest==2.0.18

ADD / /var/www/fibsvc

WORKDIR /var/www/fibsvc

EXPOSE 8080

CMD ["python",  "fibonacci_service.py"]



