An AngularJS Based simple frontend for a Ganeti Cluster
=======================================================

Design goals are to have a very simple fronend to display, and to make some small changes.

Installation:
-------------
* Install python-tornado
* Modify ganeti-frontend.py to point to the master node of your cluster
* ./ganety-frontend.py
* Browse to the host port 8888 with http

Todo:
-----
* Finalize UI and visibility
* Fix reload issue
* Add authentication
* Add modify as below
* Add historical tracking
* Add graphs (graphite)
* Better installation and dependancy documentation
* Multi-node autodiscovery
* Cluster selector?

Specific modify abilities:
--------------------------
* Shutdown / Startup a VM
* Open a VNC console
* Change memory and CPU
* Migrate to another node

Possible future
---------------
* Create a new VM
* Add storage
* Change storage profiles

Known Issues:
* Page does not load the data properly on the first attempt, wait 10 seconds or click on "Foo" on the main page (hackish)
