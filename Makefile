# This is our project's Makefile

.PHONY: help
help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: install
install: install_python_dependency install_kafka ## Install all the dependencies

.PHONY: install_python_dependency
install_python_dependency:
	pip install -r requirements.txt

.PHONY: install_kafka
install_kafka:
	curl -O -J https://dlcdn.apache.org/kafka/3.2.1/kafka_2.13-3.2.1.tgz
	tar -xzf kafka_2.13-3.2.1.tgz

.PHONY: run
run: run_kafka run_app ## Bring up all the servers

.PHONY: run_kafka
run_kafka:
	xterm -e kafka_2.13-3.2.1/bin/zookeeper-server-start.sh kafka_2.13-3.2.1/config/zookeeper.properties &
	echo "Waiting for Zookeeper to start"
	sleep 10
	xterm -e kafka_2.13-3.2.1/bin/kafka-server-start.sh kafka_2.13-3.2.1/config/server.properties &
	echo "Waiting for Kafka Server to start"
	sleep 10

.PHONY: run_app
run_app:
	xterm -e python consumer_registration.py &
	xterm -e python  consumer_post.py &
	xterm -e python app.py &

.PHONY: clean
clean:
	rm kafka_2.13-3.2.1.tgz
	rm -R kafka_2.13-3.2.1
