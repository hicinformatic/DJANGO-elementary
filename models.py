from django.db import models
from django.contrib.auth.models import (AbstractUser, Group, Permission)
from django.core.validators import (MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator)

from .apps import (Translate as T, ElementaryConfig as conf)
from .manager import UserManager

#██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
#██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
#██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
#██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
#╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
# ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
class Update(models.Model):
    date_create = models.DateTimeField(T.vn.date_create, auto_now_add=True, editable=False)
    date_update = models.DateTimeField(T.vn.date_update, auto_now=True, editable=False)
    update_by   = models.CharField(T.vn.update_by, blank=True, editable=False, help_text=T.ht.update_by, max_length=254, null=True)
    error       = models.TextField(T.vn.error, blank=True, help_text=T.ht.error, null=True)
    info        = models.TextField(T.vn.info, blank=True, help_text=T.ht.message, null=True)

    class Meta:
        abstract = True

    def status(self):
        return True if self.error is None else False
    status.boolean = True

# ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ 
#██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗
#██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝
#██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ 
#╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     
# ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  
class Group(Group, Update):
    class Meta:
        verbose_name        = T.vbn.group
        verbose_name_plural = T.vpn.group

#███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗ 
#████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗
#██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║
#██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║
#██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝
#╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
class Method(Update):
    method          = models.CharField(T.vn.method, choices=conf.choices.method_method, help_text=T.ht.method, max_length=4)
    name            = models.CharField(T.vn.name_method, help_text=T.ht.name_method, max_length=254)
    enable          = models.BooleanField(T.vn.enable, default=True, help_text=T.ht.enable)
    port            = models.PositiveIntegerField(T.vn.port, blank=True, default=0, help_text=T.ht.port, null=True, validators=[MinValueValidator(0), MaxValueValidator(65535)])
    tls             = models.BooleanField(T.vn.tls, default=False, help_text=T.ht.tls)
    certificate     = models.TextField(T.vn.certificate, blank=True, help_text=T.ht.certificate, null=True)
    self_signed     = models.BooleanField(T.vn.self_signed, default=False, help_text=T.ht.self_signed)
    is_active       = models.BooleanField(T.vn.is_active, default=True)
    is_staff        = models.BooleanField(T.vn.is_staff, default=False)
    is_superuser    = models.BooleanField(T.vn.superuser, default=False)
    groups          = models.ManyToManyField(Group, verbose_name=T.vn.groups, blank=True)
    permissions     = models.ManyToManyField(Permission, verbose_name=T.vn.permissions, blank=True)
    field_firstname = models.CharField(T.vn.field_firstname, blank=True, help_text=T.ht.field, max_length=254, null=True)
    field_lastname  = models.CharField(T.vn.field_lastname, blank=True, help_text=T.ht.field, max_length=254, null=True)
    field_email     = models.CharField(T.vn.field_email, blank=True, help_text=T.ht.field, max_length=254, null=True)

    if conf.ldap.enable:
        ldap_host       = models.CharField(T.vn.ldap_host, blank=True, default='localhost', help_text=T.ht.ldap_host, max_length=254, null=True)
        ldap_define     = models.CharField(T.vn.ldap_define, blank=True, help_text=T.ht.ldap_define, max_length=254, null=True)
        ldap_uri        = models.CharField(T.vn.ldap_uri, choices=conf.choices.ldap_uri, default=conf.choices.ldap_uri_ldap, help_text=T.ht.ldap_uri, max_length=8)
        ldap_scope      = models.CharField(T.vn.ldap_scope, choices=conf.choices.ldap_scope, default=conf.choices.ldap_scope_base, help_text=ht.ldap_scope, max_length=14)
        ldap_version    = models.CharField(T.vn.ldap_version, choices=conf.choices.ldap_version, default=conf.choices.ldap_version3, help_text=T.ht.ldap_version, max_length=8)
        ldap_bind       = models.CharField(T.vn.ldap_bind, blank=True, help_text=T.ht.ldap_bind, max_length=254, null=True)
        ldap_password   = models.CharField(T.vn.ldap_password, blank=True, help_text=T.ht.ldap_password, max_length=254, null=True)
        ldap_user       = models.TextField(T.vn.ldap_user, blank=True, help_text=T.ht.ldap_user, null=True)
        ldap_search     = models.TextField(T.vn.ldap_search, help_text=T.ht.ldap_search, blank=True, null=True)
        ldap_tls_cacert = models.BooleanField(T.vn.ldap_tls_cacert, default=False, help_text=T.ht.ldap_tls_cacert)

    class Meta:
        verbose_name        = T.vbn.method
        verbose_name_plural = T.vpn.method
        permissions         = (
            ('can_read_method',   T.ht.can_read_method),
            ('can_check_method',  T.ht.can_check_method),
            ('can_writecert_method',  T.ht.can_writecert_method))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('%s:method-detail' % conf.namespace, kwargs={ 'pk': self.id, 'extension': '.html' })

    def save(self, *args, **kwargs):
        super(Method, self).save(*args, **kwargs)
        self.certificate_content()

    def certificate_path(self):
        return None if self.certificate in [None, ''] else '{}/{}_{}.crt'.format(conf.directory.certificates, self.name, self.method)
    certificate_path.short_description = T.ht.certificate_path

    def certificate_content(self):
        if self.certificate not in [None, '']:
            certificate = self.certificate_path()
            if not os.path.isfile(certificate):
                self.certificate_write(certificate)
            else:
                timestamp_file = os.path.getctime(certificate)
                timestamp_date_update = int(time.mktime(self.date_update.timetuple()))
                if timestamp_file < timestamp_date_update:
                    self.certificate_write(certificate)
            return self.certificate
        return None
    certificate_content.short_description = T.ht.certificate_content

    def certificate_write(self, certificate):
        with open(certificate, 'w') as cert_file:
            cert_file.write(self.certificate)
        cert_file.closed

    def admin_button_check(self):
        url = reverse('admin:admin-method-check',  args=[self.id])
        return format_html('<a class="button" href="{url}">{vn}</a>'.format(url=url, vn=T.vn.check))
    admin_button_check.short_description = T.vn.check

    def admin_download_certificate(self):
        if self.certificate not in ['', None]:
            url = reverse('simplify:method-get-certificate',  args=[self.id])
            return format_html('<a class="button" href="{url}">{vn}</a>'.format(url=url, vn=T.vn.certificate))
        return None
    admin_download_certificate.short_description = T.vn.certificate

    def get_method(self):
        return getattr(getattr(methods, 'method_%s' % self.method.lower()), 'method_%s' % self.method.lower())(self)

