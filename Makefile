install:
	cd frontend && npm install
	cd backend && pip install -r requirements.txt

dev-frontend:
	cd frontend && npm run dev

dev-backend:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

docker-up:
	docker compose -f docker/docker-compose.yml down

clean:
	cd frontend && rd /s /q node_modules
	cd backend && rd /s /q __pycache__