from typing import Any, Dict

import requests

def predict(url: str, employe_info: Dict[str, Any]) -> dict:
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=employe_info, headers=headers)
    result = response.json()
    if result["prediction"] == 1:
        print("El empleado renunciará a la empresa.")
    else:
        print("El empleado no renunciará a la empresa.")
    return result


if __name__ == "__main__":
    # URL del modelo
    url = "http://127.0.0.1:5000/predict"

    # Información del empleado a predecir
    info = {
        "Age": 41, "BusinessTravel": "Travel_Rarely", "DailyRate": 1102,
        "Department": "Sales", "DistanceFromHome": 1, "Education": 2,
        "EducationField": "Life Sciences", "EmployeeCount": 1, "EmployeeNumber": 1,
        "EnvironmentSatisfaction": 2, "Gender": "Female", "HourlyRate": 94,
        "JobInvolvement": 3, "JobLevel": 2, "JobRole": "Sales Executive",
        "JobSatisfaction": 4, "MaritalStatus": "Single", "MonthlyIncome": 5993,
        "MonthlyRate": 19479, "NumCompaniesWorked": 8, "Over18": "Y",
        "OverTime": "Yes", "PercentSalaryHike": 11, "PerformanceRating": 3,
        "RelationshipSatisfaction": 1, "StandardHours": 80, "StockOptionLevel": 0,
        "TotalWorkingYears": 8, "TrainingTimesLastYear": 0, "WorkLifeBalance": 1,
        "YearsAtCompany": 6, "YearsInCurrentRole": 4, "YearsSinceLastPromotion": 0,
        "YearsWithCurrManager": 5
    }
    result = predict(url, info)
    print(result)