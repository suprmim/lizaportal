DEFAULT_DB_ALIAS = 'master'

SA_DATABASES = {
    'master': ['@DB_MASTER@', 'w',],
    'slave': ['@DB_SLAVE@', 'r',],
}

PROJECT_URL = "@HTTPD_HOST@"

EMAIL_SMTP_IDENT  = "@EMAIL_SMTP_IDENT@"
EMAIL_SMTP_SENDER = "@EMAIL_SMTP_SENDER@"
EMAIL_SMTP_LOGIN  = "@EMAIL_SMTP_LOGIN@"
EMAIL_SMTP_PASSWD = "@EMAIL_SMTP_PASSWD@"
EMAIL_SMTP_SERVER = "@EMAIL_SMTP_SERVER@"
EMAIL_SMTP_PORT   = @EMAIL_SMTP_PORT@
EMAIL_SMTP_TLS    = @EMAIL_SMTP_TLS@

