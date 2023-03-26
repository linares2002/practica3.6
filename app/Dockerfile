FROM python:3.7
MAINTAINER alumno@red.ujaen.es
WORKDIR /usr/app
COPY ./requirements.txt /usr/app/requiremets.txt
COPY ./templates /usr/app/templates/
COPY ./service.py /usr/app/service.py
RUN pip install -r /usr/app/requiremets.txt
CMD ["python", "service.py"]