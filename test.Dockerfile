FROM python:3.7-alpine3.9

WORKDIR /app
COPY requirements requirements
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements/test.txt

COPY src src
COPY tests tests

ENTRYPOINT ["python3", "-m"]
CMD ["pytest", "tests/unit"]
