def add_custom_user(settings):
    settings['INSTALLED_APPS'] += ('custom_user', )
    settings['AUTH_USER_MODEL'] = 'accounts.TransportOperator'
    settings['AUTHENTICATION_BACKENDS'] = (
        'django.contrib.auth.backends.ModelBackend',
    )
