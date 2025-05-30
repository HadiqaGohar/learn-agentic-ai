# Guardrails: Aapke Agents Ke Saath Saath Chalne Wale Pehredar!

**Guardrails** aapke agents ke **parallel (saath saath)** chalte hain. Inka kaam user ke input ko **check karna aur validate (tasdeeq karna)** hai.

Misaal ke taur par, imagine karein aapke paas ek agent hai jo customer ki madad ke liye ek bohot hi smart (aur is wajah se slow/mehnga) model istemal karta hai. Aap bilkul nahi chahenge ke koi bad-niyat user us model se apne math homework mein madad maangna shuru kar de.

Is se bachne ke liye, aap ek **Guardrail** chala sakte hain ek tez/saste model ke saath. Agar Guardrail ko koi galat ya bad-niyat istemal nazar aata hai, to woh foran ek error de sakta hai. Is se aapka mehnga model chalne se ruk jaayega aur aapka waqt aur paisa bachega.

---
### Guardrails Ki Do Types:

1.  **Input Guardrails:**
    * Ye Guardrails **shuruati user input** par chalte hain. Yani, user ka sawal agent tak pahunchne se pehle hi check ho jaata hai.

2.  **Output Guardrails:**
    * Ye Guardrails **agent ke final output** par chalte hain. Yani, agent ne jo jawab diya hai, woh user tak jaane se pehle check hota hai.
  

---


### Input Guardrails: Kaise Kaam Karte Hain?

**Input Guardrails** teen (3) steps mein kaam karte hain:

1.  **Pehla Step:**
    * Guardrail ko wohi **input milta hai jo agent ko diya gaya hai**. Yani, user ka asal sawal.

2.  **Dusra Step:**
    * Ab **guardrail function chalta hai** aur ek **`GuardrailFunctionOutput`** banata hai. Is output ko phir ek **`InputGuardrailResult`** mein wrap kiya jaata hai.

3.  **Teesra Step:**
    * Aakhir mein, hum check karte hain ke **`.tripwire_triggered`** `true` hai ya nahi. Agar ye `true` hota hai, to ek **`InputGuardrailTripwireTriggered`** exception uthaya jaata hai. Is se aap user ko sahi jawab de sakte hain ya us galti ko handle kar sakte hain.

---

**Ek Zaroori Baat:**

**Input Guardrails** sirf **user input** par chalne ke liye banaye gaye hain. Iska matlab hai ke agent ke guardrails tabhi chalenge jab woh agent **pehla agent** ho jo input receive kar raha hai.

Aap soch sakte hain ke "guardrails" property agent par kyun hai, "Runner.run" ko kyun nahi dete? Iski wajah ye hai ke guardrails aksar **agent se mutaliq (related)** hote hain. Mukhtalif agents ke liye aap mukhtalif guardrails istemal karna chahenge, isliye code ko agent ke saath hi rakhna **parhne mein asaan (readable)** hota hai.



---


### Output Guardrails: Kaise Kaam Karte Hain?

**Output Guardrails** bhi teen (3) steps mein kaam karte hain:

1.  **Pehla Step:**
    * Guardrail ko **agent ka final output milta hai**. Yani, agent ne jo jawab tayyar kiya hai.

2.  **Dusra Step:**
    * Ab **guardrail function chalta hai** aur ek **`GuardrailFunctionOutput`** banata hai. Is output ko phir ek **`OutputGuardrailResult`** mein wrap kiya jaata hai.

3.  **Teesra Step:**
    * Aakhir mein, hum check karte hain ke **`.tripwire_triggered`** `true` hai ya nahi. Agar ye `true` hota hai, to ek **`OutputGuardrailTripwireTriggered`** exception uthaya jaata hai. Is se aap user ko sahi jawab de sakte hain ya us galti ko handle kar sakte hain.

---

**Ek Zaroori Baat:**

**Output Guardrails** sirf **agent ke final output** par chalne ke liye banaye gaye hain. Iska matlab hai ke agent ke output guardrails tabhi chalenge jab woh agent **aakhri agent** ho jo jawab de raha hai. Input guardrails ki tarah hi, hum aisa isliye karte hain kyunke guardrails aksar **agent se mutaliq (related)** hote hain. Mukhtalif agents ke liye aap mukhtalif guardrails istemal karna chahenge, isliye code ko agent ke saath hi rakhna **parhne mein asaan (readable)** hota hai.


