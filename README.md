# dissonance

dissonance - a bot framework for Discord, written in Python using discord.py.

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

## Docs

Coming soon™!

## Versioning

dissonance uses [Semantic Versioning][semver] 2.0.0, meaning that:
- Major version is incremented with breaking public changes
- Minor version is incremented with added functionality
- Patch version is incremented with minor/internal bug fixes

[semver]: http://semver.org

## License

Copyright 2015 Josh Holland

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
