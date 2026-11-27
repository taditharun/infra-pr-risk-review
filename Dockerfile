FROM python:3.12-slim

COPY src/read_plan.py /opt/planguard/read_plan.py
COPY fixtures/plan.json /opt/planguard/plan.json

ENTRYPOINT ["python", "/opt/planguard/read_plan.py"]
CMD ["/opt/planguard/plan.json"]
