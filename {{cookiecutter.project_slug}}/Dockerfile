FROM totvslabs/pycarol:{{ cookiecutter.pycarol_version }}

env SRCFOLDER=src

WORKDIR /app
ADD requirements.txt /app/
ADD $SRCFOLDER/* /app/

RUN pip install -r requirements.txt && \
  pip install gunicorn

EXPOSE 5000

VOLUME [ "/app" ]

CMD ["gunicorn", "-b 0.0.0.0:5000", "{{ cookiecutter.algorithm_name }}:application"]
