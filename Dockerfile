FROM node:22-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt
COPY backend ./backend
COPY data ./data
COPY --from=frontend-build /app/frontend/dist ./dist
ENV PYTHONUNBUFFERED=1
EXPOSE 8080
CMD ["uvicorn","backend.app:app","--host","0.0.0.0","--port","8080"]
