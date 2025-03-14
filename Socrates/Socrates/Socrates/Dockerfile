FROM python:3.12

RUN export DEBIAR_FRONTEND=noninteractive \
    && apt update

ARG TZ
RUN echo ${TZ} > /etc/timezone

WORKDIR /socrates

COPY . /socrates

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r /socrates/requirements.txt

EXPOSE 6100

CMD ["python3", "/socrates/app/main.py"]
