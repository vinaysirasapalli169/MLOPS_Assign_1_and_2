FROM  continuumio/miniconda3 as build

WORKDIR /myapp

COPY environment.yml env.yml

RUN conda env create -f env.yml && \
    conda install -c conda-forge conda-pack

# Use conda-pack to create a standalone enviornment
# in /venv:
RUN conda-pack -n myenv -o /tmp/env.tar && \
  mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
  rm /tmp/env.tar 

COPY hello.py hello.py
RUN /venv/bin/conda-unpack
RUN pip install azure-storage-blob

FROM python:3.8-slim-buster
# Copy /venv from the previous stage:
COPY --from=build /venv /venv
COPY --from=build myapp/app.py app.py
SHELL ["/bin/bash", "-c"]
ENTRYPOINT source /venv/bin/activate && \
           python app.py


#commands
#docker run -p 5000:5000 -d image_name
#docker container run image_name

#sudo chmod 666 /var/run/docker.sock