from pydantic import BaseModel

class MerchantCreate(BaseModel):
    name: str
    industry: str
    email: str


class MerchantResponse(MerchantCreate):
    id: int

    class Config:
        from_attributes = True