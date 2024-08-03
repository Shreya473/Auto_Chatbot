# Run the program and keep the chrome window to see the magic of autochatbot
import pyautogui 
import time
import pyperclip
import openai

client = OpenAI(
    api_key="# Enter your own secret key #",)
# Change the sender_name according to requirement
def is_last_message(chat_log, sender_name="Saahil Chaurasia"):
    message=chat_log.strip().split("/2024")[-1]
    if sender_name in messages:
        return True
    return False
    
pyautogui.click(905,739)
time.sleep(1)  # Shorter wait time should be enough
# Click to focus on the starting point
while True:
    

    # Move to the starting point and drag to the end point
    pyautogui.moveTo(474, 151)
    time.sleep(0.5)  # Add a small delay before starting the drag
    pyautogui.dragTo(1346, 632, duration=1.0, button='left')
    time.sleep(0.5)  # Add a small delay after the drag

    # Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for the copy operation to complete

    # Print the copied text
    text = pyperclip.paste()
    pyautogui.click(1346, 632)
    print(text)
    if is_last_message(text):
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {"role": "system", "content": "You are a person name shreya who speaks hindi and english . You is from India and you are a coder. You analyze chat history and respond like shreya.Output should be the next chat response (text message only)"},
        {"role": "user", "content": text}
        ]
        )

        response= completion.choices[0].message.content
        pyperclip.copy(response)
        pyautogui.click(654, 689)
        time.sleep(1)

        pyautogui.hotkey('crtl','v')
        time.sleep(1)
        pyautogui.press('enter')