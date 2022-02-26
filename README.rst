MotivEdge Python SDK
====================

Python SDK to download map directly. Provide the :code:`Client` class and
the script :code:`download.py` to download map seamlessly.

Pre-requirements
================

* Python >= 3.6
* An account at `Portal Motivedge <https://portal.motivedge.io/>`_

Installation
============

.. code:: bash

    pip install -U git+https://github.com/motivedge/python_sdk.git

*We will put on pypi later. Don't forget use :code:`-U` which keeps code to latest*

How to use
==========

1. Get API token from `profile & token page <https://portal.motivedge.io/profile>`_

.. code:: bash

    export ME_TOKEN=<api_token>

2. Find the target map's :code:`MAP_ID`. We could find this :code:`ID` at map details page of our portal site. It's next to the map name.


SDK Client
----------

* CostMap/2D map with :code:`Client`

  .. code:: python

     from motivedge import Client
     client = Client()
     download_file_folder = client.download_map(<map_id>)

  The downloaded maps folder will be saved in :code:`/tmp/motivedge_map_<map_id>`. It contains:

  - :code:`/tmp/motivedge_map_<map_id>/maps/map.png`
  - :code:`/tmp/motivedge_map_<map_id>/maps/map.yaml`
  - :code:`/tmp/motivedge_map_<map_id>/maps/metadata.yaml`

  If you want to save into different folder, you could do:

  .. code:: python

     client.download_map(<map_id>, path=<target_folder>)

* Costmap from point cloud/3D map with :code:`Client`

  .. code:: python

     from motivedge import Client
     client = Client()
     download_file_folder = client.download_map(<map_id>, lidar_height=<float_value>, path=<target_folder>)

  The default downloaded folder is same with above :code:`/tmp/motivedge_map_<map_id>`.

* Read mark points/paths/blocks from static methods :code:`read_mark_points`.
  After running above client download map, we could check data like below:

  .. code:: python

      meta_file_path = os.path.join(download_file_folder, "metadata.yaml")
      data = Client.read_mark_points(meta_file_path)

  Return a :code:`dict` with following struct

  .. code:: python

        {
            "marks": [{
                "name": "N1",
                "x": 1.2,
                "y": 5.0,
                "rz": 1.57
            }, ...],
            "paths": [{
                "name": "P1",
                # order points with (x, y) coord
                "path": [(1.9, 1.1), (2.3, 2.1), (4.3, 5.4), ...]
            }, ...],
            "blocks": [{
                "name": "B1",
                # block corner points with (x, y) coord
                "corners": [(1.9, 1.1), (2.3, 2.1), (4.3, 5.4), ...]
            }, ...],
        }


Script from Console
-------------------

* Costmap/2D map.

  .. code:: bash

     python scripts/download.py -m <map_id> -p <target_folder> --me_token <token>

  or

  .. code:: bash

     ME_TOKEN=<token> python scripts/download.py -m <map_id> -p <target_folder>

  :code:`-p <target_folder>` is optional. By default, downloaded folder is
  same with above :code:`/tmp/motivedge_map_<map_id>`.

* Costmap from point cloud/3D map

  .. code:: bash

     python scripts/download.py -m <map_id> -p <target_folder> --lidar_height <float_value> --me_token <token>

  or

  .. code:: bash

     ME_TOKEN=<token> python scripts/download.py -m <map_id> -p <target_folder> --lidar_height <float_value>

  :code:`-p <target_folder>` is optional. By default, downloaded folder is
  same with above :code:`/tmp/motivedge_map_<map_id>`.


Documentation
=============

Our portal site document is `here <https://docs.motivedge.io/SDK.html>`_ .

Contributing
============

We love sharing and welcome sharing and contributing. Please submit pull requests or raise issues in our repo.

License
=======

We are under Apache License 2.0 License.

@2022 MotivEdge
