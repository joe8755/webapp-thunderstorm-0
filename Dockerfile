FROM debian:bookworm-slim
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV LISTEN_PORT=8080
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
EXPOSE 8080

WORKDIR /webapp-thunderstorm-0

COPY . /webapp-thunderstorm-0

RUN apt update && apt install -y --no-install-recommends python3 python3-venv

RUN python3 -m venv /webapp-thunderstorm-0-python-environment

ENV PATH /webapp-thunderstorm-0-python-environment/bin:$PATH

RUN pip install 'flask<3' 'werkzeug<3' psycopg2-binary opentelemetry-distro opentelemetry-exporter-otlp --no-input

RUN opentelemetry-bootstrap -a install

#CMD ["opentelemetry-instrument", "--logs_exporter", "otlp", "--metrics_exporter", "otlp", "--traces_exporter", "otlp", "flask", "run", "-p", "8080"]
CMD ["opentelemetry-instrument", "--logs_exporter", "console", "--metrics_exporter", "otlp", "--traces_exporter", "otlp", "flask", "run", "-p", "8080"]
