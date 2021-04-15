FROM elixircloud/foca:latest

## Copy app files
COPY ./ /app

## Install app
RUN cd /app \
  && git clone https://gitlab.com/one-touch-pipeline/weskit.git \
  && pip install cerberus==1.3.2 \
  && python setup.py develop

CMD ["bash", "-c", "cd /app/binding-scanner; python app.py"]