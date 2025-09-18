
pipeline {
    agent any
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
                    sh 'curl -f http://localhost:5001 || exit 1'
                    sh 'curl -f http://localhost:5002 || exit 1'
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

