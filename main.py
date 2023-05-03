from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from typing import Optional


app = FastAPI()

dataset = pd.read_json("data_source/dataset.json")

# Downstream data cleaning:
dataset['Current Price'] = (dataset['Current Price']
                                .str.replace("€ ", "")
                                .str.replace(",", ".")
                                .astype("float")
                            )

dataset['Original Price'] = (dataset['Original Price']
                                .str.replace("€ ", "")
                                .str.replace(",", ".")
                                .astype("float")
                            )

dataset['Colors'] = (dataset["Colors"]
                        .map(lambda colors_list: [color.replace("Color del artículo: ", "") for color in colors_list])
                    )



@app.get("/")
async def root():
    return {"message": "Hello World"}


# Filter logic
@app.get("/filter")
async def filter_data(
    sku: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    filtered_data = dataset.copy()

    # Filter the DataFrame based on SKU exact value
    if sku:
        sku_filter = filtered_data['SKUs'].apply(lambda sku_array: sku.lower() in [sku_element.lower() for sku_element in sku_array])
        filtered_data = filtered_data.query('@sku_filter')

    # Filter the DataFrame based on the minimum and maximum price values
    if min_price is not None:
        filtered_data = filtered_data.query('(`Current Price` >= @min_price) | (`Original Price` >= @min_price)')
    if max_price is not None:
        filtered_data = filtered_data.query('(`Current Price` <= @max_price) | (`Original Price` <= @max_price)')

    # Convert the filtered data to a list of dictionaries
    filtered_data_dict = filtered_data.to_dict(orient='records')

    # Return the filtered data as a JSON response with proper encoding
    return JSONResponse(content=filtered_data_dict)