#██╗   ██╗███████╗███████╗██████╗ 
#██║   ██║██╔════╝██╔════╝██╔══██╗
#██║   ██║███████╗█████╗  ██████╔╝
#██║   ██║╚════██║██╔══╝  ██╔══██╗
#╚██████╔╝███████║███████╗██║  ██║
# ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
class User(AbstractUser):
    username    = models.CharField(T.vn.username, blank=conf.user.null_username, max_length=254, null=conf.user.null_username, unique=conf.user.unique_username, validators=[AbstractUser.username_validator],)
    email       = models.EmailField(T.vn.email, blank=conf.user.null_email, null=conf.user.null_email, unique=conf.user.unique_email)
    is_active   = models.BooleanField(T.vn.is_active, default=conf.user.is_active)
    is_staff    = models.BooleanField(T.vn.is_staff, default=conf.user.is_staff)
    is_robot    = models.BooleanField(T.vn.is_robot, default=conf.user.is_robot)
    first_name  = models.CharField(T.vn.firstname, blank=conf.user.null_firstname, max_length=30, null=conf.user.null_firstname)
    last_name   = models.CharField(T.vn.lastname, blank=conf.user.null_lastname, max_length=30, null=conf.user.null_lastname)
    date_joined = models.DateTimeField(T.vn.date_joined, auto_now_add=True, editable=False)
    date_update = models.DateTimeField(T.vn.date_update, auto_now=True, editable=False)
    update_by   = models.CharField(T.vn.update_by, editable=False, max_length=254)
    method      = models.CharField(T.vn.method, choices=conf.choices.user_method, default=conf.choices.user_backend, max_length=15)
    additional  = models.ManyToManyField(Method, blank=True)
    key         = models.CharField(T.vn.key, default=conf.key, max_length=32, unique=True, validators=[MaxLengthValidator(conf.user.key_max_length), MinLengthValidator(conf.user.key_min_length),])

    objects = UserManager()
    USERNAME_FIELD = conf.user.username_field
    REQUIRED_FIELDS = conf.user.required_fields

    class Meta:
        verbose_name        = T.vbn.user
        verbose_name_plural = T.vpn.user
        ordering            = [conf.user.username_field]
        permissions         = (
            ('can_use_api', T.ht.can_use_api),
            ('can_csrf_exempt', T.ht.can_csrf_exempt),
            ('can_read_user', T.ht.can_read_user),
            ('can_see_email', T.ht.can_see_email),
            ('can_see_firstname', T.ht.can_see_firstname),
            ('can_see_lastname', T.ht.can_see_lastname),
            ('can_see_method', T.ht.can_see_method),
            ('can_see_groups', T.ht.can_see_groups),
            ('can_see_permissions', T.ht.can_see_permissions),
            ('can_see_additional', T.ht.can_see_additional),
            ('can_see_key', T.ht.can_see_key),
        )

    def clean(self):
        super(AbstractUser, self).clean()
        if 'username' in self.REQUIRED_FIELDS or self.username is not None:
            self.username = unicodedata.normalize(conf.user.normalize, self.username) 
        self.email = self.__class__.objects.normalize_email(self.email)