# SignalPost

## Problem

Railway engineers need to find rules from large railway manuals while working near railway tracks. Slow internet makes it difficult to open large PDF files. SignalPost helps them find the right information quickly. It gives short answers with references to the railway manuals.

## Who it is for

Railway Signal and Telecom engineers who need to check maintenance rules while working in the field with slow internet.

## Signature feature

Trackside Mode gives a short, three-line answer with the manual reference and is designed to work with slow internet.

## Hardest problem (my interview story)

The main challenge is finding the correct information from large railway manuals and giving the right answer quickly. The app must use very little internet data and show the correct manual reference.

## Dataset

| Source | Link | Documents | Pages | Licence / terms |
|---|---|---|---|---|
| RDSO | https://rdso.indianrailways.gov.in/ | Railway technical documents | To be counted | Check usage rules |
| Indian Railway Signal Engineering Manual | Official link to be added | Signal manual | To be counted | Check usage rules |

Target: Collect at least 1,200 pages of railway documents.

## 10 real questions

See [docs/QUESTIONS.md](docs/QUESTIONS.md).

## Run it

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements-dev.txt

copy .env.example .env

uvicorn app.main:app --reload
```

Check whether the app is running:

```bash
curl http://localhost:8000/health
```

## Live link

To be added in Week 2.
