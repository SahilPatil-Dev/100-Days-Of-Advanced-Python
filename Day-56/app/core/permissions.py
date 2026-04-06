from fastapi import Depends, HTTPException
from app.core.auth import get_current_user


def require_role(required_role: str):

    def role_checker(current_user = Depends(get_current_user)):

        if current_user.role != required_role:
            raise HTTPException(
                status_code=403,
                detail="Insufficient permissions"
            )

        return current_user

    return role_checker