#!/usr/bin/env python
import os

from flask import Flask
from mbcom.implements import (
    ServiceConfiguration,
    ServiceSite,
)

os.environ.setdefault(
    'CONFIG_FILE', os.path.join('settings', 'configs.yml'))

service_site = ServiceSite()
service_config = ServiceConfiguration()
service_config.load_yaml(service_site, os.path.join(
    os.curdir, 'settings', 'components.yml'))

application = Flask(__name__)
application.config.from_mapping(SERVICE_SITE=service_site)