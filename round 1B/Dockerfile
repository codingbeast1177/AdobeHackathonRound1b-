FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt ./backend_requirements.txt
COPY requirements.txt ./root_requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r backend_requirements.txt && \
    pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r root_requirements.txt

COPY processor/ processor/
COPY Collection_1/ Collection_1/
COPY Collection_2/ Collection_2/
COPY Collection_3/ Collection_3/
COPY backend/ .

# REMOVE THESE IF FILES DON'T EXIST
# COPY backend/round1B_input.json .
# COPY backend/round1B_output.json .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
