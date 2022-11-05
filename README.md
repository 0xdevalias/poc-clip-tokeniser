# poc-clip-tokeniser

Proof-of-Concept code using CLIP tokeniser to encode/decode a prompt string, and visually show the token boundaries

This is essentially equivalent to what is being done on the CLIP part of: https://novelai.net/tokenizer

We're using the original CLIP library currently: https://github.com/openai/CLIP

Though it would likely be fairly easy to do similar with OpenCLIP: https://github.com/mlfoundations/open_clip

We could also likely do similar fairly easily with this JavaScript port of the tokeniser: https://github.com/josephrocca/clip-bpe-js

## Usage

```bash
pip install -r requirements.txt
```

```bash
⇒  python3 clip-tokeniser.py

Tokenising prompt: This is an example prompt with 123 ways of demonstrating different clip token splits, blowup

Tokenised prompt2: [589, 533, 550, 6228, 20198, 593, 272, 273, 274, 1248, 539, 22107, 2731, 9289, 17134, 34897, 267, 15230, 705]

Decoded Tokenised prompt: this is an example prompt with 1 2 3 ways of demonstrating different clip token splits , blowup

Token 0: this 	(ID: 589)
Token 1: is 	(ID: 533)
Token 2: an 	(ID: 550)
Token 3: example 	(ID: 6228)
Token 4: prompt 	(ID: 20198)
Token 5: with 	(ID: 593)
Token 6: 1 	(ID: 272)
Token 7: 2 	(ID: 273)
Token 8: 3 	(ID: 274)
Token 9: ways 	(ID: 1248)
Token 10: of 	(ID: 539)
Token 11: demonstrating 	(ID: 22107)
Token 12: different 	(ID: 2731)
Token 13: clip 	(ID: 9289)
Token 14: token 	(ID: 17134)
Token 15: splits 	(ID: 34897)
Token 16: , 	(ID: 267)
Token 17: blow	(ID: 15230)
Token 18: up 	(ID: 705)

Wrapped Decoded Tokenised Prompt: «this »«is »«an »«example »«prompt »«with »«1 »«2 »«3 »«ways »«of »«demonstrating »«different »«clip »«token »«splits »«, »«blow»«up »
```

## Further Reading

Stable Diffusion

- https://github.com/CompVis/stable-diffusion/blob/main/configs/stable-diffusion/v1-inference.yaml#L46-L70
  - `cond_stage_config`: `ldm.modules.encoders.modules.FrozenCLIPEmbedder`
- https://github.com/CompVis/stable-diffusion/blob/main/ldm/modules/encoders/modules.py#L137-L162
  - `FrozenCLIPEmbedder`
  - > Uses the CLIP transformer encoder for text (from Hugging Face)
  - `version="openai/clip-vit-large-patch14"`
  - `self.tokenizer = CLIPTokenizer.from_pretrained(version)`
  - `self.transformer = CLIPTextModel.from_pretrained(version)`
- https://huggingface.co/docs/transformers/model_doc/clip
  - https://huggingface.co/docs/transformers/model_doc/clip#transformers.CLIPTokenizer
- https://huggingface.co/openai/clip-vit-large-patch14
  - https://huggingface.co/openai/clip-vit-large-patch14/blob/main/vocab.json
    - This seems to be all of the possible tokens, and their corresponding IDs(?)
  - https://huggingface.co/openai/clip-vit-large-patch14/blob/main/tokenizer_config.json
  - https://huggingface.co/openai/clip-vit-large-patch14/blob/main/tokenizer.json
    - This also seems to contain a whole pile of tokens and their corresponding IDs, the merges, as well as some other config things.. might be a combination of a bunch of these other files?
  - https://huggingface.co/openai/clip-vit-large-patch14/blob/main/special_tokens_map.json
  - https://huggingface.co/openai/clip-vit-large-patch14/blob/main/merges.txt
