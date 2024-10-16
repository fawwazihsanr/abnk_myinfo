from rest_framework import exceptions, status
from rest_framework.response import Response

def dict_template(**kwargs):
    return {
        'success': kwargs["success"],
        'data': kwargs["data"],
        'errors': kwargs["message"],
    }


def response_template(data=None, status=status.HTTP_200_OK, success=True, message=[]):
    response_dict = dict_template(success=success, data=data, message=message)
    return Response(status=status, data=response_dict)


def success_response(data=None):
    return response_template(data)
