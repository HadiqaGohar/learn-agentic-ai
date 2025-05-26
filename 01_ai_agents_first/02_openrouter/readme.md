# OpenRouter: 50 Free LLMs ka Unified Interface
| Code Example: Basic aur OpenAI Agents SDK OpenRouter ke sath

OpenRouter ab DeepSeek V3 0324 aur 50+ aur models bilkul free support karta hai. In me se zyadatar models OpenAI Chat Completion API standard ko follow karte hain.

🔗 https://openrouter.ai/deepseek/deepseek-chat-v3-0324:free

Aap OpenRouter Quickstart Guide aur Connecting to OpenRouter from Python se shuru kar sakte hain.

---

## **Rate Limits Overview**

Large Language Models (LLMs) API rate limits are typically measured across several dimensions:

* **Requests per Minute (RPM)**
* **Tokens per Minute (TPM)**
* **Requests per Day (RPD)**

---

### **OpenRouter Free Models — Rate Limits**

OpenRouter’s free models generally enforce the following global rate limits:

* **200 Requests per Day (RPD)** — Across all free models
* **20 Requests per Minute (RPM)** — For some models (as specified in documentation)

> **Note:** These limits apply to models with IDs ending in `:free`.

---

### **Google Gemini — Free Tier Rate Limits**

Refer to official documentation:
🔗 [Gemini API Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits)

#### **Free Tier Limits (Gemini 2.0 Flash and Flash-Lite)**

| Model                     | Requests per Day (RPD) | Requests per Minute (RPM) | Tokens per Minute (TPM) |
| ------------------------- | ---------------------- | ------------------------- | ----------------------- |
| **Gemini 2.0 Flash**      | 1,500 RPD              | 15 RPM                    | 1,000,000 TPM           |
| **Gemini 2.0 Flash-Lite** | 1,500 RPD              | 30 RPM                    | 1,000,000 TPM           |

These limits are generous enough for **development and testing**, making both Gemini 2.0 Flash and Flash-Lite ideal choices for such use cases.

Additionally, **both models** are compatible with:

* **OpenAI Chat Completion API**
* **OpenAI Agents SDK**

