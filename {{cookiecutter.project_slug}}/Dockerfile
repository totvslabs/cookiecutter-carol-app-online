{%-if cookiecutter.pycarol_version == 'latest' %}
FROM totvslabs/pycarol:latest
{%- else %}
FROM totvslabs/pycarol:{{ cookiecutter.pycarol_version }}
{%- endif %}

env SRCFOLDER={{cookiecutter.project_slug}}

WORKDIR /app
ADD requirements.txt /app/
ADD {{cookiecutter.project_slug}}/ /app/{{cookiecutter.project_slug}}/

RUN pip install -r requirements.txt && \
  pip install gunicorn

EXPOSE 5000

VOLUME [ "/app" ]

CMD ["gunicorn", "-c", "/app/{{cookiecutter.project_slug}}/gunicorn.conf.py", "{{cookiecutter.project_slug}}.{{ cookiecutter.algorithm_name }}:application"]
