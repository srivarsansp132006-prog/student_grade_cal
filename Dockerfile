
FROM python:3.10-slim

WORKDIR /app

COPY student_grade_calculator.py .

CMD ["python3", "student_grade_calculator.py"]
