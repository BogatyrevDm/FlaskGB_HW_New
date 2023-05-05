from combojsonapi.permission import PermissionMixin, PermissionForGet, PermissionUser, PermissionForPatch
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from blog.models import User


class UserPermission(PermissionMixin):
    ALL_AVAILABLE_FIELD = (
        'id',
        'email',
        'first_name',
        'last_name',
    )

    PATCH_AVAILABLE_FIELD = (
        'first_name',
        'last_name',
    )

    def get(self, *args, many=True, user_permission: PermissionUser = None, **kwargs) -> PermissionForGet:
        if not current_user.is_authenticated:
            raise AccessDenied('No access')

        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELD, 10)
        return self.permission_for_get

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data=None, obj=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=User)
        return {
            k: v
            for k, v in data.items()
            if k in permission_for_patch.columns
        }