---
### Tripwires: Guardrails ka Alarm System

**Tripwires** ek tarah ka alarm system hain Guardrails ke liye. Agar koi input ya output Guardrail ke checks mein **fail ho jaata hai**, to Guardrail is baat ka signal **tripwire** se deta hai. Jaise hi koi Guardrail tripwire trigger karta hai, hum foran **`{Input,Output}GuardrailTripwireTriggered`** exception raise kar dete hain aur Agent ka kaam wahi rok dete hain.

---
### Guardrail Ko Implement Kaise Karen?

Guardrail banane ke liye aapko ek function provide karna hota hai jo input receive karta hai aur **`GuardrailFunctionOutput`** return karta hai. Is misaal mein, humne ye kaam pichhe ek Agent ko run karke kiya hai.

```python
from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail, # Yeh decorator Input Guardrail ke liye
)

# Output ka format define kiya gaya hai
class MathHomeworkOutput(BaseModel):
    is_math_homework: bool # Kya yeh math homework hai?
    reasoning: str        # Kyun aisa kaha gaya?

# Ek agent jo homework check karega
guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput, # Output is format mein chahiye
)

# Input Guardrail function
@input_guardrail # Is decorator se pata chalta hai ke ye input guardrail hai
async def math_guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    # Guardrail agent ko chalao input check karne ke liye
    result = await Runner.run(guardrail_agent, input, context=ctx.context)

    # GuardrailFunctionOutput return karo
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        # Agar math homework hai to tripwire trigger kar do
        tripwire_triggered=result.final_output.is_math_homework,
    )

# Hamara main Customer Support Agent
agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail], # Is agent par input guardrail lagaya gaya hai
)

async def main():
    # Jab yeh code chalega, to guardrail trigger hona chahiye
    try:
        await Runner.run(agent, "Hello, can you help me solve for x: 2x + 3 = 11?")
        print("Guardrail didn't trip - this is unexpected") # Agar trip nahi hua to ghalti hai

    except InputGuardrailTripwireTriggered:
        print("Math homework guardrail tripped") # Guardrail trigger ho gaya
```

---
### Output Guardrails Bhi Isi Tarah Kaam Karte Hain

Output Guardrails bhi Input Guardrails se milte-julte hain.

```python
from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered, # Yeh exception Output Guardrail ke liye
    RunContextWrapper,
    Runner,
    output_guardrail, # Yeh decorator Output Guardrail ke liye
)

# Agent ke final message ka output format
class MessageOutput(BaseModel):
    response: str

# Guardrail agent ke output ka format
class MathOutput(BaseModel):
    reasoning: str
    is_math: bool # Kya output mein math hai?

# Ek agent jo output mein math check karega
guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the output includes any math.",
    output_type=MathOutput, # Output is format mein chahiye
)

# Output Guardrail function
@output_guardrail # Is decorator se pata chalta hai ke ye output guardrail hai
async def math_guardrail(
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    # Guardrail agent ko chalao output check karne ke liye
    result = await Runner.run(guardrail_agent, output.response, context=ctx.context)

    # GuardrailFunctionOutput return karo
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        # Agar output mein math hai to tripwire trigger kar do
        tripwire_triggered=result.final_output.is_math,
    )

# Hamara main Customer Support Agent
agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    output_guardrails=[math_guardrail], # Is agent par output guardrail lagaya gaya hai
    output_type=MessageOutput, # Agent ka apna output format
)

async def main():
    # Jab yeh code chalega, to guardrail trigger hona chahiye
    try:
        # Agent ko math ka sawal diya gaya, iska jawab math wala hoga jo guardrail trip karega
        await Runner.run(agent, "Hello, can you help me solve for x: 2x + 3 = 11?")
        print("Guardrail didn't trip - this is unexpected") # Agar trip nahi hua to ghalti hai

    except OutputGuardrailTripwireTriggered:
        print("Math output guardrail tripped") # Guardrail trigger ho gaya
```

