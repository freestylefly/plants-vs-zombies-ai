import os
import json

PROMPTS_DIR = "../prompts"

def list_prompts():
    """列出所有咒语集"""
    return [f for f in os.listdir(PROMPTS_DIR) if f.endswith('.json')]

def add_prompt(wizard_name, prompt):
    """为指定法师添加咒语"""
    file_path = os.path.join(PROMPTS_DIR, f"{wizard_name}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        data = {"name": wizard_name, "prompts": []}

    data["prompts"].append(prompt)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"咒语已添加到 {wizard_name}.json")

if __name__ == "__main__":
    print("欢迎使用咒语管理工具！")
    print("1. 列出所有咒语集")
    print("2. 添加咒语")
    choice = input("请选择操作: ")

    if choice == "1":
        prompts = list_prompts()
        print("现有咒语集:", prompts)
    elif choice == "2":
        wizard_name = input("请输入法师名字: ")
        title = input("请输入咒语标题: ")
        description = input("请输入咒语描述: ")
        content = input("请输入咒语内容: ")

        prompt = {
            "title": title,
            "description": description,
            "content": content
        }

        add_prompt(wizard_name, prompt)
    else:
        print("无效选择！")
