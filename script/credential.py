import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from settings import CREDENTIALS_FILE, SCOPES

def Authorize():
    """Авторизация в Google API"""
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        SCOPES)

    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets','v4', http=httpAuth)
    return service