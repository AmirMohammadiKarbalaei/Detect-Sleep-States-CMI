FROM python:3.11.5


WORKDIR /app


COPY environment.yml .

RUN pip install -r environment.yml


COPY . .


CMD ["python", "notebooks/eda - 1.0.ipynb"]