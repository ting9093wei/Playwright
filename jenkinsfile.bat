pipeline {
    agent any

    stages {
        stage('Run Playwright Tests') {
            steps {
                dir('C:\\Users\\ting9\\OneDrive\\Desktop\\Playwright\\pytest') {
                    bat 'pytest --html=result\\report.html'
                }
            }
        }

        stage('Send Email') {
            steps {
                emailext(
                    to: 'ting9093wei@gmail.com',
                    subject: 'Playwright Test Report',
                    body: 'Playwright 測試已完成，請查收附加的 HTML 報告。',
                    attachmentsPattern: 'report.html',
                    attachLog: false
                )
            }
        }
    }
}
