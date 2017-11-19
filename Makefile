docker:
	docker build -f Dockerfile -t ionavincent/riverfordscraper .
docker-push: docker
	docker push ionavincent/riverfordscraper