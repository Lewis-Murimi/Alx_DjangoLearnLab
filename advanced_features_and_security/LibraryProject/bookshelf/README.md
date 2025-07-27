"""
Permission Setup:
- Permissions defined: can_view, can_create, can_edit, can_delete
- Groups:
    - Viewers: can_view
    - Editors: can_create, can_edit
    - Admins: all permissions
- Use Django Admin or run `python manage.py setup_groups` to configure groups.
"""

## Security Measures Implemented

- CSRF protection via Django's built-in CSRF middleware and template tokens.
- SQL Injection mitigation by using Django ORM and forms.
- XSS mitigation through secure settings and Content Security Policy headers.
- Cookies secured with CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE.
