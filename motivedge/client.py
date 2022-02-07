import os
import logging
import requests
from io import BytesIO
from zipfile import ZipFile

from .constants import BASE_URL, ME_TOKEN, DOWNLOAD_PARENT_FOLDER
from .errors import TokenMissError, HTTPError


class Client:
    """
    API client to reach MotivEdge API.

    Wrap the requests, parameters, unzip, token, etc... in this class. User
    only need to use the simple API to fetch data from api.motivedge.io.

    Parameters
    ----------
    base_url: str
        Server base url. Currently, it's `api.motivedge.io`
    _token: str
        Token which is from MotivEdge Profile&Token page

    Methods
    -------
    __init__: initialize token in this methods
    download_map: fetch map zip file from server and unzip to target folder

    Example
    -------

    Set :code:`ME_TOKEN` ENV variable.

    $ export ME_TOKEN=<api_token>

    Costmap/2D map:

    >>> from motivedge import Client
    >>> client = Client()
    >>> client.download_map(<map_id>, path=<target_folder>)

    Costmap from point cloud/3D map

    >>> client.download_map(<map_id>, lidar_height=<float_value>, path=<target_folder>)
    """

    base_url = BASE_URL
    _download_parent_folder = DOWNLOAD_PARENT_FOLDER
    
    def __init__(self, me_token: str = ''):
        self._token = (me_token or os.environ.get(ME_TOKEN, "")).strip()
        if not self._token:
            raise TokenMissError(self._token)
        
    def download_map(self,
                     map_id: int,
                     lidar_height: float = 0.0,
                     resolution: float = 0.05,
                     path: str = ''):
        """
        Download map from MotivEdge server and unzip files into target folder

        Parameters
        ----------
        map_id: int
            Required. The ID could be found in map details of portal MotivEdge site.
        lidar_height: float
            Required for point cloud/3D map. Valid range is [0.1, 1.8]. Unit: meter.
            Ignored for costmap/2D map.
        resolution: float
            Optional for point cloud/3D map. Valid range is [0.01, 1.0]. Unit: meter.
            Ignored for costmap/2D map.
        path: str
            Optional. By default, files save in /tmp/motivedge_map_{map_id} folder.
        """
        url = self._get_download_url(map_id, lidar_height, resolution)
        target_folder = self._get_extract_path(path, map_id)
        logging.info(f"Start downloading map {map_id}")
        resp = requests.get(url)

        if resp.status_code != 200:
            err = resp.json()
            err_msg = f"HTTPError {err['status']}, Reason: {err['message']}"
            logging.error(err_msg)
            raise HTTPError(err)
        else:
            zipfile = ZipFile(BytesIO(resp.content))
            logging.info("Start extracting content in zip file")
            zipfile.extractall(target_folder)
            logging.info(f"`maps` folder created in {target_folder}")
            logging.info(f"Map downloaded. Ready to GO!")

    def _get_download_url(self, map_id: int, lidar_height: float, resolution: float):
        url = f"{self.base_url}/map/{map_id}/2d?me_token={self._token}"
        if lidar_height > 0:
            url += f"&h={lidar_height}"
        if resolution > 0:
            url += f"&r={resolution}"
        return url

    def _get_extract_path(self, path: str, map_id: int):
        if not path:
            return os.path.join(self._download_parent_folder, f"motivedge_map_{map_id}")
        return path
