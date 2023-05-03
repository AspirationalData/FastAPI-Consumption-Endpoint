# FastAPI-Consumption-Endpoint
FastAPI endpoint through which the scraped data can be consumed

This API is self-documented, the API documentation will be automatically re-generated when the source file changes.

You'll be able to find the documentation by appending "/docs" to the base URL of the Web API.


## Endpoints

This API will have the following endpoints:

* **/group={query_group}**

    By using this endpoint, you'll be able to query the scraped products of the specified group.

    It has 3 possible values:

    * Men
    * Women
    * Children
    


* * **/item={query_item}**

    You'll be able to filter the results by querying the item type:

    * Shoes.


* **/filter**

    By using this endpoint, you can filter products based on a SKU value and minimun or maximum prices (no need to stricly set a range, you can just set "min_price" or "max_price" and it will work just fine).

    Example Queries:

    * **http://localhost:8000/filter?min_price=50**
    * **http://localhost:8000/filter?sku=FZ6161**
    * **http://localhost:8000/filter?min_price=10.0&max_price=50.0**
    * **http://localhost:8000/filter?sku=DEF&min_price=50.0**

## Ideas to Extend the API

* **Show all elements of the last breadcrumb.**

    Example:
    **Inicio / Originals / Calzado**

    In this example, it would only show elements from the "Calzado" group or "conglomerate".

* **Find out the most repeated color in a given product (or group)**

    Example on a given product:

    SKU: XXXXXX
    Colors: [White/Red, White/Blue, Grey, Purple]
    Most repeated color: White.