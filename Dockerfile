FROM python:3

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./main.py /app/

ENV BIND_HOST=0.0.0.0
ENV BIND_PORT=500

EXPOSE 5000

CMD ["python", "main.py"]
