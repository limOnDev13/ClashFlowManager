FROM python:3.13

WORKDIR /ClashFlowManager

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATHBUFFERED=1

# Установить необходимые пакеты
RUN apt-get update && \
    apt-get install -y redis-tools net-tools iputils-ping curl && \
    rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip uv
COPY ./pyproject.toml ./uv.lock ./
RUN uv sync --no-dev

COPY . .
