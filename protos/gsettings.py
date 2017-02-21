DEFAULT_DB_ALIAS = 'master'

SA_DATABASES = {
    'master': ['@DB_MASTER@', 'w',],
    'slave': ['@DB_SLAVE@', 'r',],
}

