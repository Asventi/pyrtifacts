import requests_cache
import requests
import logging
from pyrtifacts_wrapper.schemas import Result
from typing import Dict, Optional
from pyrtifacts_wrapper.exceptions import PyrtifactsException
from json.decoder import JSONDecodeError

class   RestAdapter:
    def __init__(self, token: str, hostname: Optional[str] = 'api.artifactsmmo.com', ssl_verify: Optional[bool] = True, logger: Optional[logging.Logger] = None):
        """
        Constructor for RestAdapter
        :param hostname: (optional) Should be api.artifactsmmo.com
        :param token: Your account token
        :param ssl_verify: (optional) Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: (optional) If your app has a logger, pass it in here.
        """
        self._logger = logger or logging.getLogger(__name__)
        self.url = "https://{}/".format(hostname)
        self._token = token
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: str, endpoint: str, ep_params: Optional[Dict] = None, data: Optional[Dict] = None) -> Result:
        full_url = self.url + endpoint
        headers = {'Authorization': 'Bearer ' + self._token}
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method= http_method, url=full_url, verify=self._ssl_verify, headers=headers, params=ep_params, json=data)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=str(e))
            raise PyrtifactsException("Request failed") from e
        # Deserialize JSON output to Python object, or return failed Result on exception
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise PyrtifactsException("Invalid JSON") from e
        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        success = 200 <= response.status_code <= 299
        log_line = log_line_post.format(success, response.status_code, response.reason)
        if success:
            self._logger.debug(msg=log_line)
            return Result(response.status_code, response.reason, data_out['data'])
        log_line = log_line_post.format(success, response.status_code, data_out['error']['message'])
        self._logger.error(msg=log_line)
        raise PyrtifactsException(f"{response.status_code}: {data_out['error']['message']}")

    def get(self, endpoint: str, ep_params: Optional[Dict] = None) -> Result:
        return self._do('GET', endpoint, ep_params)

    def post(self, endpoint: str, ep_params: Optional[Dict] = None, data: Optional[Dict] = None) -> Result:
        return self._do('POST', endpoint, ep_params, data)

    def delete(self, endpoint: str, ep_params: Optional[Dict] = None, data: Optional[Dict] = None) -> Result:
        return self._do('DELETE', endpoint, ep_params, data)