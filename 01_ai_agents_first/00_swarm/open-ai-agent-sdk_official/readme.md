
# **OpenAI Agents SDK: Kya Hai Aur Kaise Kaam Karta Hai 🤖✨**

OpenAI Agents SDK ek aasaan aur halka-phulka package hai jo aapko intelligent AI apps banane mein madad karta hai. Yeh hamare pehle ke experimental agent project, "Swarm," ka ek production-ready upgrade hai. Is SDK mein bohot kam lekin bohot powerful cheezein hain:

1. **Agents (ایجنٹس) 🧠:**
   Ye asl mein LLMs (Large Language Models) hotay hain jinhe khaas instructions (hidayat) aur tools (auzaar) diye jaate hain.

   * **Explanation:** Socho ek insaan hai jise kuch kaam karna hai. "Instructions" us insaan ko batate hain ke kya karna hai aur kaise karna hai (maslan, "Customer ki shikayat hal karo"). "Tools" us insaan ke haath mein maujood cheezein hain jinse woh kaam karega (maslan, computer, phone, ya koi software). Isi tarah, Agent ek AI hai jise hum batate hain ke uska maqsad kya hai aur woh kaun se kaam kar sakta hai (tools ke zariye).

2. **Handoffs (ہینڈ آفز) 🤝:**
   Ye agents ko dusre agents ko khaas kaam delegat (saupne) karne ki ijazat dete hain.

   * **Explanation:** Imagine karo ek company mein alag-alag departments hain. Jab customer support ka bandah kisi technical masle ko hal nahi kar pata, toh woh usko "handoff" kar deta hai technical department ko. Isi tarah, jab ek AI agent (maslan, ek general query agent) kisi bohot khaas ya mushkil sawal ka jawab nahi de pata, toh woh us sawal ko us agent ko "handoff" kar deta hai jo us topic ka specialist hai (maslan, data analysis agent ya product support agent). Isse kaam theek tareeqe se divide ho jata hai.

3. **Guardrails (گارڈ ریلز) 🛡️:**
   Ye inputs (daakhil kiye gaye data) ko validate (tasdeeq) karne mein madad karte hain, taake agents ko sirf sahi aur relevant information mile.

   * **Explanation:** Guardrails sarak ke kinare lagi deewaron ki tarah hain jo gariyon ko sarak se utarne se rokti hain. Yahan, Guardrails ye ensure karte hain ke agent ko jo information mil rahi hai ya jo information agent bahar de raha hai, woh safe, relevant, aur hamari guidelines ke mutabiq ho. Maslan, agar koi user koi inappropriate ya harmful content input kare toh Guardrail usko rokh dega. Ya agar agent ko ek khaas format mein output dena hai (jaise koi number ya email address), toh Guardrail ensure karega ke output usi format mein ho.

---

**In sab ko mila kar kya hota hai? 🤔**

Jab aap in primitives (bunyadi cheezon) ko Python programming language ke saath istemal karte hain, toh aap tools aur agents ke darmiyan bohot complex (pecheeda) rishte bana sakte hain. Isse aap real-world applications (haqeeqi dunya ki apps) bana sakte hain bina zyada mushkil programming seekhe. Matlab, aap AI-powered software bana sakte hain jo asal zindagi ke maslon ko hal karega.

---

**Built-in Tracing (بلٹ ان ٹریسنگ) 🔍:**

Is SDK ki ek khaas baat iska "built-in tracing" feature hai.

* **Explanation:** Tracing bilkul ussi tarah hai jaise aap kisi cheez ke pichhe uske qadam dekhte hain. Jab aap agentic flow chalate hain, toh tracing aapko har qadam dikhata hai jo agent le raha hai – woh kya soch raha hai, kaun sa tool use kar raha hai, kis agent ko handoff kar raha hai, aur guardrails kaise kaam kar rahe hain. Isse aap apne agent ke behavior ko visualize (tasawwur karna) aur debug (galatiyan theek karna) kar sakte hain. Aap isse agent ki performance ko evaluate (jaanch-partaal) bhi kar sakte hain aur yahan tak ke apne models ko apni specific app ke liye fine-tune (behtar banana) bhi kar sakte hain.

---

## **Aksar Puche Jaane Waale Sawaalat (FAQ) - OpenAI Agents SDK ❓**

### Q1: OpenAI Agents SDK kya hai? 🤔

