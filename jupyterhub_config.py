# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Configuration file for JupyterHub
import dummyauthenticator
import dockerspawner
from jupyterhub.spawner import Spawner
c = get_config()

# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
#c.DummyAuthenticator.password = "123"
# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'jupyterhub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image = 'jupyter/base-notebook:v7'

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'jupyterhub'

# delete containers when the stop
c.DockerSpawner.remove = True

# for debugging arguments passed to the spwaned containers
c.DockerSpawner.debug = True

## normally mount the notebook server volumes
notebook_dir = '/home/jovyan/work'
#c.DockerSpawner.notebook_dir = notebook_dir
#c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# mount notebook server volunes with persistant storage in host
notebook_dir = '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
host_dir = '/home/manshi/docker-workspace/working-codehub-prod/codehub-dockerspawner-nbgrader/notebook-data'

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container

c.DockerSpawner.volumes = {"/home/manshi/docker-workspace/working-codehub-prod/codehub-dockerspawner-nbgrader/notebook-data/{username}": {"bind": "/home/jovyan/work/course101", "mode": "rw"}}
