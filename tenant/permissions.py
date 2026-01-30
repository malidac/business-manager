def is_company_admin(user):
    return user.is_authenticated and user.role == 'ADMIN'


def is_staff_user(user):
    return user.is_authenticated and user.role == 'STAFF'


def can_manage_expenses(user):
    """
    ADMIN može sve
    STAFF samo view (ili kasnije svoje)
    """
    if user.is_superuser:
        return True

    if is_company_admin(user):
        return True

    return False


def can_view_expenses(user):
    return user.is_authenticated
