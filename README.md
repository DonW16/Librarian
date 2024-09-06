# Librarian

Librarian my own FOSS Discord bot with features.

## Features


## Create a Discord Bot:

1. Go to the [Discord Developer Portal](https://discord.com/developers/)
2. Create a new application.
3. Create a bot user and get the bot token.
4. Invite the bot to your server with the appropriate permissions (Read and Manage Messages).
5. Enable Message Content Intent under the bot section.


Your DISCORD_BOT_TOKEN can be found here.

## Build pod
```bash
podman build -t librarian .
```

## Run pod
```bash
podman run --network host -e DISCORD_BOT_TOKEN="yourtokenhere" --read-only --cap-drop=ALL --security-opt=no-new-privileges -d --replace --name librarian-container librarian
```

## Pod params
```bash
--network host: Ensures the container uses the host’s network stack, bypassing the need for TUN/TAP devices.
--read-only: Makes the filesystem read-only.
--cap-drop=ALL: Drops all Linux capabilities, ensuring the container runs with the least privileges.
--security-opt=no-new-privileges: Ensures the container processes cannot gain new privileges.
```

## Add this bot to your server
[Click here.]()

## Preview


## Donate
- https://buymeacoffee.com/donw16
- XMR: 84jWayVVFGdSLjGLWSw1cKc4rWsocYz3XEctEggK2m7s6Lw46xirDWMac6NWQgUc5pDKVmTK6QGFbXrzUkDBuinRPRun6f7
- BTC: 3QYqpUdrinrmyJSrdBuTwgXpnYzHt5KaGj
- LTC: MCi1rHR6Yy9crMDxHGgkBgQMxUpFzt55us
- ETH: 0xf1a1929772F6CdC22594B88b53842a4Da594172e
