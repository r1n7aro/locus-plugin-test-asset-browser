# Asset Browser Tools

Asset Browser Tools 是 Locus 插件导入测试仓库。`0.1.1` 版本包含一个 Hello View 和一个 PSD Parser Skill，可用于验证本地导入、仓库链接导入、release 安装和注册表安装后的组件发现。

![资产浏览预览](docs/asset-browser-preview.svg)

## 包含组件

| 组件 | 路径 | 用途 |
| --- | --- | --- |
| Hello View | `views/hello-view` | 验证 View 包导入和插件托管 View 列表 |
| PSD Parser Skill | `skills/psd-parser` | 验证 Skill 包导入和 Python 工具注册 |

## PSD 工具输入

~~~json
{ "path": "Assets/UI/mockup.psd" }
~~~

解析器只读取 PSD/PSB 文件头，不依赖第三方 Python 包。
