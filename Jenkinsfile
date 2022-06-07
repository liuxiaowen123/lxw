pipeline{
  agent any
  stages{
    stage("aip_auto"){
      steps{
        sh '''cd test_practice
        python3.8 test_skip.py'''
      }
    }
  }
}