OpenAI Agents SDK ek halka-phulka aur istemal karne mein aasaan Python package hai jo aapko zameen AI applications banane mein madad karta hai. Yeh hamare pichhle experimental agent framework, **Swarm**, ka ek production-ready upgrade hai. SDK kuch khaas aur powerful bunyadi cheezon par tawajjo deta hai: **Agents**, **Handoffs**, aur **Guardrails**. Yeh aapko kam complexity ke saath mushkil agentic workflows banane ki ijazat deta hai.

---

### Q2: SDK mein **Agents** kaise kaam karte hain? 🧩

**Agents** bunyadi taur par Large Language Models (LLMs) hotay hain jinhe khaas **instructions** (unki marzi aur kaise behave karna hai) aur kuch **tools** diye jaate hain. Ye tools agent ko bahar ki duniya se interact karne, kaam karne (jaise web search karna, APIs call karna, ya files padhna), aur apne diye gaye tasks ko mukammal karne ki ijazat dete hain. Agent ko aise samjhein jaise ek AI worker jise ek job description aur kaam karne ke liye zaroori saamaan diya gaya ho.

---

### Q3: **Handoffs** kya hain aur yeh kion zaroori hain? 🔄

**Handoffs** agents ko doosre specialized agents ko tasks delegat (saupne) karne ki ijazat dete hain. Agar ek agent ye samjhta hai ke doosra agent kisi khaas task ke hisse ko sambhalne ke liye zyada behtar ya zyada maahir hai, to woh us hisse ko expert agent ko "hand off" kar deta hai. Yeh mustahkam multi-agent systems banane ke liye bohot zaroori hai jahan mukhtalif agents mukhtalif functions mein maahir hotay hain, is baat ko yakeeni banate hue ke tasks behtareen tareeqe se sab se qabil hisse ko bheje jaayen.

---

### Q4: SDK mein **Guardrails** ka maqsad kya hai? 🛑

**Guardrails** security aur validation mechanisms hain. Inka istemal ye yakeeni banane ke liye kiya jata hai ke agents ko milne waale inputs sahi hon aur agents ke zariye generate kiye gaye outputs mehfooz, relevant, aur pehle se tay shuda qawaneen ya formats par poora utarte hon. Maslan, ek guardrail ek appointment chatbot ko bahar ke links share karne se rok sakta hai ya ye yakeeni bana sakta hai ke agent ka output hamesha ek khaas data structure mein ho. Ye ghair-mutaliqa rawaiye ya galat information flow ko rokne ke liye hudood (boundaries) ka kaam karte hain.

---

### Q5: **Built-in Tracing** development mein kaise madad karta hai? 🛠️

**Built-in Tracing** aapke agentic workflows ko visualize aur debug karne ke liye ek qeemti feature hai. Yeh aapko agent ke sochne ke tareeqe ko qadam-ba-qadam dekhne ki ijazat deta hai, jismein yeh kab tools call karta hai, faisle leta hai, ya handoff karta hai. Agar koi error ho, to tracing aapko bilkul theek jagah aur wajah maloom karne mein madad karta hai, jis se debugging aur optimization ka process bohot zyada asaan ho jaata hai.

---

### Q6: **Swarm** aur **OpenAI Agents SDK** ke darmiyan kya rishta hai? Kya SDK Swarm ke data ke liye abstraction ka istemal karta hai? 🔗

Ji haan, OpenAI Agents SDK apne predecessor **Swarm** ki complexity ko **abstract** karta hai. Swarm ek pehle ka experimental framework tha, aur SDK us par iski andaruni pecheeda details ko chhupa kar aur ek simplified, zyada accessible interface faraham kar ke aage badhta hai. Iska matlab hai ke developers ko Swarm ke bunyadi architecture ko samajhne ki zaroorat nahi hoti; woh seedhe SDK ke high-level primitives (Agents, Handoffs, Guardrails) ka istemal kar ke powerful applications bana sakte hain, Swarm ki asl complexity se deal kiye baghair. Bunyadi taur par, SDK Swarm ki core functionalities ke upar ek user-friendly layer ka kaam karta hai.

---
---
---


## Agents SDK Ko Kyun Istimal Karein? 🤖✨ (Why use the Agents SDK?)

OpenAI Agents SDK ko do khaas usoolon (design principles) ko zehn mein rakh kar banaya gaya hai:

1. **Zaroori Features, Magar Seekhna Aasaan 📚:** Is mein itne features hain ke yeh aapke liye kaaram ho, lekin primitives (bunyadi cheezein) itni kam hain ke isay jaldi seekha ja sake. Matlab, yeh powerful bhi hai aur isay samajhna bhi mushkil nahi.
2. **Out-of-the-Box Acha Kaam 🚀, Magar Aapki Marzi Se Customization 🎨:** Yeh bina kisi khaas set up ke foran acha kaam karta hai, lekin aap apni marzi ke mutabiq har cheez ko customize (tarteeb) kar sakte hain.

