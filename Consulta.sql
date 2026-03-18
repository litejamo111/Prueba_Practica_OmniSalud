USE prueba_tecnica;
SELECT
  region,
  SUM(cantidad * precio_unitario) AS total_ventas,
  COUNT(*) AS transacciones,
  AVG(cantidad * precio_unitario) AS ticket_promedio
FROM ventas
GROUP BY region
ORDER BY region;
