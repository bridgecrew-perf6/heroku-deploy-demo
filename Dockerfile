FROM python:3.10
WORKDIR /code
RUN ls
COPY ./requirements.txt /code/requirements.txt
RUN cat /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./code /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
