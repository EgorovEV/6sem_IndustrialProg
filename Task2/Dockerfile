FROM python:3
RUN mkdir /code
WORKDIR /code
ADD ./ /code/
RUN pip install django~=1.11.0
EXPOSE 8000
ENTRYPOINT ["bash", "run.sh"]