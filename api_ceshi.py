from kubernetes import client,config

class Kube(object):
    api_instance=client.CoreV1Api()
    api_apps=client.AppsV1Api()
    def __init__(self) -> None:
        pass