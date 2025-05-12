FROM python

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "-m", "pytest", "--cov=.", "--cov-report=html", "--cov-report=term-missing", "--alluredir=allure-results", "-v"]