FROM python:3
RUN mkdir /code
WORKDIR /code
ADD ./ /code/
RUN pip install -r req.txt
EXPOSE 8000
ENTRYPOINT ["bash", "run.sh"]