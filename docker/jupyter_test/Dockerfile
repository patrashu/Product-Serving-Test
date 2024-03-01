FROM python:3.9-slim

RUN pip install pip --upgrade && \
    pip install jupyter

EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0", "--port=8888"]