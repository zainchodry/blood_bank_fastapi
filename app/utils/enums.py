from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    STAFF = "staff"
    DONOR = "donor"
    REQUESTER = "requester"


class RequestStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class DonationStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
