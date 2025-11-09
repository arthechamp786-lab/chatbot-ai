



import pyautogui
import pyperclip
import time
from google import genai

client = genai.Client(api_key="AIzaSyBnECFse1lPozNpnP8kO5rreU6NEbRgfWE")

# Give yourself time to switch to the right window
print("starting in 5 seconds")
time.sleep(5)


# Step 1: Click on the icon
pyautogui.moveTo(1251,1073)
pyautogui.click(1251, 1073)
time.sleep(2)

# Step 2: Drag to select text
pyautogui.moveTo(932, 249)
pyautogui.dragTo(1883, 971, duration=1.5)
pyautogui.click(1783, 971)

# Step 3: Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get clipboard content
chat_history = pyperclip.paste()
print("Copied text:")
print(chat_history)

# Step 5: Combine with prompt instructing the model to reply
prompt = f"""
You are a person named Abdur who speaks English and Hindi. 
You are from Netherlands and you are a coder. 
You are reading the following WhatsApp chat history:

{chat_history}

Now, reply as Abdur to the **latest message only**. Respond naturally in Abdur's style, mixing English and Hindi if appropriate.
    """

 # Step 6: Generate reply
response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt

    )
print("\n Abdur's Reply")
print(response.text)


pyautogui.moveTo(1286, 1013)
pyautogui.click(1286, 1013)   # Click the WhatsApp input box
time.sleep(0.3)
pyperclip.copy(response.text)    # Copy reply to clipboard
pyautogui.hotkey("ctrl", "v") # Paste the reply
time.sleep(0.3)
pyautogui.press("enter")      # Send message

print("✅ Reply sent successfully!")
