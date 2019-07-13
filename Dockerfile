FROM rasa/rasa:latest

COPY ./ /app/
CMD ["run"]

