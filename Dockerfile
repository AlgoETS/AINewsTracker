# Python fastapi app using poetry

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ARG PYTHONUNBUFFERED=1
ENV PORT=8080
ARG HOST=0.0.0.0


# Stage 1 - Build

# Install poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN poetry install
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt


# Run app
CMD uvicorn app.app:app --port $PORT --host=$HOST