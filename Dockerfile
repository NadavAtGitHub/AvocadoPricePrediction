FROM centos
RUN  yum update -y && yum install -y python3
COPY  . /app
WORKDIR /app
RUN ls -al && cat requirements.txt
RUN pip3 install --extra-index-url https://test.pypi.org/simple/  -r requirements.txt
RUN python3 avocado/manage.py makemigrations --noinput
RUN python3 avocado/manage.py migrate --noinput
EXPOSE 8000
USER 1000
CMD ["python3", "avocado/manage.py", "runserver", "0.0.0.0:8000"]