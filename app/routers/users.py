from fastapi import APIRouter

router = APIRouter()

@router.get("/users", tags=["users"])
async def read_users():
	return [{"username":"Ted"}, {"username":"Robin"}]

@router.get("/users/me", tags=["users"])
async def read_users_me():
	return {"username":"fakeuser"}