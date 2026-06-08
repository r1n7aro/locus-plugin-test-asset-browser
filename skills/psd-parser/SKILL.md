# PSD Parser

Use this skill when the user asks to inspect a Photoshop PSD or PSB file without opening Photoshop.

## Tool

- `parse_psd_header`: reads the PSD/PSB header and returns JSON metadata.

## Input

Pass a JSON object with `path`:

~~~json
{ "path": "Assets/UI/mockup.psd" }
~~~

Relative paths resolve against the current Locus workspace when available. The parser intentionally uses only the Python standard library so plugin import tests do not depend on external packages.

## Output

The tool reports `signature`, `version`, `format`, `channels`, `height`, `width`, `depth`, `colorMode`, `colorModeName`, and `fileSizeBytes`.
