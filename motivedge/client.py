import os
import logging
import requests
from io import BytesIO
from zipfile import ZipFile

from .constants import BASE_URL, ME_TOKEN, DOWNLOAD_PARENT_FOLDER
from .errors import TokenMissError, HTTPError


class Client:

    base_url = BASE_URL
    download_parent_folder = DOWNLOAD_PARENT_FOLDER
    
    def __init__(self, me_token: str = ''):
        self._token = (me_token or os.environ.get(ME_TOKEN, "")).strip()
        if not self._token:
            raise TokenMissError(self._token)
        
    def download_map(self,
                     map_id: int,
                     lidar_height: float = 0.0,
                     resolution: float = 0.05,
                     path: str = ''):
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
            return f"{self.download_parent_folder}/motivedge_map_{map_id}"
        return path
