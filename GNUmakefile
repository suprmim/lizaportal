include conf/local.mk

.DEFAULT_GOAL := help

WEB		?= ${ROOT}/web
APPS		?= ${WEB}/apps
PROTOS		?= ${ROOT}/protos
SCRIPTS		?= ${ROOT}/scripts
TESTS		?= ${ROOT}/tests
GLOBALS		?= ${ROOT}/globals
CONFIG		?= ${ROOT}/conf
LOGS		?= ${ROOT}/logs
TEMPLATES	?= ${WEB}/templates
ASSETS		?= ${WEB}/assets
STATIC		?= ${WEB}/static
MIGRATIONS	?= ${GLOBALS}/migrations
HTTPD_USER	?= ${OWNER}
HTTPD_GROUP	?= ${OWNER_GROUP}
MAKE		?= make




help:
	@echo '\
	Avalible targets:\
	*	init		- Build configs based on conf/local.mk;\
	*	configs		- Link configs to system directories;\
				  (FreeBSD by default)\
	*	configs-freebsd	- Link configs to FreeBSD system directories;\
	*	configs-linux	- Link configs to Linux system directories;\
		\
		\
	Targets marked by "*" need superuser privileges!\
	'

configs: configs-freebsd

configs-freebsd: build_protos
	@mkdir -p /usr/local/etc/supervisor
	@ln -s ${CONFIG}/supervisor.conf /usr/local/etc/supervisor/osteola-portal.conf
	@mkdir -p /usr/local/etc/nginx/sites-enabled
	@ln -s ${CONFIG}/nginx.conf /usr/local/etc/nginx/sites-enabled/osteola-portal.conf

configs-linux: build_protos
	@mkdir -p /etc/supervisor/conf.d
	@ln -s ${CONFIG}/supervisor.conf /etc/supervisor/conf.d/osteola-portal.conf
	@mkdir -p /etc/nginx/sites-enabled
	@ln -s ${CONFIG}/nginx.conf /etc/nginx/sites-enabled/osteola-portal.conf




init: build_protos
#	${call build_exec}

compat_links:
	rm -f ${STATIC} >/dev/null 2>&1; 
	ln -s ${ASSETS} ${STATIC} >/dev/null 2>&1; 

build_protos: make_dirs compat_links 
	${call build, ${PROTOS}/supervisor.conf, ${CONFIG}/supervisor.conf}
	${call build, ${PROTOS}/nginx.conf, ${CONFIG}/nginx.conf}
	${call build, ${PROTOS}/settings.py, ${WEB}/settings/local.py}
	${call build, ${PROTOS}/gsettings.py, ${GLOBALS}/gsettings/local.py}
	${call build, ${PROTOS}/start.py, ${APPS}/start.py}
	${call build, ${PROTOS}/alembic.ini, ${GLOBALS}/alembic.ini}
	${call build, ${PROTOS}/py_path.py, ${APPS}/py_path.py}
	${call build, ${PROTOS}/py_path.py, ${CONFIG}/py_path.py}
	${call build, ${PROTOS}/py_path.py, ${SCRIPTS}/py_path.py}
	${call build, ${PROTOS}/py_path.py, ${SCRIPTS}/cron/py_path.py}
	${call build, ${PROTOS}/py_path.py, ${TESTS}/py_path.py}
	${call build, ${PROTOS}/py_path.py, ${MIGRATIONS}/py_path.py}

make_dirs:
	@mkdir -p ${PROTOS} 2>/dev/null
	@mkdir -p ${CONFIG} 2>/dev/null
	@mkdir -p ${LOGS} 2>/dev/null
	@mkdir -p ${MIGRATIONS} 2>/dev/null
	@mkdir -p ${ASSETS} 2>/dev/null
	@mkdir -p ${SCRIPTS} 2>/dev/null
	@mkdir -p ${TESTS} 2>/dev/null
	@chown -R ${OWNER} ${ROOT}
	@chgrp -R ${HTTPD_GROUP} ${ASSETS} 
	@chown -R ${HTTPD_USER}:${HTTPD_GROUP} ${LOGS} 

define build_exec
	${call build, ${1}, ${2}} && chmod a+x ${2}
endef


define build
	@sed \
		-e 's%@ROOT@%${ROOT}%g' \
		-e 's%@WEB@%${WEB}%g' \
		-e 's%@APPS@%${APPS}%g' \
		-e 's%@CONFIG@%${CONFIG}%g' \
		-e 's%@PROTOS@%${PROTOS}%g' \
		-e 's%@GLOBALS@%${GLOBALS}%g' \
		-e 's%@LOGS@%${LOGS}%g' \
		-e 's%@TEMPLATES@%${TEMPLATES}%g' \
		-e 's%@ASSETS@%${ASSETS}%g' \
		-e 's%@STATIC@%${STATIC}%g' \
		-e 's%@ROOTCOOKIE@%${ROOTCOOKIE}%g' \
		-e 's%@AUTH_URL@%${AUTH_URL}%g' \
		-e 's%@MIGRATIONS@%${MIGRATIONS}%g' \
		-e 's%@HTTPD_USER@%${HTTPD_USER}%g' \
		-e 's%@HTTPD_HOST@%${HTTPD_HOST}%g' \
		-e 's%@WEBAPI_HOST@%${WEBAPI_HOST}%g' \
		-e 's%@WEBAPI_PORT@%${WEBAPI_PORT}%g' \
		-e 's%@DB_MASTER@%${DB_MASTER}%g' \
		-e 's%@DB_SLAVE@%${DB_SLAVE}%g' \
		-e 's%@EMAIL_SMTP_SENDER@%${EMAIL_SMTP_SENDER}%g' \
		-e 's%@EMAIL_SMTP_LOGIN@%${EMAIL_SMTP_LOGIN}%g' \
		-e 's%@EMAIL_SMTP_PASSWD@%${EMAIL_SMTP_PASSWD}%g' \
		-e 's%@EMAIL_SMTP_SERVER@%${EMAIL_SMTP_SERVER}%g' \
		-e 's%@EMAIL_SMTP_PORT@%${EMAIL_SMTP_PORT}%g' \
		-e 's%@EMAIL_SMTP_TLS@%${EMAIL_SMTP_TLS}%g' \
		-e 's%@TIMEDIFF_TZ@%${TIMEDIFF_TZ}%g' \
		-e 's%@OWNER@%${OWNER}%g' \
		-e 's%@MAKE@%${MAKE}%g' \
	< ${1} > ${2}
endef
