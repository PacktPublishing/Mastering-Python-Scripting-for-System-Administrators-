node ('slave1') {
  def compiled = true
  stage('Source') {
      cleanWs()
    //
      dir ('build') {
    echo "Source "
//    git 'https://github.com/beam2895/Mastering-Python-Scripting-for-System-Administrators-'
    checkout scm
      }
  }
      try{
    stage('Compile and test') {
    echo "Build stage"
//    sh 'python --version;sh "find build -iname '*.py''

    python_files = sh (
    script: " python -m compileall build ",
    returnStdout: true
).trim()
  }
      } catch(e) {
              compiled = false
 //         echo "python files== ${python_files}"
          ansiColor('vga') {
             echo '\033[42m\033[97mSome files are not compiles, see below error logs \033[0m'
                       echo e.toString()

          }

    if(compiled) {
        currentBuild.result = "SUCCESS"
    } else {
        currentBuild.result = "UNSTABLE"
    }

    }
    stage('Build') {
    sh 'tar -cvzf build.tgz build/'
  }
stage('Deploy') {
sshPublisher(publishers: [sshPublisherDesc(configName: 'staging', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '/tmp/', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'build.tgz')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
}

}
