FROM python:3.11.4-bookworm

ARG JUPYTER_USERNAME=amoha
ARG UID=1000
ARG GID=1000
ARG JUPYTER_PORT=8888

RUN groupadd -g ${GID} jupyteruser
RUN useradd -g ${GID} -u ${UID} ${JUPYTER_USERNAME}


COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

WORKDIR /home/${JUPYTER_USERNAME}
RUN chown -R ${JUPYTER_USERNAME} /home/${JUPYTER_USERNAME}
USER ${JUPYTER_USERNAME}

COPY . .

EXPOSE ${JUPYTER_PORT}
CMD ["jupyter", "notebook","--port","8888","--no-browser","--ip=0.0.0.0","--notebook-dir","./notebooks"]

# RUN echo "#!/bin/bash\njupyter notebook --port 8888 --no-browser --notebook-dir /app/notebooks /app/notebooks/eda-1.0.ipynb" > start_notebook.sh
# RUN chmod +x start_notebook.sh

# CMD ["./start_notebook.sh"]
