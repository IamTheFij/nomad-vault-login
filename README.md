# nomad-vault-login

Shim service allowing authenticating a Nomad session using Vault

The idea is that this service would be run along side Nomad and Vault and proxied on the same hostname so it can write to localstorage. It would then provide a form to allow authentication with Vault and then will retrieve the token and store that in the browser for Nomad to use.

It is, as of now, completely untested and may not work at all.
