import pandas as pd
import numpy as np

ruta_csv = "ventas.csv"
df = pd.read_csv(ruta_csv)
df["total_venta"] = df["cantidad"] * df["precio_unitario"]

resumen_regional = (
    df.groupby("region")
      .agg(total_ventas=("total_venta", "sum"),
           transacciones=("total_venta", "count"),
           ticket_promedio=("total_venta", "mean"))
      .reset_index()
)

resumen_regional["ticket_promedio"] = resumen_regional["ticket_promedio"].round(2)

salida_csv = "resumen_regional.csv"
resumen_regional.to_csv(salida_csv, index=False)

print("Resumen regional generado en:", salida_csv)
print(resumen_regional)