---

### SDK Ke Bunyadi Features (Main Features of the SDK) 🛠️

Yahaan SDK ke bunyadi features ki tafseel hai:

#### 1. Agent Loop (ایجنٹ لوپ) 🔄

Is mein ek built-in agent loop hai jo **tools ko call karna**, **results ko LLM tak bhejna**, aur tab tak loop karte rehna jab tak LLM apna kaam mukammal na kar le, sab kuch khud hi sambhal leta hai.

* **Explanation:** Sochian agent ko koi kaam diya gaya hai. Agent loop us kaam ko mukammal karne ke liye zaroori steps ko khud-ba-khud control karta hai. Maslan, agar agent ko web search karni hai, to loop tool ko call karega, search ke results LLM (AI brain) ko dega, aur agar mazeed search ki zaroorat hai to ye cycle (dauraan) chalata rahega jab tak ke LLM apna jawab tayar na kar le. Aapko is saare process ko manually code karne ki zaroorat nahi padti.

#### 2. Python-First (پائتھن فرسٹ) 🐍

Nayi abstractions (pecheeda concepts) seekhne ki bajaye, aap Python ki built-in language features ko istemal kar sakte hain agents ko orchestrate (munazzam) aur chain (ek doosre se jorna) karne ke liye.

* **Explanation:** Iska matlab hai ke agar aapko Python aati hai, to aap is SDK ko aasani se use kar sakte hain. Aapko koi bilkul nayi programming language ya mushkil tareeqay nahi seekhne padenge sirf agents ko apas mein jorne ya unse kaam karwane ke liye. Python ki apni functions aur libraries ka istemal karte hue aap agents ke flows ko control kar sakte hain.

#### 3. Handoffs (ہینڈ آفز) 🤝

Yeh ek bohot powerful feature hai jo **multiple agents ke darmiyan coordination (talamel) aur delegation (zimmedari saupna)** mein madad karta hai.

* **Explanation:** Agar aapka AI system ek se zyada agents par mushtamil hai aur har agent ka apna khaas kaam hai, to Handoffs unhein apas mein smoothly kaam tafweez karne ki ijazat dete hain. Misal ke taur par, ek general query agent kisi scientific sawal ko ek scientific research agent ko hand off kar sakta hai. Is se poora system zyada efficient aur focused ho jata hai.

#### 4. Guardrails (گارڈ ریلز) 🚧

Yeh aapko **input validations aur checks** ko apne agents ke parallel mein chalane ki ijazat dete hain, aur agar checks fail ho jaayen to kaam ko foran rokte hain.

* **Explanation:** Guardrails aik security aur quality check point ki tarah kaam karte hain. Jab bhi agent ko koi input milta hai ya woh koi output generate karne wala hota hai, Guardrails usay check karte hain. Agar input ya output hamari guidelines ke mutabiq nahi hai (maslan, galat format, ya harmful content), to Guardrail us process ko waheen rok deta hai. Is se galat ya gair-zaroori information ko system mein aanay ya bahar jaane se roka jaata hai.

#### 5. Function Tools (فنکشن ٹولز) ⚙️

Aap kisi bhi Python function ko ek tool mein badal sakte hain, **automatic schema generation** aur **Pydantic-powered validation** ke saath.

* **Explanation:** Ye SDK ki aik bohot bari sahulat hai. Agar aapne Python mein koi function likha hai jo koi khaas kaam karta hai (maslan, database se data nikalna, email bhejna, ya weather check karna), to aap us function ko Agent ke liye aik tool bana sakte hain. SDK khud-ba-khud us tool ki tafseelat (schema) generate kar dega, aur Pydantic ki madad se us tool ke inputs aur outputs ki validation bhi ho sakegi, jis se ghaltiyon ka imkaan kam ho jayega.

#### 6. Tracing (ٹریسنگ) 🔍

Built-in tracing aapko apne workflows ko **visualize (tasawwur karna), debug (ghaltiyan theek karna)** aur **monitor (nigraani karna)** karne ki ijazat deta hai, is ke elawa aap OpenAI ke evaluation, fine-tuning aur distillation tools ka bhi istemal kar sakte hain.