---

Yeh code Guards aur Tripwires ke concept ko achhe se samjhata hai, khas taur par ke kaise woh Agent ke execution flow ko control karte hain. Aapne dekha ke Input Guardrail user ke sawal ko check karta hai, aur Output Guardrail Agent ke jawab ko.

### Full Source Code 

```
# zaroori modules import kiye ja rahe hain
import os  # system-level environment variables handle karne ke liye
from dotenv import load_dotenv  # .env file se environment variables load karne ke liye
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, InputGuardrail, GuardrailFunctionOutput
from agents.run import RunConfig  # run karne ke config ke liye
from pydantic import BaseModel  # data validation ke liye (type checking)

# .env file se environment variables load karo
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")  # GEMINI_API_KEY environment se nikala gaya

# agar key nahi mili to error throw karo
if not gemini_api_key:
    raise ValueError("Your GEMINI_API_KEY is not working!")  # key missing hone par error dikhai jati hai

# External LLM (Language Model) client configure karo
external_client = AsyncOpenAI(
    api_key=gemini_api_key,  # upar wali key use kar ke
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Gemini ka endpoint
)

# Gemini model ka wrapper banaya gaya
model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash",  # Gemini 2.0 ka fast version use ho raha hai
)

# run ke configuration set karo
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True  # debug tracing band hai
)

# yeh ek data model hai jo guardrail ke output ko validate karega
class HomeworkOutput(BaseModel):
    is_homework: bool  # kya user ka sawal homework se related hai?
    reasoning: str  # reasoning batayega ke kyu aesa kaha gaya

# guardrail agent banaya gaya — iska kaam hai dekhna ke sawal homework ka hai ya nahi
guardrail_agent = Agent(
    name="Guardrail check",  # agent ka naam
    instructions="Check if the user is asking about homework.",  # kya karna hai agent ko
    output_type=HomeworkOutput,  # output kis format mein chahiye
    model=model  # kaunsa model use hoga
)

# Math subject ke liye alag agent banaya gaya
math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",  # jab agent forward hoga to yeh description dikhegi
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples.",  # is agent ko math ka expert banaya gaya
    model=model
)

# History subject ke liye bhi alag agent
history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",  # handoff description
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",  # yeh historical cheeze explain karega
    model=model
)

# ----------------------------------------------IMPORTANT FUNCTIONALITY------------------------------------------------


# yeh guardrail function hai — yeh dekhega ke input homework ka hai ya nahi
# agar nahi hai to bhi program rokega nahi

# ctx (Context - Mahaul ya Haalaat):
async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context, run_config=config)  # guardrail agent ko run karo
    final_output = result.final_output_as(HomeworkOutput)  # output ko HomeworkOutput format mein convert karo
    if not final_output.is_homework:
        print("⚠️ Warning: This input does not appear to be a homework question.")  # agar homework nahi hai to warning
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=False  # input ko allow karo aage jane ke liye
    )

# ----------------------------------------------IMPORTANT FUNCTIONALITY------------------------------------------------






# yeh main agent hai jo decide karega ke kaunsa tutor (math ya history) use karna hai
# ye main agent he last wala jis ke pass sub info he
triage_agent = Agent(
    name="Triage Agent",  # agent ka naam
    instructions="You determine which agent to use based on the user's homework question.",  # iska kaam routing karna hai
    handoffs=[history_tutor_agent, math_tutor_agent],  # dono subject agents ko handoff ke liye register kiya gaya
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),  # guardrail function attach kiya gaya
    ],
    model=model
)

# ab hum triage agent ko run kar rahe hain history related question ke liye
result = Runner.run_sync(triage_agent, "Add both 2 and 3 and give me answer?", run_config=config)
print("\n✅ Result 1:", result.final_output)  # output print karo

# ab ek philosophical question diya gaya hai — yeh guardrail se pass ho jayega lekin warning milegi
result = Runner.run_sync(triage_agent, "What is life", run_config=config)
print("\n✅ Result 2:", result.final_output)  # output print karo

result = Runner.run_sync(triage_agent, "Who is the first governor of pakistan?", run_config=config)
print("\n✅ Result 3:", result.final_output)
```
