FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
#  Debian + Python + FastAPI + UVicorn server

RUN pip install -U pip && pip install cython
RUN mkdir pythonpacks
COPY ./requirements.txt pythonpacks
RUN pip install --no-cache-dir -r pythonpacks/requirements.txt

RUN mkdir /models

ADD ./application/ /app


