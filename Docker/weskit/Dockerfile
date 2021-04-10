FROM continuumio/miniconda3

WORKDIR /app1

# Create the environment:
COPY environment.yaml .

RUN conda env create -f environment.yaml
RUN git clone https://gitlab.com/one-touch-pipeline/weskit.git
ENV PATH /opt/conda/envs/weskit/bin:$PATH
RUN /bin/bash -c "source activate weskit" \
    && cd /app1/weskit \
    && python -m pytest