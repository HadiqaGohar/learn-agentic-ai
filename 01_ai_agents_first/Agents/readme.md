# Agents

---
**Agents are the core building block in your apps. An agent is a large language model (LLM), configured with instructions and tools.**

**Agents aap ki apps ke bunyadi building block hain. Agent aik bada language model (LLM) hota hai, jise hidayat aur tools ke saath configure kiya jaata hai.**
---

## Basic configuration
The most common properties of an agent you'll configure are:

Instructions: also known as a developer message or system prompt.
Model: which LLM to use, and optional model_settings to configure model tuning parameters like temperature, top_p, etc.
Tools: Tools that the agent can use to achieve its tasks.


## Bunyadi Configuration
Agent ki sab se aam khasusiyat (properties) jo aap configure karenge, woh yeh hain:

Instructions: Jise developer message ya system prompt bhi kaha jaata hai.
Model: Kaun sa LLM istemal karna hai, aur ikhtiyari (optional) model_settings jismein aap model tuning parameters jaise ke temperature, top_p, wagaira configure kar sakte hain.
Tools: Woh tools jo agent apne kaamon ko mukammal karne ke liye istemal kar sakta hai.

```
from agents import Agent, ModelSettings, function_tool

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku form",
    model="o3-mini",
    tools=[get_weather],
)
```

---

### Context
Agents are generic on their context type. Context is a dependency-injection tool: it's an object you create and pass to Runner.run(), that is passed to every agent, tool, handoff etc, and it serves as a grab bag of dependencies and state for the agent run. You can provide any Python object as the context.

### Context
Agents apni context type par generic hotay hain. Context aik dependency-injection tool hai: yeh aik object hai jo aap banatay hain aur Runner.run() ko pass kartay hain, jo har agent, tool, handoff, wagaira ko diya jaata hai, aur yeh agent run ke liye dependencies aur state ka aik "grab bag" (yani, cheezon ka majmua) ka kaam karta hai. Aap koi bhi Python object context ke tor par faraham kar sakte hain.

```
@dataclass
class UserContext:
    uid: str
    is_pro_user: bool

    async def fetch_purchases() -> list[Purchase]:
        return ...

agent = Agent[UserContext](
    ...,
)
```

---

### Output types
By default, agents produce plain text (i.e. str) outputs. If you want the agent to produce a particular type of output, you can use the output_type parameter. A common choice is to use Pydantic objects, but we support any type that can be wrapped in a Pydantic TypeAdapter - dataclasses, lists, TypedDict, etc.

### Output Types (Output ki Iqsaam)
By default, agents plain text (yaani str) outputs dete hain. Agar aap chahte hain ke agent kisi khaas qisam ka output de, to aap output_type parameter ka istemal kar sakte hain. Aik aam intikhab Pydantic objects ka istemal karna hai, lekin hum har us type ko support karte hain jise Pydantic TypeAdapt
```
from pydantic import BaseModel
from agents import Agent


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

agent = Agent(
    name="Calendar extractor",
    instructions="Extract calendar events from text",
    output_type=CalendarEvent,
)
```

---
```
Note
When you pass an output_type, that tells the model to use structured outputs instead of regular plain text responses.

Note
Jab aap output_type pass karte hain, to yeh model ko batata hai ke woh regular plain text responses ke bajaye structured outputs ka istemal kare.

```

---

## Handoffs
Handoffs are sub-agents that the agent can delegate to. You provide a list of handoffs, and the agent can choose to delegate to them if relevant. This is a powerful pattern that allows orchestrating modular, specialized agents that excel at a single task. Read more in the handoffs documentation.

### Handoffs
Handoffs aise sub-agents hotay hain jin ko agent apna kaam delegate kar sakta hai. Aap handoffs ki aik list faraham karte hain, aur agent agar mauzoo samjhe to woh unhein delegate karne ka intikhab kar sakta hai. Yeh aik taqatwar pattern hai jo modular aur specialized agents ko regulate karne ki ijazat deta hai jo aik hi kaam mein maharat rakhtay hain. Mazeed tafseelat ke liye handoffs documentation mein parhen.

```
from agents import Agent

booking_agent = Agent(...)
refund_agent = Agent(...)

triage_agent = Agent(
    name="Triage agent",
    instructions=(
        "Help the user with their questions."
        "If they ask about booking, handoff to the booking agent."
        "If they ask about refunds, handoff to the refund agent."
    ),
    handoffs=[booking_agent, refund_agent],
)
```
---

### Dynamic instructions
In most cases, you can provide instructions when you create the agent. However, you can also provide dynamic instructions via a function. The function will receive the agent and context, and must return the prompt. Both regular and async functions are accepted.

