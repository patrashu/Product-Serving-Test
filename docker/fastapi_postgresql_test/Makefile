clean:
	docker stop fastapi_test
	docker stop postgres_db
	docker rm fastapi_test
	docker rm postgres_db
	docker rmi postgres:13
	docker rmi fastapi_test:latest
	docker volume rm fastapi_postgresql_test_test_volume
	docker volume rm fastapi_postgresql_test_test_volume_db
