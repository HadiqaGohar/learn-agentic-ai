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