* **Explanation:** Tracing aik tarah se aapke agent ke kaam karne ka poora record rakhta hai. Aap dekh sakte hain ke agent ne kya socha, kaun sa tool use kiya, kab koi handoff kiya, aur guardrails ne kab check kiya. Yeh aapko kisi bhi masle ko samajhne aur theek karne mein bohot madad karta hai. Iske sath hi, OpenAI ke mazeed tools bhi available hotay hain jin se aap apne agents ki performance ko behtar bana sakte hain.

---
---
---


### Code Explanation: OpenAI Agents SDK (Hello World)

Yeh code aapko dikhata hai ke aap OpenAI Agents SDK ko kaise install kar sakte hain aur ek bohot hi bunyadi (basic) "Hello World" example kaise chala sakte hain.

---

### Installation (انسٹالیشن)

```bash
pip install openai-agents
```

* **Explanation:** Yeh pehla step hai. Jab aapko koi Python package istemal karna hota hai, to usay pehle apne system par install karna hota hai. `pip` Python ka package manager hai. Yeh command aapke computer par **OpenAI Agents SDK** ko download aur install kar dega. Isay chalanay ke liye aapko apna terminal (command prompt) khol kar yeh command likhna hoga.

---

### Hello World Example (ہیلو ورلڈ ایگزامپل)

```python
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)
```

* **`from agents import Agent, Runner`**
    * **Explanation:** Yeh line **OpenAI Agents SDK** se do khaas cheezein import kar rahi hai:
        * **`Agent`**: Yeh woh class hai jis se aap apna AI **agent** banate hain. Agent woh AI entity hai jo kaam karegi.
        * **`Runner`**: Yeh woh class hai jo aapke agent ko chalanay (run) mein madad karti hai.

* **`agent = Agent(name="Assistant", instructions="You are a helpful assistant")`**
    * **Explanation:** Yahan hum apna pehla **agent** bana rahe hain.
        * `name="Assistant"`: Hum is agent ko ek **naam** de rahe hain, jo "Assistant" hai.
        * `instructions="You are a helpful assistant"`: Yeh sab se ahem hissa hai. Ye agent ko bata raha hai ke uska **maqsad** kya hai aur usay kya karna hai. Yahan hum usay keh rahe hain ke "Aap ek madadgar assistant hain." Yeh uski bunyadi personality aur role set karta hai. LLM (Large Language Model) in instructions ko follow karte hue jawab dega.

* **`result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")`**
    * **Explanation:** Yeh woh line hai jahan hum apne **agent** ko **actual kaam** de rahe hain.
        * `Runner.run_sync()`: `Runner` class ka yeh method (function) agent ko **sync (synchronously)** chalata hai, matlab yeh code tab tak wait karega jab tak agent apna kaam mukammal na kar le.
        * `agent`: Hum yahan bata rahe hain ke kis **agent** ko chalana hai (jo humne "Assistant" ke naam se banaya hai).
        * `"Write a haiku about recursion in programming."`: Yeh woh **prompt** ya **sawal** hai jo hum apne agent se pooch rahe hain. Agent is instructions aur is sawal ki buniyad par apna jawab banayega.
        * `result`: Jo bhi jawab agent deta hai, woh is `result` variable mein store ho jayega.

* **`print(result.final_output)`**
    * **Explanation:** Jab agent apna jawab de chuka hota hai, to us jawab ko console (screen) par print karne ke liye yeh line istemal hoti hai. `result.final_output` agent ka aakhri aur mukammal jawab hota hai.

---

### Expected Output (Mutawaqqo Natija)

```
# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
```

* **Explanation:** Jab aap yeh code chalayenge, to aapka "Assistant" agent `instructions` aur `prompt` ki buniyad par recursion par ek haiku likh kar dega, jaisa ke upar dikhaya gaya hai.

---

### Important Note (Zaroori Hidayat)

```bash
(If running this, ensure you set the OPENAI_API_KEY environment variable)

export OPENAI_API_KEY=sk-...
```

* **Explanation:** OpenAI ke APIs (jinhein Agents SDK istemal karta hai) ko use karne ke liye aapko ek **API key** ki zaroorat hoti hai. Yeh ek khaas secret code hota hai jo aapko OpenAI ki website par milta hai jab aap account banate hain.
    * `export OPENAI_API_KEY=sk-...`: Yeh command aapke terminal mein **`OPENAI_API_KEY`** naam ka ek **environment variable** set karta hai. `sk-...` ki jagah aapko apni asal OpenAI API key paste karni hogi. Yeh key aapke code ko OpenAI ke servers se connect karne ki ijazat deti hai. Is command ko aapko code chalanay se **pehle** apne terminal mein run karna hoga.
