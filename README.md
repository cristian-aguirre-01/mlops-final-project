## MLOps Introduction: Final Project
FInal work description in the [final_project_description.md](final_project_description.md) file.

Student info:
- Full name: Cristian Fernando Aguirre Janampa
- e-mail: caguirrej@uni.pe
- Grupo: 2

## Project Name: Predicción de Rotación de Empleados (Employee Attrition)

Este proyecto tiene como finalidad desarrollar un modelo de Machine Learning capaz de predecir la probabilidad de que un 
empleado abandone la empresa.
La rotación de personal representa un costo significativo para las organizaciones debido a gastos de reclutamiento, 
capacitación y pérdida de conocimiento interno.
Mediante el uso de técnicas de análisis de datos y aprendizaje automático, se busca identificar patrones asociados 
a la salida de empleados y generar predicciones que permitan a la empresa tomar decisiones preventivas.


### Identificación del Problema
Muchas empresas no cuentan con herramientas analíticas que les permitan anticipar la renuncia de sus empleados.
La falta de predicción genera:
- Costos elevados de reemplazo.
- Disminución de productividad.
- Pérdida de talento estratégico.
- Impacto negativo en clima laboral.
El problema central es que las decisiones se toman de forma reactiva y no preventiva.

### Objetivo de Negocio
El objetivo de negocio consiste en reducir la rotación de empleados mediante la identificación temprana de perfiles con 
alta probabilidad de abandono.

### Objetivo Analítico
Desarrollar un modelo de clasificación supervisada que permita:
- Predecir si un empleado abandonará la empresa (Attrition = Yes/No).
- Identificar las variables más influyentes en la rotación.
- Obtener métricas de desempeño confiables (Accuracy, Recall, F1-Score, ROC-AUC).
- Implementar un pipeline reproducible de entrenamiento y desplegado como servicio (enfocado a MLOps).

### Descripción del Dataset

**Nombre del Dataset**

*IBM HR Analytics – Employee Attrition & Performance*

Referencia: https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset

- De 1470 registros
- 35 características
- 2 Clases - Target (Attrition = Yes/No)


| Variable                 | Significado                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Age                      | Edad del empleado en años.                                                                                           |
| Attrition                | Indica si el empleado dejó la empresa. Valores: `Yes`, `No`. **Variable objetivo.**                                  |
| BusinessTravel           | Frecuencia de viajes laborales. Valores: `Non-Travel`, `Travel_Rarely`, `Travel_Frequently`.                         |
| DailyRate                | Tarifa o ingreso diario del empleado.                                                                                |
| Department               | Departamento donde trabaja. Valores: `Sales`, `Research & Development`, `Human Resources`.                           |
| DistanceFromHome         | Distancia desde el hogar al trabajo (en millas).                                                                     |
| Education                | Nivel educativo. Valores: `1=Below College`, `2=College`, `3=Bachelor`, `4=Master`, `5=Doctor`.                      |
| EducationField           | Campo de estudio. Ejemplos: `Life Sciences`, `Medical`, `Marketing`, `Technical Degree`, `Human Resources`, `Other`. |
| EmployeeCount            | Número de empleados (constante = 1 en todo el dataset, no aporta información).                                       |
| EmployeeNumber           | Identificador único del empleado.                                                                                    |
| EnvironmentSatisfaction  | Nivel de satisfacción con el ambiente laboral. Escala `1–4` (1=Bajo, 4=Alto).                                        |
| Gender                   | Género del empleado. Valores: `Male`, `Female`.                                                                      |
| HourlyRate               | Tarifa o ingreso por hora.                                                                                           |
| JobInvolvement           | Nivel de involucramiento con el trabajo. Escala `1–4`.                                                               |
| JobLevel                 | Nivel jerárquico dentro de la empresa. Valores `1–5`.                                                                |
| JobRole                  | Rol del empleado. Ejemplos: `Sales Executive`, `Research Scientist`, `Laboratory Technician`, `Manager`, etc.        |
| JobSatisfaction          | Nivel de satisfacción laboral. Escala `1–4`.                                                                         |
| MaritalStatus            | Estado civil. Valores: `Single`, `Married`, `Divorced`.                                                              |
| MonthlyIncome            | Ingreso mensual del empleado.                                                                                        |
| MonthlyRate              | Tarifa mensual interna asignada al empleado.                                                                         |
| NumCompaniesWorked       | Número de empresas en las que ha trabajado previamente.                                                              |
| Over18                   | Indica si es mayor de 18 años. Valores: `Y` (constante en dataset).                                                  |
| OverTime                 | Indica si realiza horas extra. Valores: `Yes`, `No`.                                                                 |
| PercentSalaryHike        | Porcentaje de incremento salarial reciente.                                                                          |
| PerformanceRating        | Calificación de desempeño. Valores comunes: `3` o `4`.                                                               |
| RelationshipSatisfaction | Nivel de satisfacción con relaciones laborales. Escala `1–4`.                                                        |
| StandardHours            | Horas estándar de trabajo (constante = 80).                                                                          |
| StockOptionLevel         | Nivel de opciones de acciones asignadas. Valores `0–3`.                                                              |
| TotalWorkingYears        | Total de años de experiencia laboral.                                                                                |
| TrainingTimesLastYear    | Número de capacitaciones recibidas el último año.                                                                    |
| WorkLifeBalance          | Balance entre trabajo y vida personal. Escala `1–4`.                                                                 |
| YearsAtCompany           | Años trabajando en la empresa actual.                                                                                |
| YearsInCurrentRole       | Años en el rol actual dentro de la empresa.                                                                          |
| YearsSinceLastPromotion  | Años desde la última promoción.                                                                                      |
| YearsWithCurrManager     | Años trabajando con el gerente actual.                                                                               |



