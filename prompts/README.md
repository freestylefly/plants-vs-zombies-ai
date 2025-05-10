# Prompts

此文件夹用于存储每个法师的咒语集（prompt 集）。

## 咒语集命名规则
- 每个咒语集以法师的名字命名，例如：`wizard_name.json`。

## 咒语集格式
咒语集应为 JSON 格式，示例如下：

```json
{
  "name": "法师名字",
  "prompts": [
    {
      "title": "咒语标题",
      "description": "咒语描述",
      "content": "咒语内容"
    }
  ]
}
```

## 如何贡献咒语集
1. 创建一个新的 JSON 文件，按照上述格式编写咒语集。
2. 将文件放入此文件夹。
3. 提交 Pull Request 或直接上传到项目中。
