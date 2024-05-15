# kind

```
kind create cluster --config cluster-config.yml
kind delete cluster

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s
```



# to test ingress in kind

```
kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/usage.yaml
```



# postgresql db helm chart

```
helm install my-release oci://registry-1.docker.io/bitnamicharts/postgresql
```



# pgadmin4 helm chart

```
helm repo add runix https://helm.runix.net
helm install pgadmin4 runix/pgadmin4
```



# container commands

```
docker build . -t localhost/webapp-thunderstorm-0:v0.0.1
export CR_PAT=YOUR_TOKEN
echo $CR_PAT | docker login ghcr.io -u joe8755 --password-stdin
#docker tag localhost/webapp-thunderstorm-0:v0.0.1 ghcr.io:443/joe8755/webapp-thunderstorm-0:v0.0.1
docker tag localhost/webapp-thunderstorm-0:v0.0.1 ghcr.io/joe8755/webapp-thunderstorm-0:v0.0.1
docker push ghcr.io/joe8755/webapp-thunderstorm-0:v0.0.1
```



# flux

```
export GITHUB_TOKEN=<your-token>
export GITHUB_USER=<your-username>

flux bootstrap github \
  --owner=$GITHUB_USER \
  --repository=fleet-infra \
  --branch=main \
  --path=./clusters/my-cluster \
  --personal

flux create source git webapp-thunderstorm-0 --url=https://github.com/joe8755/webapp-thunderstorm-0 --branch=main --interval=1m --export > ./clusters/my-cluster/webapp-thunderstorm-0-source.yaml

flux create kustomization webapp-thunderstorm-0 \
  --target-namespace=default \
  --source=webapp-thunderstorm-0 \
  --path="./kustomize" \
  --prune=true \
  --wait=true \
  --interval=30m \
  --retry-interval=2m \
  --health-check-timeout=3m \
  --export > ./clusters/my-cluster/webapp-thunderstorm-0-kustomization.yaml
```



# container registry secret

```
kubectl create secret docker-registry regcred --docker-server=ghcr.io --docker-username=joe8755 --docker-password=password
```
