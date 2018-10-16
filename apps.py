from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import datetime, syslog, os, sys, random, string

class Translate(object):
    class vn(object):
        date_create     = _('Creation date')
        date_update     = _('Last modification date')
        update_by       = _('Update by')
        error           = _('Error encountered')
        info            = _('Additional information')
        method          = _('Method')
        name_method     = _('Name')
        enable          = _('Enable')
        port            = _('Port')
        tls             = _('Enable TLS')
        is_active       = _('Will be active')
        is_staff        = _('Will be staff')
        superuser       = _('Will be superuser')
        groups          = _('Groups associated')
        permissions     = _('Permissions associated')
        certificate     = _('TLS Certificate')
        check           = _('Check')
        self_signed     = _('Self-signed')
        field_firstname = _('Firstname correspondence')
        field_lastname  = _('Lastname correspondence')
        field_email     = _('Email correspondence')
        heck            = _('Check')
        user            = _('User')
        username        = _('Username')
        email           = _('Email address')
        is_active       = _('Active')
        is_staff        = _('Staff')
        is_robot        = _('Robot')
        firstname       = _('Firstname')
        lastname        = _('Lastname')
        date_joined     = _('Date joined')
        method          = _('Create method')
        key             = _('Authentication key')

    class ht(object):
        update_by            = _('Last user who modified.')
        error                = _('Detail about the error.')
        message              = _('add additional information')
        port                 = _('Change the port used by the method')
        tls                  = _('Enable or disable TLS')
        certificate          = _('Uploaded here the certificate to check')
        method               = _('Method type')
        name_method          = _('Method name')
        enable               = _('Enable or disable the method')
        certificate_content  = _('Certificate content')
        certificate_path     = _('Certificate path')
        self_signed          = _('Is the certificate self-signed?')
        field                = _('Automatically filled field with key map (Keep null if not used)')
        can_update_method    = _('Can update task')
        can_read_method      = _('Can detail and list method')
        can_writecert_method = _('Can write certificate method')
        can_check_method     = _('Can check method')
        can_use_api          = _('Can use API')
        can_csrf_exempt      = _('Can csrf exempt')
        can_read_user        = _('Can detail and list user')
        can_see_email        = _('Can see email')
        can_see_firstname    = _('Can see firstname')
        can_see_lastname     = _('Can see lastname')
        can_see_method       = _('Can see method')
        can_see_groups       = _('Can see groups')
        can_see_permissions  = _('Can see permissions')
        can_see_additional   = _('Can see additional')
        can_see_key          = _('Can see key')

    class error(object):
        is_superuser    = _('Superuser must have is_superuser=True.')
        required_fields = _('The given field must be set: %s')
        method_check    = _('The method does not works')
        invalid_login   = _('Please enter a correct LDAP login and password. Note that both '
                            'fields may be case-sensitive.')
        inactive        = _('This account is inactive.')
        user_notfound   = _('User Not Found')
        credentials     = _('Invalid credentials')
        not_order       = _('Not ordered, check status')
        not_ready       = _('Not ready, check status')
        tls_disable     = _('TLS is disable on this method')
        no_certificate  = _('This method does not use a certificate')
        maintain        = _('This default script not exist')
        no_ldapcache    = _('No cached LDAP method')

    class vbn(object):
        group  = _('Group')
        method = _('Method')
        user   = _('User')

    class vpn(object):
        group  = _('Groups')
        method = _('Methods')
        user   = _('Users')

    class admin(object):
        site_header              = _('Django administration')
        index_title              = _('Site administration (assisted by Simplify)')
        verbose_name             = _('Authentication and Authorization')
        login                    = _('Log in')

    class ldap(object):
        ldap   = _('LDAP')
        login  = _('LDAP Login')

