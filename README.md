# container test

I built this small application to test GitHub's container registry feature.

## Pulling and running the container

pull the container

```bash
docker pull ghcr.io/kaoplo/container-test:main
```

run the container

```bash
docker run --rm -p 8000:8000 ghcr.io/kaoplo/container-test:main
```

visit `http://127.0.0.1:8000` to see the API respond.
