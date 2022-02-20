FROM python:3.10
WORKDIR /code
RUN export PYTHONPATH=${PYTHONPATH}:/code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./code /code/app
CMD uvicorn app.app:app --host 0.0.0.0 --port $PORT
