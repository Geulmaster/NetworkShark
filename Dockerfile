FROM geulmaster/tshark:v1.0.0
WORKDIR /NetworkShark
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH /NetworkShark
CMD ["python", "cli.py"]