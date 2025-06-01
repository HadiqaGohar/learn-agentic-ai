
# 🧠 Async vs Sync: What's the Difference?

This repository contains the blog post and example code that explains the difference between **Synchronous** and **Asynchronous** programming in a beginner-friendly way — using real-life analogies and Python code examples.

📖 **Read the Full Blog on Medium:**  
[Async vs Sync: What's the Difference?](https://medium.com/@hadiqagohar12/async-vs-sync-whats-the-difference-974a77cedf3e)

---

## 🧵 Overview

When we write programs, we deal with multiple tasks — some quick, others slow (like API calls or file I/O).  
How your program **waits or doesn't wait** for a task defines its execution style:

- ✅ **Synchronous (Sync):** Waits for one task to finish before starting another.
- ⚡ **Asynchronous (Async):** Starts a task and moves on to others without waiting.

---

## 🍕 Real-World Analogy

- **Sync:** A single chef waits until one pizza is baked before taking the next order.
- **Async:** A chef delegates pizza-making to an assistant and continues taking more orders.

---

## 🧪 Code Examples

### 🔹 Synchronous Code (Blocking)

```python
result = Runner.run_sync(agent, "What is the capital of Pakistan?", run_config=config)
print(f"Result: {result.final_output}")
````

👉 The program waits for the API call to complete before moving on.

---

### 🔹 Asynchronous Code (Non-Blocking)

```python
async def main():
    result = await Runner.run(agent, "What is the capital of Pakistan?", run_config=config)
    print(f"Result: {result.final_output}")

asyncio.run(main())
```

👉 The program **doesn't get stuck** waiting and can perform other tasks while awaiting the result.

---

## ✅ When to Use Async?

* For I/O-bound tasks like:

  * API calls
  * Database queries
  * File operations

---

## 📸 Infographic

![Async vs Sync Infographic](./A_flat-style_digital_illustration_infographic_comp.png)

---

## 🧑‍💻 Author

**Hadiqa Gohar**
[LinkedIn](https://www.linkedin.com/in/hadiqagohar/) | [Medium](https://medium.com/@hadiqagohar12) | [GitHub](https://github.com/hadiqagohar)

---

## 📌 License

This project is licensed under the MIT License.

```

---

Let me know if you’d like:
- Urdu-English hybrid version?
- React or JS version of this example?
- Blog badge or deployment info?

I’m here to help polish it more!
```
