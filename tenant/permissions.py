def is_company_admin(user):
    return user.role == 'ADMIN'


def user_can_manage_company(user):
    return user.is_superuser or is_company_admin(user)
