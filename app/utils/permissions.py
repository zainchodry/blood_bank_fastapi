def is_admin(user):
    return user.role == "admin"


def can_manage_requests(user):
    return user.role in ["admin", "doctor", "staff"]


def can_donate(user):
    return user.role == "donor"


def can_request_blood(user):
    return user.role == "requester"
