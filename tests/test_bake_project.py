import datetime
import json
import os
import shlex
import subprocess
import sys
from contextlib import contextmanager

import yaml
from click.testing import CliRunner
from cookiecutter.utils import rmtree

if sys.version_info > (3, 0):
    import importlib
else:
    import imp


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'README.md' in found_toplevel_files
        assert 'src' in found_toplevel_files

def test_bake_with_defaults_online(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.exception is None
        assert result.exit_code == 0
        project_path, project_slug, project_dir = project_info(result)
        manifest_file_path = f"{result.project}/src/manifest.json"
        with open(manifest_file_path, 'r') as manifest_file:
            manifest = manifest_file.read()
            assert '"online": {' in manifest
            assert f'"algorithmName": "alg_carol_app_boilerplate"' in manifest
            assert f'"name": "{project_slug}"' in manifest
        api_file_path = f"{result.project}/src/alg_carol_app_boilerplate.py"
        with open(api_file_path, 'r') as api_file:
            api = api_file.read()
            assert f"application = OnlineApi('alg_carol_app_boilerplate').get_api()" in api
