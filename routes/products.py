from fastapi import APIRouter
from datetime import datetime
from database import products_collection
from models.product import ProductCreateRequest

router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("")
async def get_products():
    products = []
    cursor = products_collection.find({})

    async for document in cursor:
        document["id"] = str(document["_id"])
        del document["_id"]
        products.append(document)

    return {
        "success": True,
        "data": products
    }


@router.post("", status_code=201)
async def add_product(product: ProductCreateRequest):
    if not product.name or product.price <= 0:
        return {
            "success": False,
            "message": "Invalid product data"
        }

    new_product = {
        "name": product.name,
        "price": product.price,
        "created_at": datetime.utcnow()
    }

    try:
        await products_collection.insert_one(new_product)
        return {
            "success": True,
            "message": "Product added successfully"
        }
    except Exception:
        return {
            "success": False,
            "message": "Database insertion failure"
        }
