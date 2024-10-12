## Prompt Engineering Guide
1. https://www.promptingguide.ai/

</br>

## Cloudflare
1. https://developers.cloudflare.com/workers-ai/guides/prompting/
2. Scoped Prompts
    1. system: System messages define the AI’s personality. You can use them to set rules and how you expect the AI to behave.
    2. user: User messages are where you actually query the AI by providing a question or a conversation.
    3. assistant: Assistant messages hint to the AI about the desired output format. Not all models support this role.
    4. EXAMPLE:
        ```py
        {
            messages: [
                { role: "system", content: "you are a professional computer science assistant" },
                { role: "user", content: "what is WASM?" },
                { role: "assistant", content: "WASM (WebAssembly) is a binary instruction format that is designed to be a platform-agnostic" },
                { role: "user", content: "does Python compile to WASM?" },
                { role: "assistant", content: "No, Python does not directly compile to WebAssembly" },
                { role: "user", content: "what about Rust?" },
            ],
        }
        ```
3. Unscoped Prompts
    1. You can send a single question to the model without providing any context. 
    2. Cloudflare recommend using unscoped prompts for inference with LoRA.

</br>

## Meta Llama
1. https://www.llama.com/docs/how-to-guides/prompting/


