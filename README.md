# Shopping List API

![GitHub](https://img.shields.io/github/license/nicoleta7688/shopping-list-api)
![GitHub repo size](https://img.shields.io/github/repo-size/nicoleta7688/shopping-list-api)
![GitHub issues](https://img.shields.io/github/issues/nicoleta7688/shopping-list-api)
![GitHub pull requests](https://img.shields.io/github/issues-pr/nicoleta7688/shopping-list-api)

This repository contains the source code for a RESTful API designed to manage a shopping list. The API allows users to perform CRUD operations (Create, Read, Update, Delete) on shopping items.

## Features

- **Add Item**: Add a new item to the shopping list.
- **View List**: View the entire shopping list.
- **View Item by ID**: View a specific item by its unique identifier.
- **Get Items by Name**: Get a list of shopping items that match a given name.
- **Update Item by ID**: Update an existing item in the shopping list.
- **Delete Item by ID**: Delete an item from the shopping list.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/): FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- [Pydantic](https://pydantic-docs.helpmanual.io/): Pydantic is a data validation and settings management library.
- [Python](https://www.python.org/): The programming language used to build the API.

## Usage

1. **Clone the repository**: git clone https://github.com/your-username/shopping-list-api.git
2. **Install the dependencies**: pip install -r requirements.txt
3. **Run the API**: uvicorn main:app --reload

The API will be available at http://localhost:8000.

## Documentation

The API documentation can be accessed by navigating to http://localhost:8000/docs or http://localhost:8000/redoc in your browser.
