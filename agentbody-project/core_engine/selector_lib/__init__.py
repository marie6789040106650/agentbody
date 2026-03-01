"""
Selector Library - Common website selectors
"""

SELECTORS = {
    "github": {
        "login": {
            "username": "#login_field",
            "password": "#password",
            "submit": "[type='submit']",
        }
    },
    "vercel": {
        "login": {
            "email": "input[type='email']",
            "github": "[aria-label*='GitHub'], [data-testid*='github']",
        }
    },
    "google": {
        "login": {
            "email": "input[type='email']",
            "password": "input[type='password']",
        }
    },
    "generic": {
        "button_primary": "button[type='submit']",
        "input_text": "input[type='text'], input[type='email']",
        "input_password": "input[type='password']",
    }
}

def get_selector(site: str, element: str) -> str:
    if site in SELECTORS and element in SELECTORS[site]:
        return SELECTORS[site][element]
    return None

def get_site_selectors(site: str) -> dict:
    return SELECTORS.get(site, {})
