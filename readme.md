# Altman Gate

On November 17, 2023, Sam Altman, co-founder of OpenAI, was removed as CEO and left the company's board. This decision came after a review by the board, which found Altman's lack of transparency impeded their oversight, leading to a loss of confidence in his leadership. But what happens next?

This is a project from the [MoaR LLM Hackathon @ AGI House](https://partiful.com/e/RRemJjBuI9ij8ws0BN7b), Nov 18 2023.

## Team

- Anya
- Kevin
- Tim
- Arsen

## Technology Stack

### Backend

- Python
- News data - we tried you.com (sponsor of hackathon) but decided to go with https://www.newscatcherapi.com/ instead - as they include summaries
- [bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) embeddings from [embaas.io](https://embaas.io/)
- [Clustering with usearch](https://github.com/unum-cloud/usearch/tree/main/python/usearch)

### Frontend

- Custom fork of image preview proxy from https://github.com/dhaiwat10/rlp-proxy
- Next.js
- Tailwind

## Vision

The vision of the project is to get the latest news about the matter and cluster it immediately. We didn't get to the fully continuous nature of it in the short time of the hackathon, but that will be the next step.
