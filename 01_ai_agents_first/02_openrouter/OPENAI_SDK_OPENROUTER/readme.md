
# **OpenRouter ko OpenAI Agents SDK ke sath use karna**

### 🛠 Setup ki zaroori cheezein:

1. **OpenRouter par sign up karo**
2. **API Key banao**
3. **Ek free model select karo** (hum yahan free model hi use kar rahe hain to continue kar sakte ho)

---

### 💸 Free aur Paid Models

OpenRouter support karta hai latest **DeepSeek V3 0324** aur 50+ models ko **bilkul free** mein. Zyada tar models **OpenAI Chat Completion API** ka defacto standard follow karte hain.

Agar aap free model use kar rahe ho (jiska ID end mein `:free` hota hai), to aap:

* **20 requests per minute**
* **200 requests per day** tak limited ho.

🔗 **Models list dekhne ke liye:** [https://openrouter.ai/models](https://openrouter.ai/models)

📌 **Note:** OpenRouter inference time par koi extra charges nahi leta.

---

### ⛔ Rate Limiting aur Credits ka system:

* Free model ka use karte hue: 20 request per minute aur 200 per day ka limit hota hai.
* Agar aapke account ka credit balance negative ho gaya to **402 errors** aa sakte hain — even on free models. Balance positive karne ke baad aap un models ko phir se use kar sakte ho.

---

### 📚 Reference

#### OpenAI Agents dependencies install karne ke liye:

```python
!pip install -Uq openai-agents
```

---

### ⚙️ Import aur Configuration

```python
import nest_asyncio
nest_asyncio.apply()
```

```python
from google.colab import userdata

OPENROUTER_API_KEY = userdata.get("OPENROUTER_API_KEY")
```

---

### 🌐 API aur Model ka config:

```python
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "mistralai/mistral-small-24b-instruct-2501:free"
```

Kuch aur free models (26 March):

* [https://openrouter.ai/deepseek/deepseek-chat-v3-0324\:free](https://openrouter.ai/deepseek/deepseek-chat-v3-0324:free)
* [https://openrouter.ai/google/gemini-2.5-pro-exp-03-25\:free](https://openrouter.ai/google/gemini-2.5-pro-exp-03-25:free)

---

### 1️⃣ OpenRouter API directly use karna:

```python
import requests
import json

response = requests.post(
  url=f"https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
  },
  data=json.dumps({
    "model": MODEL,
    "messages": [
      {
        "role": "user",
        "content": "Hi, i have 1000 pkr i want you to convert into usd"
      }
    ]
  })
)

print(response.json())
```

➡️ Output mein model response return karega jisme likha hoga:

**PKR ko USD mein convert karne ke liye current exchange rate chahiye hoga.**
Wo suggest karega ki:

1. XE.com jese site check karo
2. Currency converter app use karo
3. Bank ya Google par conversion rate dekho

---

### 2️⃣ OpenAI Agents SDK use karte hue:

```python
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

set_tracing_disabled(disabled=True)

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL
)

async def main():
    agent = Agent(
        name="LahoreTA",
        instructions="You only respond in english.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(
        agent,
        "What is your name?.",
    )
    print(result.final_output)

asyncio.run(main())
```

📌 Iska output ye hoga:

**"Mera koi naam nahi hai, main ek AI model hoon. Aap mujhe koi bhi naam de sakte hain agar aapko acha lage."**

---

```python
response.json()
```

Output ek aur assistant response deta hai:

**"Hello! How can I help you today?..."**

---

🧾 **Note:**
Agar aap Colab ka paid version use kar rahe ho, to aap contracts ko cancel bhi kar sakte ho.
