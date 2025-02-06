# classical_gram_schmidt
Practice

# Runnning
## Python
```
$ cd python
$ poetry run python3 cram_schmidt.py
```
## Rust
```
$ cd rust
$ cargo run
```

Docker container is also available if you need
```
$ cd classical_gram_schmidt
$ docker compose  -f docker/docker-compose.yaml build
$ docker compose -f docker/docker-compose.yaml  up -d
$ docker compose -f docker/docker-compose.yaml run --rm rust_adn_python cargo run --manifest-path /root/classical_gram_schmidt/rust/Cargo.toml

```