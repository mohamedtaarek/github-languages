from githubLanguages.env import credentials

DATABASES = {
    "default": {
        "ENGINE": credentials.get("DB_ENGINE"),
        "NAME": credentials.get("POSTGRES_DB", ""),
        "USER": credentials.get("POSTGRES_USER", ""),
        "HOST": credentials.get("POSTGRES_HOST", ""),
        "PASSWORD": credentials.get("POSTGRES_PASSWORD", ""),
        "PORT": credentials.get("POSTGRES_PORT", ""),
    }
}
