# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

PLUGINS = [
    "adestis_netbox_domain_management",
    "netbox_certificate_management",
    "adestis_netbox_applications",
]

PLUGINS_CONFIG = {
  'netbox_certificate': {},
  "netbox_certificate_management": {
        'top_level_menu': True,
        },
  "adestis_netbox_applications":{},
}

