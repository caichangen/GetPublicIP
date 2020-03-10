FROM python:alpine
LABEL author="Bryan"
LABEL email="mail0426@163.com"
LABEL maintainer="The container can get your public ip"
RUN pip install flask && mkdir /usr/local/ip
COPY ip.py /usr/local/ip
WORKDIR /usr/local/ip
CMD ["python","ip.py"]
EXPOSE 5000