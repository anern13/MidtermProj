pipeline {
  agent any
  stages {
    stage('step1 ') {
      steps {
        sleep 5
        echo 'step1'
      }
    }

    stage('step2') {
      steps {
        sleep 1
        echo 'step2'
      }
    }

    stage('') {
      steps {
        mail(subject: 'anern13@gmail.com', body: 'pipeline finished ', to: 'anern13@gmail.com')
      }
    }

  }
}