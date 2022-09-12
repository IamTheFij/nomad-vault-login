# nomad-vault-login

Shim service allowing authenticating a Nomad session using Vault

This service would runs along side Nomad and Vault and proxied on the same hostname so it can write to localstorage. It then provides a form to allow authentication with Vault and then will retrieve the token and store that in the browser for Nomad to use.

## Instructions

You can configure the service through environment variables.

* `BIND_HOST`: Host to bind the server on. Defaults to `0.0.0.0`.
* `BIND_PORT`: Port to bind the server on. Defaults to `5000`.
* `VAULT_ADDR`: Address where we can find Vault. Defaults to `http://127.0.0.1:8200`.
* `NOMAD_ROLE`: Default Nomad role to request from Vault. Defaults to `admin`.

Example Caddyfile

```caddyfile
nomad.example.com {
  reverse_proxy /login localhost:5000
  reverse_proxy localhost:4646
}
```
