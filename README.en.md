# Asset Browser Tools

Asset Browser Tools is a test fixture for the Locus Plugin Hub detail view. It models a compact Unity asset browsing helper and validates English rich descriptions, relative images, tables, and code blocks.

![Asset browser preview](docs/asset-browser-preview.svg)

## Intended Capabilities

- Surface common Prefab, Material, and Script entry points
- Keep reusable filters close to the current workflow
- Group scene references by folder and asset type
- Present asset inspection results in a compact layout

## Detail View Coverage

| Area | Expected Behavior |
| --- | --- |
| Heading hierarchy | Rendered with compact plugin detail typography |
| Relative image | `docs/asset-browser-preview.svg` resolves against this README |
| Table | Stays readable inside the detail pane |
| Inline code | `Assets/Characters/Hero.prefab` keeps document styling |

## Example Filter

~~~json
{
  "filter": "type:Prefab path:Assets/Characters",
  "groupBy": "folder",
  "showDependencies": true
}
~~~

This repository is intentionally minimal. The downloadable plugin package comes from a release or dynamic download source, while this README supplies the rich detail content.
