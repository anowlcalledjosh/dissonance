# dissonance

a bot framework for Discord, written in Python using discord.py

**Note:** this framework is old and is no longer maintained.

## Dependencies

- Python 3.4+ (lower versions might work, but no guarantees)
- `discord.py` ([on GitHub][discord.py]) – tested with v0.8.0

[discord.py]: https://github.com/Rapptz/discord.py

## Example

```python3
import dissonance

@dissonance.register_command(lambda message: message.content.startswith("!ping"))
def command(message, client, match):
    client.send_message(message.channel, "Pong!")

dissonance.main()
```

## Copyright

Copyright © 2015 Ash Holland. Licensed under the EUPL (1.2 or later).
