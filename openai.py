from openai import OpenAI
#OpenAI API key only works if you have Api paid key
client = OpenAI(
    api_key="# Enter your own secret key #",)
command="""
Woh muje bhi theek se nhi pata
Woh sab dekhna padega re
Me kal dekhati hi woh san
Sab
Okayy...
Yup
Akele project banane ka socha hai kya?
Ig tu abhi busy hai... Jab free ho jaaye toh bata
"""
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a person name shreya who speaks hindi and english . She is from India and is a coder. You analyze chat history and respond like shreya"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
