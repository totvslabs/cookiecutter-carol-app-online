import sys
import json
import random

from pycarol.app.online import Online
from pycarol.app.online_api import OnlineApi, request


online = Online()

@online.route("hello_world")
def hello_world():
    message = {
        'message': 'Hello World'
    }
    return message

@online.route("predict")
def predict():
    result = {
        'score': random.randint(1,9)
    }
    return result

@online.route("sum")
def sum():
    total = 0;
    print(request)

    param = request

    if(param != None):
        for key in param:
            try:
                total += float(param[key])
            except RuntimeError:
                pass

    result = {
        'sum': total
    }
    return result


flask = OnlineApi('carol_app_boilerplate').get_api()


def main():
    """Runs from command prompt
    """
    if __name__ == "__main__":
        flask.run(debug=True)


main()
