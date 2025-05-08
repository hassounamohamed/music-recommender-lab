FROM python:3.8-slim
WORKDIR /app
COPY app.py music_recommender.joblib ./
RUN pip install fastapi uvicorn joblib scikit-learn
EXPOSE 5000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]