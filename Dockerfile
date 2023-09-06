FROM python:3.11.3-alpine3.18
LABEL mantainer="rarorza@proton.me"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY djangoapp /djangoapp
COPY scripts /scripts

WORKDIR /djangoapp

EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home rarorza && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R rarorza:rarorza /venv && \
  chown -R rarorza:rarorza /data/web/static && \
  chown -R rarorza:rarorza /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts


ENV PATH="/scripts:/venv/bin:$PATH"

USER rarorza

# Executa o arquivo scripts/commands.sh
CMD ["commands.sh"]