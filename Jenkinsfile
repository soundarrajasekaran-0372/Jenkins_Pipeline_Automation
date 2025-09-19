
pipeline {
    agent any
    
    options {
    	skipDefaultCheckout()
	disableConcurrentBuilds()
    	timeout(time: 20, unit: 'MINUTES')
    }

    stages {
        stage('Checkout the Code') {
            steps {
                git branch: 'main', url: 'https://github.com/soundarrajasekaran-0372/Docker-Multi-Container.git'
            }
        }

        stage('Build & Deploy Containers') {
            steps {
                script {
                    sh 'docker-compose down || true'
                    sh 'docker-compose up --build -d'
                }
            }
        }

        stage('Verify the Application') {
            steps {
                script {
                    echo "Waiting for containers to start..."
              	    sleep 5
                    echo "Testing App1..."
                    curl -v http://localhost:5001 || (docker logs $(docker ps -qf "name=app1") && exit 1)
                    echo "Testing App2..."
                    curl -v http://localhost:5002 || (docker logs $(docker ps -qf "name=app2") && exit 1)
                }
            }
        }

        stage('Install Nginx through Ansible') {
            steps {
                script {
                    sh 'ansible-playbook -i inventory.ini install_nginx.yml'
                }
            }
        }
    }
}

