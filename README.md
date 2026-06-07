# Asset Browser Tools

Asset Browser Tools is a test fixture for the Locus Plugin Hub detail window. It describes a compact Unity asset browsing workflow and intentionally includes Markdown structures that the Hub should render consistently.

![Asset browser preview](docs/asset-browser-preview.svg)

## What This Plugin Pretends To Provide

The package represents a small set of Unity editor helpers for teams that repeatedly inspect prefabs, materials, scripts, and scenes. In a real plugin, the workflow would collect project assets into reusable views, keep common filters nearby, and reduce repeated Project window navigation.

## Detail Window Test Coverage

| Area | Expected Hub Behavior |
| --- | --- |
| Heading hierarchy | Rendered with compact plugin detail typography |
| Relative image | `docs/asset-browser-preview.svg` resolves against this repository README |
| Table | Width stays inside the modal and scrolls horizontally when needed |
| Inline code | `Assets/Characters/Hero.prefab` keeps document styling |
| Lists | Dense but readable spacing inside the detail modal |

## Example Asset Filters

- Prefabs updated in the last build iteration
- Materials with missing texture assignments
- Scripts under `Assets/Editor` and `Packages/com.company.tools`
- Scene references grouped by folder and asset type

```json
{
  "filter": "type:Prefab path:Assets/Characters",
  "groupBy": "folder",
  "showDependencies": true
}
```

## Notes For Registry Testing

This repository is intentionally minimal. The installable plugin package is published as a GitHub release asset. The repository keeps source-level fixture files and documentation, so the registry can download the release package without storing binary archives in the repository. This README acts as the rich `descriptionSource` content for the registry entry. The Hub should display this text after the card is clicked, with the fallback short description remaining available when the README cannot be loaded.

See the registry entry in [locus-plugin-registry](https://github.com/r1n7aro/locus-plugin-registry/tree/test/v1/plugins/d0).