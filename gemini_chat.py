import os
import sys
from google import genai
from google.genai import types

# 检查环境变量是否已设置
if "GEMINI_API_KEY" not in os.environ:
    print("错误: 请先设置 GEMINI_API_KEY 环境变量。")
    sys.exit(1)

# 初始化客户端 (会自动读取 GEMINI_API_KEY)
client = genai.Client()

# 创建一个持续的对话 Session，这样它能记住上下文
# 这里我们使用最新的模型，您可以根据需要调整
chat = client.chats.create(model="gemini-2.5-flash")

print("=========================================")
print("🤖 Gemini 终端助手已启动！(输入 'quit' 退出)")
print("=========================================")

while True:
    try:
        # 获取用户输入
        user_input = input("\n\033[92mYou:\033[0m ")

        # 退出机制
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n再见！祝您科研顺利。")
            break

        if not user_input.strip():
            continue

        print("\033[96mGemini:\033[0m ", end="", flush=True)

        # 发送消息并流式接收回复 (打字机效果)
        response = chat.send_message_stream(user_input)
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print() # 换行

    except KeyboardInterrupt:
        # 允许使用 Ctrl+C 安全退出
        print("\n\n再见！")
        break
    except Exception as e:
        print(f"\n发生错误: {e}")