### Dynamic Instructions
Zyadatar cases mein, aap agent banate waqt instructions faraham kar sakte hain. Lekin, aap aik function ke zariye dynamic instructions bhi de sakte hain. Yeh function agent aur context receive karega, aur prompt return karega. Dono tarah ke functions, regular aur async, qabool kiye jaate hain.


```
def dynamic_instructions(
    context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    return f"The user's name is {context.context.name}. Help them with their questions."


agent = Agent[UserContext](
    name="Triage agent",
    instructions=dynamic_instructions,
)
```
---

### Lifecycle events (hooks)
Sometimes, you want to observe the lifecycle of an agent. For example, you may want to log events, or pre-fetch data when certain events occur. You can hook into the agent lifecycle with the hooks property. Subclass the AgentHooks class, and override the methods you're interested in.

### Lifecycle Events (Hooks)
Kabhi kabhi, aap agent ke lifecycle ko observe karna chahte hain. Misaal ke taur par, aap events ko log karna chahte hain, ya khaas events hone par data ko pre-fetch karna chahte hain. Aap hooks property ke zariye agent ke lifecycle se jud sakte hain. Iske liye, AgentHooks class ko subclass karein, aur un methods ko override karein jin mein aap dilchaspi rakhte hain.

---

### Guardrails
Guardrails allow you to run checks/validations on user input, in parallel to the agent running. For example, you could screen the user's input for relevance. Read more in the guardrails documentation.

### Guardrails
Guardrails aap ko user input par checks/validations chalane ki ijazat dete hain, agent ke chalne ke mutawazi (in parallel). Misaal ke taur par, aap user ke input ko relevance (mutaliqa) ke liye screen kar sakte hain. Mazeed tafseelat ke liye guardrails documentation mein parhen.


---

### Cloning/copying agents
By using the clone() method on an agent, you can duplicate an Agent, and optionally change any properties you like.

### Cloning/Copying Agents (Agents ko Clone/Copy karna)
Aik agent par clone() method ka istemal karke, aap aik agent ko duplicate kar sakte hain, aur ikhtiyari (optionally) apni pasand ki koi bhi properties tabdeel kar sakte hain.


```
pirate_agent = Agent(
    name="Pirate",
    instructions="Write like a pirate",
    model="o3-mini",
)

robot_agent = pirate_agent.clone(
    name="Robot",
    instructions="Write like a robot",
)
```
---

### Forcing tool use
Supplying a list of tools doesn't always mean the LLM will use a tool. You can force tool use by setting ModelSettings.tool_choice. Valid values are:

auto, which allows the LLM to decide whether or not to use a tool.
required, which requires the LLM to use a tool (but it can intelligently decide which tool).
none, which requires the LLM to not use a tool.
Setting a specific string e.g. my_tool, which requires the LLM to use that specific tool.

### Forcing Tool Use (Tool ke Istemaal ko Lazmi banana)
Tools ki list faraham karne ka matlab hamesha yeh nahi hota ke LLM aik tool ka istemal karega. Aap ModelSettings.tool_choice set karke tool ke istemaal ko lazmi bana sakte hain. Jayaz qadrein (valid values) yeh hain:

auto, jo LLM ko yeh faisla karne ki ijazat deta hai ke tool istemal karna hai ya nahi.
required, jo LLM ko tool istemal karne ka taqaza karta hai (lekin yeh aqalmandi se faisla kar sakta hai ke kaun sa tool).
none, jo LLM ko tool istemal na karne ka taqaza karta hai.
Kisi khaas string ko set karna masalan my_tool, jo LLM ko us khaas tool ko istemal karne ka taqaza karta hai.

```
Note

To prevent infinite loops, the framework automatically resets tool_choice to "auto" after a tool call. This behavior is configurable via agent.reset_tool_choice. The infinite loop is because tool results are sent to the LLM, which then generates another tool call because of tool_choice, ad infinitum.
If you want the Agent to completely stop after a tool call (rather than continuing with auto mode), you can set [Agent.tool_use_behavior="stop_on_first_tool"] which will directly use the tool output as the final response without further LLM processing.

Note

Infinite loops se bachne ke liye, framework tool call ke baad tool_choice ko khud-ba-khud "auto" par reset kar deta hai. Yeh ravaiyya agent.reset_tool_choice ke zariye configure kiya ja sakta hai. Infinite loop is wajah se hota hai ke tool results LLM ko bheje jaate hain, jo phir tool_choice ki wajah se aik aur tool call generate karta hai, ad infinitum (hamesha ke liye).
Agar aap chahte hain ke agent tool call ke baad mukammal taur par ruk jaye (auto mode mein jari rakhne ke bajaye), to aap [Agent.tool_use_behavior="stop_on_first_tool"] set kar sakte hain jo tool output ko baghair mazeed LLM processing ke bara-e-rast final response ke taur par istemal karega.
```
