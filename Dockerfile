FROM jupyter/scipy-notebook

COPY . app

#WORKDIR app

## If you have a proper requirements.txt file, install all these requirements
RUN pip install --no-cache-dir -r app/source/requirements.txt

## Start Jupyter inside the container
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]