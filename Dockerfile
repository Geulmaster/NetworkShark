FROM python:3
WORKDIR /NetworkShark
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH /NetworkShark
CMD ["python", "cli.py"]