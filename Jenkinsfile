node ('slave1') {
  def compiled = true
  stage('Source') {
      cleanWs()
      dir ('build') {
    echo "Source "
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
sshPublisher(publishers:
    [sshPublisherDesc(configName: 'staging', transfers:
        [sshTransfer(cleanRemote: false, excludes: '',
        execCommand: "[ -d /var/lib/py_scripts/build ] && mv /var/lib/py_scripts/build /var/lib/py_scripts/build_bkp_${BUILD_TAG}; tar -xvzf /var/lib/py_scripts/build.tgz -C /var/lib/py_scripts/",
        execTimeout: 120000,
        flatten: false,
        makeEmptyDirs: false,
        noDefaultExcludes: false,
        patternSeparator: '[, ]+',
        remoteDirectory: '',
        remoteDirectorySDF: false,
        removePrefix: '',
        sourceFiles: 'build.tgz')],
        usePromotionTimestamp: false,
        useWorkspaceInPromotion: false,
        verbose: true)])

    if (env.BRANCH_NAME == "master") {
        echo "master branch detected, deploying on production too"

    sshPublisher(publishers:
    [sshPublisherDesc(configName: 'production', transfers:
        [sshTransfer(cleanRemote: false, excludes: '',
        execCommand: "[ -d /var/lib/py_scripts/build ] && mv /var/lib/py_scripts/build /var/lib/py_scripts/build_bkp_${BUILD_TAG}; tar -xvzf /var/lib/py_scripts/build.tgz -C /var/lib/py_scripts/",
        execTimeout: 120000,
        flatten: false,
        makeEmptyDirs: false,
        noDefaultExcludes: false,
        patternSeparator: '[, ]+',
        remoteDirectory: '',
        remoteDirectorySDF: false,
        removePrefix: '',
        sourceFiles: 'build.tgz')],
        usePromotionTimestamp: false,
        useWorkspaceInPromotion: false,
        verbose: true)])


      }

  }
}
