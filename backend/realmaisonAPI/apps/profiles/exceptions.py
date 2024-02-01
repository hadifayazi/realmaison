from rest_framework.exceptions import APIException


class ProfileNotFoundException(APIException):
    status_code = 404
    default_detail = "Profile not found"


class NotYourProfileException(APIException):
    status_code = 403
    default_detail = "You cannot edit profile that does not belong to you"
