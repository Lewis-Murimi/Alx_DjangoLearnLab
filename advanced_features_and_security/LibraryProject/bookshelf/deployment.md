# HTTPS and Security Configuration

## Django settings
- `SECURE_SSL_REDIRECT = True`: Forces all HTTP to HTTPS redirects.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS-only access for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows browser preload of HSTS.
- `SESSION_COOKIE_SECURE = True`: Ensures session cookies are only sent over HTTPS.
- `CSRF_COOKIE_SECURE = True`: Ensures CSRF protection cookies are secure.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS protection.

## Nginx/Apache Configuration
- Set up SSL certificates using Let’s Encrypt or similar.
- Redirect HTTP (port 80) to HTTPS (port 443).
- Forward requests to Django backend using gunicorn/uwsgi.

## Notes
- DEBUG must be set to `False` for these settings to be effective.
- Test HTTPS access using your browser or `curl -I https://yourdomain.com`.
