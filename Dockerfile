FROM python:3.10.14-alpine
LABEL author="Kuba.csproj"

ENV LOG_FILE="log.txt"
ENV LOG_FREQUENCY=64

RUN pip install --upgrade pip

COPY ./app /app

WORKDIR /app

COPY ./run.sh /

ENTRYPOINT ["sh", "/run.sh"]