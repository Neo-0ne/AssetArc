Education Onboarding Bot
=========================
This bot takes in user goals (as plain text) and suggests which structuring bots would be most relevant.

POST endpoint:
    /educate

JSON Payload:
    {
        "goals": "I want offshore protection and tax savings"
    }

Returns:
    {
        "recommended_bots": ["IBC Bot", "Tax Optimization Bot"]
    }

Deploy in a Flask environment. Adjust and scale logic in app/main.py.
