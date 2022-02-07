#!/usr/bin/env python3
import sys
import logging
import argparse

from motivedge import Client


if __name__ == "__main__":

    logFormatter = "%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s"
    logging.basicConfig(format=logFormatter)
    logging.getLogger().setLevel(logging.INFO)
    
    parser = argparse.ArgumentParser(description='Download map from MotivEdge')
    parser.add_argument('-m', '--map_id', type=int, required=True,
                        help='Target map ID. You could find this ID in portal.motivedge.io. Required')
    parser.add_argument('-p', '--path', type=str, default="",
                        help=('The Target folder where the downloaded maps will be save. '
                              'By default, extracted `maps` folder will be saved in `/tmp/motivedge_map_{ID}/`'))
    parser.add_argument('--lidar_height', type=float, default=0.0,
                        help='Lider height to the ground. Required for 3D map')
    parser.add_argument('--resolution', type=float, default=0.05,
                        help='Downloaded costmap resolution for 3D map, default is 0.05')
    parser.add_argument('--me_token', type=str, default="",
                        help='API token. It could be set here or set ENV variable `ME_TOKEN`')

    args = parser.parse_args()
    map_id = args.map_id
    path = args.path
    lidar_height = args.lidar_height
    resolution = args.resolution
    me_token = args.me_token

    if map_id <= 0:
        logging.error("Map ID has to be larger than 0")
        sys.exit(1)

    client = Client(me_token)
    client.download_map(map_id, lidar_height, resolution, path)
