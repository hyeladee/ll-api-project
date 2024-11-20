from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call the default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    # Customize the response for Authentication-related errors.
    if isinstance(exc, (AuthenticationFailed, NotAuthenticated)) and response:
        response.data['detail'] = f"{response.data.get('detail', '')} Please log in."
        response.data['login_url'] = "http://localhost:8000/api/alt-login"  # Optional: Adding a separate field for the link
        response.status_code = status.HTTP_401_UNAUTHORIZED
    
    if response is None:
        response = Response(
            {"detail": "Not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    return response
