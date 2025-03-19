FROM python:3.11 AS builder

COPY requirements.txt . 

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --user -r requirements.txt

FROM python:3.11-slim

COPY --from=builder /root/.local /root/.local

COPY . .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 6000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:6000", "app:app"]