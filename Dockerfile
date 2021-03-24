##### BASE IMAGE #####
FROM continuumio/miniconda3

##### METADATA ##### 
LABEL software="trs-filer"
LABEL software.website="https://github.com/krish8484/binding-scanner"
LABEL maintainer="akrish136@gmail.com"
LABEL maintainer.organisation="Zavolab, University of Basel"
LABEL maintainer.license="https://spdx.org/licenses/Apache-2.0"
RUN apt-get update && apt-get install -y nodejs openssl git build-essential python3-dev curl jq \
  && apt-get install -y snakemake

COPY ./ /app

## Install app
RUN cd /app \
  && python setup.py develop \
  && git clone https://github.com/zavolanlab/binding-scanner.git binding_scanner_git \
  && bash binding_scanner_git/scripts/create-conda-environment-main.sh \
  && activate binding-scanner \
  && cd /app/binding_scanner_git \
  && bash /app/binding_scanner_git/tests/integration/execution/snakemake_local_run_conda_environments.sh

ENV PATH /opt/conda/envs/$conda_env/bin:$PATH
ENV CONDA_DEFAULT_ENV $conda_env
