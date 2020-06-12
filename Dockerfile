FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /nekidaem_test
WORKDIR /nekidaem_test
COPY requirements.txt /nekidaem_test/
RUN pip install -r requirements.txt
COPY . /nekidaem_test/
#RUN python manage.py migrate
#RUN python manage.py loaddata example_data.json