from kubernetes import client,config

class Kube(object):
    api_instance=client.CoreV1Api()
    api_apps=client.AppsV1Api()
    def __init__(self,conf=None) -> None:
        if conf:
            config.load_kube_config(config_file=conf)
        else:
            config.load_incluster_config()
    def change_env(self,name,namespace):
        result=self.api_apps.read_namespaced_stateful_set(name=name,namespace=namespace)
        print(result)