# poc-clip-tokeniser

Proof-of-Concept code using CLIP tokeniser to encode/decode a prompt string, and visually show the token boundaries

This is essentially equivalent to what is being done on the CLIP part of: https://novelai.net/tokenizer

We're using the original CLIP library currently: https://github.com/openai/CLIP

Though it would likely be fairly easy to do similar with OpenCLIP: https://github.com/mlfoundations/open_clip

We could also likely do similar fairly easily with this JavaScript port of the tokeniser: https://github.com/josephrocca/clip-bpe-js

## Usage

```
pip install -r requirements.txt
```

```
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
