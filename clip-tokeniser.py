#!/usr/bin/env/python3

# https://novelai.net/tokenizer

# https://github.com/openai/CLIP#usage
# https://github.com/mlfoundations/open_clip

# https://github.com/josephrocca/clip-bpe-js

# import torch
# import clip

from clip.simple_tokenizer import SimpleTokenizer as _Tokenizer

_tokenizer = _Tokenizer()

# clip_model_name = "ViT-B/32"
prompt_text = "This is an example prompt with 123 ways of demonstrating different clip token splits, blowup"

# device = "cuda" if torch.cuda.is_available() else "cpu"

# print(f"Loading CLIP model: {clip_model_name}")

# model, preprocess = clip.load(clip_model_name, device=device)

print(f"Tokenising prompt: {prompt_text}")

# tokenised_prompt_text = clip.tokenize(prompt_text).to(device)
tokenised_prompt_text2 = _tokenizer.encode(prompt_text)

# print(f"Tokenised prompt: {tokenised_prompt_text}")
print(f"Tokenised prompt2: {tokenised_prompt_text2}")

decoded_tokenised_prompt_text = _tokenizer.decode(tokenised_prompt_text2)

print(f"Decoded Tokenised prompt: {decoded_tokenised_prompt_text}")

wrapped_tokens = []
for idx, token in enumerate(tokenised_prompt_text2):
    decoded_token = _tokenizer.decode([token])
    print(f"Token {idx}: {decoded_token}\t(ID: {token})")
    wrapped_tokens.append(f"«{decoded_token}»")

wrapped_prompt_tokens = ''.join(wrapped_tokens)

print(f"Wrapped Decoded Tokenised Prompt: {wrapped_prompt_tokens}")
