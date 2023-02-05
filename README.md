# Locust load testing for Item calculation API
1. Update locustfiles/locustfile.py
2. Create the configmap

```bash
kubectl create configmap loadtest-locustfile --from-file locustfiles/locustfile.py
```

3. Install the helm chart
 
```bash

helm upgrade --install locust charts/locust \
  --set loadtest.name=loadtest \
  --set loadtest.locust_locustfile_configmap=loadtest-locustfile \
  --set loadtest.locust_locustfile=locustfile.py \
  --set worker.replicas=5 \
  --set worker.resources.requests.cpu="1" \
  --set worker.resources.requests.memory="500Mi"
```