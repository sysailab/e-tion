from fastapi import Header, HTTPException

async def get_token_header(x_token: str = Header(...)):
	if x_token != "secret_token":
		raise HTTPException(status_code=400, detail="X-Token Header Invaild")


async def get_query_token(token: str):#
	if token != "xxx":
		raise HTTPException(status_code=400, detail="No Barney token provided")