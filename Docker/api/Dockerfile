FROM elixircloud/foca:latest

## Copy app files
COPY ./ /app

## Install app
RUN cd /app \
  && pip install -r requirements_weskit.txt \
  && python setup.py develop \

CMD ["bash", "-c", "cd /app/binding_scanner; python app.py"]