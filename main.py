from fastapi import  FastAPI, Path, Query
from typing import Optional 
from pydantic import BaseModel, Field, model_validator


app = FastAPI(
    title="Shopping List API",
    description="API for managing a **shopping list**.",
    version="1.0"
)

class ShoppingItem(BaseModel):
  """Representation of a shopping item"""
  name: str
  quantity: int = Field(..., ge=1, description="Quantity of the item. Must be greater than or equal to 1.")
  price: float = Field(..., ge=0, description="Quantity of the item. Must be greater than or equal to 0.")

class UpdateShoppingItem(BaseModel):
  """Representation of an update request for a shopping item"""
  name: Optional[str] = None
  quantity: Optional[int] = None
  price: Optional[float] = None

shopping_list = [
    ShoppingItem(name="apple", quantity=5, price=1.0),
    ShoppingItem(name="banana", quantity=10, price=0.5),
    ShoppingItem(name="orange", quantity=3, price=2.0)
]

@app.post("/add-item/", summary="Add a new item to the shopping list", response_description="Confirmation message")
def add_item(item: ShoppingItem):
  """
  Example:
  - Request Body:
      {
          "name": "apple",
          "quantity": 5,
          "price": 1.0
      }
  - Response: {"message": "Item added successfully"}
  """

  shopping_list.append(item)
  return {"message": "Item added successfully"}

@app.get("/view-list/", summary="View the entire shopping list", response_model=list[ShoppingItem], response_description="List of shopping items")
def view_list():
    """
    Example:
    - Request: GET /view-list/
    - Response: [{"name": "apple", "quantity": 5, "price": 1.0}, ...]
    """

    if len(shopping_list) == 0:
        return {"Error": "List is empty"}
    return shopping_list

@app.get("/view-list/{item_id}", summary="View a specific item by ID", response_model=ShoppingItem, response_description="Shopping item details")
def view_item(item_id: int = Path(description = "The ID of the item you want to view", ge = 0)):
    """
    Example:
    - Request: GET /view-list/0
    - Response: {"name": "apple", "quantity": 5, "price": 1.0}
    """

    if item_id < 0 or item_id >= len(shopping_list):
      return {"Error": "Item not found"}
    return shopping_list[item_id]

@app.get("/get-by-name", summary="Get items by name", response_model=list[ShoppingItem], response_description="List of shopping items matching the given name") #"/get-by-name?name=pizza"#
def get_item_by_name(name: Optional[str] = Query(None, description="Name of the item to search")):
  """
  Example:
  - Request: GET /get-by-name?name=apple
  - Response: [{"name": "apple", "quantity": 5, "price": 1.0}]
  """

  if name == None:
     return shopping_list

  found_items = []
  for item in shopping_list:
      if item.name == name:
          found_items.append(item)

  if found_items:
      return found_items
  else:
      return {"Data": "Not found"}


@app.put("/update-item/{item_id}", summary="Update an existing item by ID", response_model=ShoppingItem, response_description="Updated shopping item details")
def update_item(item: UpdateShoppingItem, item_id: int = Path(description = "The ID of the item you want to update", ge = 0) ):
  """
  Example:
  - Request: PUT /update-item/0
    Request Body:
      - { "name": "apple", "quantity": 10, "price": 2.0 }
      - { quantity":20 }  
      
  - Response: 
    - {"name": "apple", "quantity": 10, "price": 2.0}
    - {"name": "apple", "quantity": 20, "price": 1.0}
  """

  if item_id < 0 or item_id >= len(shopping_list):
    return {"Error": "Item not found"}
  
  if item.name != None:
    shopping_list[item_id].name = item.name

  if item.quantity != None:
    shopping_list[item_id].quantity = item.quantity

  if item.price != None:
    shopping_list[item_id].price = item.price  

  return shopping_list[item_id]

@app.delete("/delete-item/{item_id}", summary="Delete an item by ID", response_description="Confirmation message")
def delete_item(item_id: int = Path(description = "The ID of the item you want to update", ge = 0) ):
    """
    Example:
    - Request: DELETE /delete-item/0
    - Response: {"Message": "Item deleted successfully"}
    """

    if item_id < 0 or item_id >= len(shopping_list):
      return {"Error": "Item not found"}
    
    del shopping_list[item_id]
    return {"Message": "Item deleted successfully"}


