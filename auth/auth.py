from fastapi_users.authentication import CookieTransport

cookie_transport = CookieTransport(cookie_name="matcha", cookie_max_age=3600)