Documentation for compatibility:
🔗 [Using Gemini with OpenAI API](https://ai.google.dev/gemini-api/docs/openai)

---

### **Usage Strategy**

* **Primary for Development & Testing**:
  Use **Google Gemini 2.0 Flash** and **Flash-Lite** for regular development workflows due to their higher RPD and RPM limits.

* **Backup Option**:
  Use **OpenRouter free APIs** when quick testing across various models is required, despite the stricter **200 RPD** limitation.

GitHub Reference:
🔗 [Panaverse – Hello Agent Example](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/04_hello_agent)

---

## **What is OpenRouter?**

**OpenRouter** is a powerful platform that offers unified access to a wide range of **Large Language Models (LLMs)** from multiple providers. These include both commercial providers such as **OpenAI** and **Anthropic**, as well as leading **open-source models** like **Mistral** and **LLaMA**.

OpenRouter simplifies the integration of these models by exposing a **single API endpoint**, enabling developers to seamlessly switch between different models without modifying their core application logic. This abstraction also optimizes requests for **cost-efficiency**, **performance**, and **availability**, dynamically routing to the most suitable provider based on factors such as **price**, **latency**, and **uptime**.

---

## **User Interface and API Access**

OpenRouter offers both a **web-based user interface** and a **developer-friendly API**:

### 🔹 **User Interface**

* Interactive **multi-model chatroom**
* Dashboard to manage **accounts**, track **usage**, and monitor **token consumption and billing**

### 🔹 **API**

* A standardized interface designed for developers
* Enables seamless integration of LLMs into apps
* Supports structured interactions and tooling

---

## **Compatibility with OpenAI Chat Completion API**

OpenRouter is **highly compatible** with the **OpenAI Chat Completion API**, closely mirroring its:

* **Endpoints**
* **Payload structure**
* **Parameter configuration**

This means developers already using OpenAI APIs can often switch to OpenRouter by **simply updating the base URL and API key**, making it ideal for rapid prototyping or cost-sensitive deployments without rewriting code.

---

## **Support for Function Calling**

OpenRouter supports **function calling** (also referred to as **tool calling**), a feature that allows LLMs to interact with external tools based on user input. This makes it possible to build intelligent agents that can trigger APIs like:

* Weather data
* Calendars
* Calculators
* Custom user-defined functions

Function calling is **standardized** across supported models, ensuring consistent behavior regardless of the underlying provider.

---

## **Model Hosting Strategy: Proxy, Not Host**

Rather than hosting LLMs directly, **OpenRouter functions as a proxy**, routing API requests to third-party providers. This architecture enables access to **over 200 LLMs** while offloading the complexity and cost of infrastructure.

* OpenRouter handles **authentication**, **request formatting**, and **provider-specific translations**
* Developers benefit from a **single, unified interface** while leveraging a vast and evolving ecosystem of LLMs


---

## **Survey Note: OpenRouter Ka Mukammal Jaiza (Roman Urdu)**

**OpenRouter** aik aisa platform hai jo users ko alag alag **LLMs (Large Language Models)** tak asaani se access dene ke liye banaya gaya hai. Yeh platform **user interface aur API** dono provide karta hai taa keh developers, researchers, aur AI users isay efficiently use kar sakein.

---

### 🖥 **Platform Overview aur Interface**

OpenRouter aik **central platform** hai jahan aap multiple companies ke AI models ko use kar saktay hain jaise:

* **OpenAI**, **Anthropic**, **Google**, **Meta**
* Aur open-source models jaise **Mistral** aur **LLaMA**

Iska faida yeh hai keh aapko har model ke liye alag alag API keys ya accounts manage nahi karne partay.

🔹 **User Interface**:

* Bohat hi asaan aur user-friendly hai.
* Aik **chatroom** bhi diya gaya hai ([https://openrouter.ai/chat](https://openrouter.ai/chat)) jahan aap multiple models se baat kar saktay hain.
* Yeh chatroom **1.5 billion tokens** support karta hai — yani bohat zyada data kaam mein liya ja sakta hai.
* Aap apna usage, token count, aur credits **Activity Page** se dekh saktay hain.

🔹 **Account Tools**:

* Tokens ka input/output, total cost waghera har cheez track ki ja sakti hai.

---

### 🛠 **API aur Developer Features**

OpenRouter ka API **OpenAI ke Chat Completion API** ke saath compatible hai. Iska matlab:

* Agar aap pehle se OpenAI use kar rahay hain to aapko sirf API key aur base URL change karna hoga:

  * URL: `https://openrouter.ai/api/v1`

API developers ke liye design kiya gaya hai jahan:

* `model`, `messages`, `temperature`, `max_tokens` jaise parameters use kiye jate hain.
* Aap easily apna code OpenRouter pe shift kar saktay hain bina bohat zyada changes kiye.

---

### ⚙️ **Function Calling (Tool Calling)**

Yeh feature allow karta hai keh AI aapko kisi external tool ka use suggest kare based on aapka input. Jaise:

* Agar user mausam ka poochay, to AI weather API ko call karne ka suggestion de sakta hai.

Ismein:

* Aap tools ka JSON schema API request mein define karte hain.
* AI decide karta hai kaunsa tool use karna hai aur kin arguments ke saath.
* Execution developer ke code mein hoti hai.

Lekin har model yeh feature support nahi karta. Jaise:

* GPT-4o (OpenAI) aur Claude (Anthropic) support karte hain.
* Lekin OpenRouter ensure karta hai keh agar aap `tools` parameter use karte hain, to request sirf unhi models ko bheji jaye jo support karte hain.

---

### 🧠 **Model Hosting — Host ya Proxy?**

OpenRouter **khud models host nahi karta**, yeh sirf **proxy** ka kaam karta hai. Yani:

* Jab aap request bhejtay hain to OpenRouter woh request third-party providers (jaise Together AI, AWS, Fireworks) ko bhejta hai.
* Response ko format karke aapko wapis deta hai.
* Yeh tareeqa cost aur speed dono ke liye optimize hai.

Documentation aur Reddit posts mein bhi yeh confirm kiya gaya hai keh OpenRouter sirf request routing aur formatting karta hai.

---

### 💲 **Pricing aur Extra Features**

Pricing **token-based** hai. Kuch models **free** bhi hote hain jab keh kuch ke liye **credits** chahiye hotay hain. Features mein shamil hain:

* **Playground** jahan aap test kar saktay hain
* **Streaming support** (real-time response)
* **Prompt logging** (aap chahein to enable/disable kar saktay hain)
* **Load balancing** aur **fallbacks** for high availability
* Advanced config: aap specify kar saktay hain keh kis type ke provider ko request di jaye (price ya specs ke basis par)

---

### 🔍 **User Experience aur Comparison**

OpenRouter ka use karna asaan hai, especially un logon ke liye jo multiple APIs handle nahi karna chahte:

* Chatroom interface basic lekin effective hai for testing.
* API compatibility se developers ko asaani hoti hai shift karne mein.
* Lekin kuch models ka **free tier jaldi exhaust ho jata hai**, to top-up zaroori hota hai.

---

### 📊 **Table: OpenRouter Features Summary**

| Feature               | Description                             |
| --------------------- | --------------------------------------- |
| **User Interface**    | Chatroom, account tools                 |
| **API Compatibility** | OpenAI API ke saath compatible          |
| **Function Calling**  | Tools suggest karne ka feature          |
| **Model Hosting**     | Models host nahi karta — sirf proxy hai |
| **Pricing**           | Tokens per pay karna hota hai           |
| **Extras**            | Playground, streaming, logging etc.     |

---

### 📚 **Sources (Key Citations)**

* OpenRouter Official Site: [https://openrouter.ai](https://openrouter.ai)
* Quickstart Guide
* Tool Calling Documentation
* Reddit: r/ChatGPTCoding
* Medium: LangChain Integration Article
* Novelcrafter Help Center
* Provider Routing Guide


---

**What Are Free Models on OpenRouter?**
OpenRouter kai tarah ke large language models (LLMs) ek hi interface se access karne ki sahulat deta hai, aur in mein se kuch models bilkul free hain. Ye free models bina kisi cost ke use kiye ja sakte hain, magar in par rate limits hoti hain, jaise ke 20 requests per minute aur 200 requests per din, taake usage manage ho sake.

**How Many Are There?**
OpenRouter ke official X account ke ek recent post ke mutabiq, jo 23 March 2025 ko hua tha, lagta hai ke abhi tak 50 free models available hain. In mein se 6 models ke paas 1 million tokens ya us se zyada context window hai, jo ke un users ke liye ek surprising aur acha option hai jinhein high-capacity free models chahiye.

**Survey Note: Comprehensive Details on Free Models on OpenRouter**
24 March 2025 tak, OpenRouter, jo ke ek platform hai jo kai providers ke LLMs ko ek jagah se access karne deta hai, users ko free models ki ek range provide karta hai. Yeh section in free models ki tadaad, khasoosiyat, aur unke background ko detail mein samjhata hai, taake developers, researchers, aur enthusiasts ko behtareen samajh mile.

**Overview of OpenRouter and Free Models**
OpenRouter asal mein ek proxy ki tarah kaam karta hai, jo API requests ko third-party providers tak forward karta hai jahan asli model inference hota hai, na ke khud models host karta ho. Is tarah se 200 se zyada models available hain, jin mein se kuch free hain matlab users bina token charges ke use kar sakte hain. Lekin free models par aksar usage restrictions hoti hain, jese ke rate limits, taake fair use aur server load manage ho sake.

"Free" ka matlab yahan aam tor par zero cost per token hota hai, magar users ko account banana zaroori hota hai, aur 20 requests per minute aur 200 per din ki limit bhi lag sakti hai (API Rate Limits documentation ke mutabiq). Ye limits abuse rokne ke liye hain, khaas tor par free variants jo aksar IDs ke end mein "\:free" ke saath hote hain.

**Determining the Number of Free Models**
Research se maloom hua ke March 2025 tak OpenRouter par 50 free models hain. Ye number OpenRouter ke official X post se liya gaya hai, jisme likha tha, "There are now 50 free models on OpenRouter including 6 with 1M+ context windows!" Yeh post 23 March 2025 ko subah 10:23 AM PDT par hua tha. Isi din @TonyLovesAI ne bhi ek post kiya tha jisme kaha gaya, "OpenRouter offers you 50 free AI models!"

Ye number khaas hai kyun ke 6 models itni badi context window ke saath free mein mil rahe hain, jo high-capacity free options ke liye zabardast hai.

**Usage and Limitations**
Free models personal ya low-usage projects ke liye bohat faida mand hain, jaise ke @lucifer\_x007 ne 23 March 2025 ko kaha, "Use the free tier models from openrouter if you feel you'll be rate limited." Ye API rate limits ke sath match karta hai jo usage ko manage karta hai taake free access providers ko overwhelm na kare.

@geekbb ne 29 December 2024 ko bataya ke Gemini models OpenRouter par free hain magar un par bhi 20 requests per minute aur 200 per din ki limits hain. Ye limitations samajhna zaroori hai kyunki wo project scalability ko affect kar sakti hain. Lekin 50 free models ke sath, jin mein high-context options bhi hain, OpenRouter aik bohat acha resource hai.

---

**Table: Summary of Free Models on OpenRouter**

| Aspect                | Details                                                                               |
| --------------------- | ------------------------------------------------------------------------------------- |
| Number of Free Models | Research ke mutabiq 50 (23 March 2025 ke posts)                                       |
| Context Windows       | 6 models 1M+ tokens ke context window ke sath                                         |
| Usage Limits          | 20 requests per minute, 200 requests per day                                          |
| Identification        | IDs aksar "\:free" par end hoti hain, jaise OpenChat 3.5 (free)                       |
| Community Feedback    | Free models RP (role play), personal projects ke liye ache hain, magar limits ke sath |

**Comparative Analysis and User Experience**
Users ke liye 50 free models milna ek achi baat hai, khaas tor par jab high-context models bhi free milte hain jo aam tor par expect nahi kiye jate. Community feedback se pata chalta hai ke OpenRouter "game-changer" hai jo kai free AI models ek sath access karne ka mauqa deta hai, jo cost-conscious developers ke liye bohat useful hai. Lekin kuch models, jaise OpenChat 3.5, kabhi kabhi free nahi hote, jo kuch discrepancies ya status changes ko dikhata hai.

**Conclusion**
Summary yeh hai ke March 2025 tak OpenRouter par 50 free models hain, jin mein 6 models ke paas 1 million+ tokens ke context windows hain. Yeh models rate limits ke sath aate hain, magar phir bhi OpenRouter un users ke liye bohat acha platform hai jo free mein LLMs access karna chahte hain.

---

**Key Citations**

* Models | OpenRouter
* OpenRouter Models | Access 300+ AI Models Through One API
* API Rate Limits - Manage Model Usage and Quotas
* Use OpenRouter Models
* OpenRouter free models – not free? | WordPress.org
* r/SillyTavernAI on Reddit: Free RP models on OpenRouter
* How to Access Multiple Free AI Models at Once - Showcase - Make Community
* OpenRouterAI X post
* TonyLovesAI X post
* lucifer\_x007 X post
* geekbb X post

---

