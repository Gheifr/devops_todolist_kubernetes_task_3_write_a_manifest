FROM python:3.8

WORKDIR /app

COPY manage.py ./
COPY todolist ./todolist
COPY accounts ./accounts
COPY api ./api
COPY lists ./lists
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]