class Config(object):
    namespace = 'elementary'
    override  = 'ELEMENTARY'

    class choices(object):
        method_method = ()
        user_createsuperuser = 'CREATESUPERUSER'
        user_backend         = 'BACKEND'
        user_frontend        = 'FRONTEND'
        user_additional      = 'ADDITIONAL'
        user_method = (
            (user_createsuperuser, _('Create Super User')),
            (user_backend,         _('Back-end')),
            (user_frontend,        _('Front-end')),
            (user_additional,      _('Additional method')),
        )

    class user(object):
        login_method    = 'login_method'
        username_field  = 'username'
        required_fields = []
        unique_username = True
        unique_email    = False
        null_username   = False
        null_email      = True
        null_firstname  = True
        null_lastname   = True
        is_active       = False
        is_staff        = False
        is_robot        = False
        key_min_length  = 10
        key_max_length  = 32
        normalize       = 'NFKC'
        api_backend     = 'user.simplify.api'
        robot_backend   = 'user.simplify.robot'
        anonymous       = 'user.anonymous'

    class admin(object):
        log_fieldsets            = (_('Log informations'), {'fields': ('update_by', 'date_create', 'date_update', 'error', 'message')})
        method_fieldsets         = (((None, { 'fields': ('method', 'name', 'port', 'enable',), })),
                                   ((_('TLS configuration'), { 'classes': ('wide',), 'fields': ('tls', 'certificate', 'self_signed', 'certificate_path', 'certificate_content')})),
                                   ((_('Correspondence'), { 'classes': ('collapse',), 'fields': ('field_firstname', 'field_lastname', 'field_email')})),
                                   (_('Groups and permissions'), { 'classes': ('collapse',), 'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'permissions', )}))
        method_filter_horizontal = ('groups', 'permissions')
        method_list_display      = ('name', 'method', 'enable', 'is_active', 'is_staff', 'is_superuser', 'status', 'admin_button_check', 'admin_download_certificate')
        method_readonly_fields   = ('update_by', 'date_create', 'date_update', 'error', 'certificate_path', 'certificate_content')
        method_list_filter       = ('method', 'enable',)
        method_search_fields     = ('name',)
        ldap_fieldsets           = (_('LDAP method'), 
                                   {'classes': ('collapse',),
                                   'fields': ('ldap_host', 'ldap_define', 'ldap_uri', 'ldap_scope', 'ldap_version', 'ldap_bind', 'ldap_password', 'ldap_user', 'ldap_search')})
        user_add_fieldsets       = None
        user_fieldsets           = (((None, {'fields': ('username', 'password')})),
                                   ((_('Personal info'), {'fields': ('email', 'first_name', 'last_name')})),
                                   (_('Authentication method'), {'fields': ('method', 'additional')}),
                                   (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_robot', 'groups', 'user_permissions')}),
                                   (_('API'), {'fields': ('key', )}),
                                   (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                                   (_('Log informations'), {'fields': ('date_update', 'update_by')}))
        user_filter_horizontal   = ('groups', 'user_permissions', 'additional')
        user_list_display        = (None,)
        user_readonly_fields     = ('date_joined', 'date_update', 'update_by')
        user_list_filter         = ('method', 'is_active', 'is_staff', 'is_superuser', 'is_robot')

    class ldap(object):
        enable = False
        option = 'LDAP'
        fields_check = ['ldap_host', 'ldap_define', 'ldap_scope', 'ldap_version', 'ldap_bind', 'ldap_password', 'ldap_user', 'ldap_search', 'ldap_tls_cacertfile']

if hasattr(settings, Config.override):
    for config,configs in getattr(settings, Config.override).items():
        if hasattr(Config, config):
            for key,value in configs.items():
                if hasattr(getattr(Config, config), key):
                    setattr(getattr(Config, config), key, value)

if Config.ldap.enable: Config.choices.method_method += ((Config.ldap.option, Config.ldap.name),)

class ElementaryConfig(AppConfig, Config):
    name = 'elementary'

    def key():
        return ''.join(random.choice('-._~+'+string.hexdigits) for x in range(ElementaryConfig.user.key_max_length))

