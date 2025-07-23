from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from io import BytesIO
from sklearn.ensemble import HistGradientBoostingRegressor

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="O arquivo precisa ser .xlsx")

    contents = await file.read();

    try:
        df = pd.read_excel(BytesIO(contents))
    except Exception as e:
      raise HTTPException(status_code=400, detail=f"Erro ao ler o arquivo: {str(e)}")

    model = HistGradientBoostingRegressor(l2_regularization=1.0, learning_rate=0.2, max_depth=30,max_iter=450, min_samples_leaf=5, random_state=42)

    predictions = model.predict(df)

    df['Predicted_Price'] = predictions

    return JSONResponse(content={"predictions": predictions.tolist()})
