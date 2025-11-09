import pyautogui
import pyperclip
import time
from google import genai

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyBnECFse1lPozNpnP8kO5rreU6NEbRgfWE")

# Function to check if last message is from given sender(s)
def is_last_message_from_sender(chat_history, sender_names=["Hamza Bro", "Ammi"]):
    """
    Checks if the last message in the WhatsApp chat is from one of the given sender names.
    Returns True if yes, False otherwise.
    """
    lines = [line.strip() for line in chat_history.split("\n") if line.strip()]
    if not lines:
        return False

    last_line = lines[-1]
    return any(sender in last_line for sender in sender_names)


# Focus WhatsApp window
pyautogui.moveTo(1251, 1073)
pyautogui.click(1251, 1073)


print("🤖 WhatsApp AI Chatbot started...")

last_seen = ""

while True:
    print("\nChecking for new messages...")
    time.sleep(1)

    # Step 1: Select chat area and copy all text
    pyautogui.moveTo(932, 249)
    pyautogui.dragTo(1883, 971, duration=1.5)
    pyautogui.click(1783, 971)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Step 2: Read clipboard
    chat_history = pyperclip.paste()

    # Skip if nothing new
    if not chat_history or chat_history == last_seen:
        continue
    last_seen = chat_history

    print("Copied chat history:")
    print(chat_history)

    # Step 3: Check if last message is from Hamza Bro or Abba
    if is_last_message_from_sender(chat_history):
        print("📩 Message from Hamza Bro or Abba detected. Generating reply...")

        # Step 4: Prepare prompt
        prompt = f"""
        You are a person named Abdur who speaks English and Hindi. 
        You are from the Netherlands and you are a coder. 
        You are reading the following WhatsApp chat history:

        {chat_history}

        Now, reply as Abdur to the latest message only. 
        Respond naturally in Abdur's style, mixing English and Hindi if appropriate.
        Keep it short and casual.
        """

        # Step 5: Get Gemini response
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        # Extract reply text
        try:
            reply_text = response.text.strip()
        except AttributeError:
            reply_text = response.candidates[0].content.parts[0].text.strip()

        print("\n💬 Abdur's Reply:")
        print(reply_text)

        # Step 6: Send reply to WhatsApp
        pyautogui.moveTo(1286, 1013)
        pyautogui.click(1286, 1013)
        time.sleep(0.3)
        pyperclip.copy(reply_text)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.3)
        pyautogui.press("enter")

        print("✅ Reply sent successfully!")

    else:
        print("⏳ Last message not from Hamza Bro or Abba. Waiting...")

    time.sleep(1)
