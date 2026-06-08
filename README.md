# Asset Browser Tools

Asset Browser Tools is a plugin import fixture for Locus. Version `0.1.1` includes a Hello View and a PSD Parser skill so direct local, repository-link, release, and registry installs can verify component discovery.

![Asset browser preview](docs/asset-browser-preview.svg)

## Included Components

| Component | Path | Purpose |
| --- | --- | --- |
| Hello View | `views/hello-view` | Confirms View package import and plugin-managed View listing |
| PSD Parser Skill | `skills/psd-parser` | Confirms Skill package import and Python tool registration |

## PSD Tool Input

~~~json
{ "path": "Assets/UI/mockup.psd" }
~~~

The parser reads only the PSD/PSB header and uses no third-party Python dependencies.
