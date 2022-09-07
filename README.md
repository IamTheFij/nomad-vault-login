# nomad-vault-login

Shim service allowing authenticating a Nomad session using Vault

The idea is that this service would be run along side Nomad and Vault and proxied on the same hostname so it can write to localstorage. It would then provide a form to allow authentication with Vault and then will retrieve the token and store that in the browser for Nomad to use.

Right now it appears to be working, but isn't super pretty and I have no written instructions.
