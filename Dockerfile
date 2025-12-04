# Switch to standard jupyter image if needed. I use this one locally for multiple projects.
FROM jupyter/pyspark-notebook:spark-3.5.0

# Prevent Python from writing .pyc files and buffer stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LOG_LEVEL=INFO

WORKDIR /home/jovyan/work
COPY pyproject.toml ./

# Use uv to install from pyproject.toml and install on system python
RUN pip install --no-cache-dir uv
RUN uv pip install --system pyproject.toml
