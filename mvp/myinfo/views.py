from rest_framework.views import APIView

from mvp.myinfo.services import retrieve_authorise_url, get_auth_code
from mvp.myinfo.utils import success_response


class MyinfoView(APIView):
    def get(self, request):
        cookie = request.COOKIES.get('sessionid')
        url = retrieve_authorise_url(cookie)
        return success_response(url)

    def post(self, request):
        cookie = request.COOKIES.get('sessionid')
        data = request.data
        return success_response(get_auth_code(cookie, data['auth_code']))
