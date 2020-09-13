FROM python:3.7-alpine

# set environment variables
    ## prevents python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1 \
    ## prevents python from bufferin stdout and stderr
    PYTHONUNBUFFERED=1 \
    ## default port for the app
    PORT=5480 \
    ## default mode is production
    FLASK_ENV=production \
    ## set workdir
    WORKDIR=/app

# set work directory
WORKDIR $WORKDIR

# copy project
COPY ./ $WORKDIR

# install dependencies & setup user & file permissions
RUN apk add --update --upgrade --no-cache --virtual .build-deps \
    bash \
    g++ \
    libxml2 \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libxml2-dev \
    libxslt-dev \
    && pip install --upgrade pip \
    && pip install pipenv \
    && pipenv lock --requirements > requirements.txt \
    && CFLAGS="-O0" pip install -r requirements.txt \
    ## create the app user
    && addgroup -S app \
    && adduser -S app -G app -h $WORKDIR \
    ## make startup scripts executable
    && chmod +x $WORKDIR/sh/crawler-container-startup.sh \
    # chown entry scripts to app user
    && chown -R app:app $WORKDIR/sh/crawler-container-startup.sh

# change to the app user
USER app

CMD ["/app/sh/crawler-container-startup.sh"]
