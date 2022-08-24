from django.core.exceptions import PermissionDenied # Importamos la excepcion de permisos



    #     return super().dispatch(request, *args, **kwargs)

class SuperUsuarioMixin():
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        elif not request.user.es_administrador and not request.user.is_superuser:
            raise PermissionDenied
        return super(SuperUsuarioMixin, self).dispatch(request, *args, **kwargs)








#profe
'''
class SuperUsuarioMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.es_administrador:
            raise PermissionDenied
        return super(SuperUsuarioMixin, self).dispatch(request, *args, **kwargs)

def superuser_required():
    def permission_required(f):
        def check(request, *arg, **kwargs):
            if not request.user.is_superuser:
                raise PermissionDenied
            return f(request, *arg, **kwargs)
    return permission_required
'''     
