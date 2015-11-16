#!/usr/bin/env python
# -*- coding: utf-8 -*-

SCRIPTNAME = 'squishRunSelectTestsbatch.py'

import os, sys, subprocess, time, datetime
import shutil
import argparse

sys.path.insert(0, './lib')
import config
import productinfo
import testsets
import filesystemutils

# sys.path.append('/local/StP/{}/Scripts/'.format(config.Major))
# import globals

SCRIPTNAME='squishRunSelectTests.py'

def sendemail(logfile,message):
    filesystemutils.logprint(logfile, 'sendemail', 'message to be sent: '+message, SCRIPTNAME)
    sendemail = u'{}/SquishTests/lib/sendEmail-v156/sendEmail.exe'.format(config.Root)
    arguments = [u'-t aav/qualitätssicherung', '-s outlook.wkd.wolterskluwer.de',\
     '-xu autotest@wolterskluwer.de',\
     '-xp Qualität2015!',
     '-a {}'.format(message)]
    subprocess.call([sendemail,arguments])

# g = globals.cls() 
SQUISHINSTALLATION = '{}/squish-6.0.0-qt54x-win32-msvc12/bin'.format(config.Root)
                    # '{}/Projekte/{}/QS/squish-6.0.0-qt55x-win32-msvc12/bin'.format(config.Branch)
                    # 'M:/Test/squish/{}/QS/squish-6.0.0-qt54x-win32-msvc12/bin'.format(config.Branch)
                    # '{}//squish-5.1-20150408-2009-qt54x-win32-msvc12/bin'.format(config.Root)
                    # '{}/squish-5.1-20150805-2352-qt54x-win32-msvc12/bin'.format(config.Root)
                    # 'M:/Test/Squish/squish-5.1-20150408-2009-qt54x-win32-msvc12/bin'
                    #  C:\local\TestSys\squish-5.1.1-qt53x-win32-msvc12\bin
# SQUISHINSTALLATION = os.getenv('SQUISH_PACKAGE')

def runTest(squishrunner, machinename, testsuite, testname, argsdebug, argsformat, argssendemail,\
            HOME, Major, Release, Revision,logfile,version='SSE'):
    fname = 'runTest' 

    print('starting '+fname)
    format = 'xml2.1'
    extension = 'xml'
    if argsformat == 'ascii':
        format = argsformat
        extension = 'txt'
    if argsformat == 'xls':
        format = argsformat
        extension = 'xls'

    os.environ['Major'] = str(Major)
    os.environ['Release'] = str(Release)
    os.environ['Revision'] = str(Revision)
    os.environ['SQUISH_LICENSEKEY_DIR'] = config.Root + 'SquishTests/setup/license'
    os.environ['SQUISH_USER_SETTINGS_DIR'] = config.Root + 'SquishTests/setup/ver1'

    HOME = config.Root+'SquishTests/'
    # create a dated filename for the logfile
    #LOGFILE = os.path.join(config.Logdir, 'resultsDatenTests-%s.%s'
    #                       % ( time.strftime('%Y-%m-%d-%H-%M'), extension) )
    LOGDIR = config.Logdir
 
    """   
    # os.path.join(config.Logdir, 'resultsDatenTests-%s.%s'
    #                        % ( time.strftime('%Y-%m-%d-%H-%M'), extension) )


    #subprocess.call([squishrunner, '--debugLog', argsdebug, '--testsuite',\
    #    os.path.join(HOME, testsuite),\
    #    '--testcase='+name,\
    #    '--resultdir='+'\\temp',\
    #    '--reportgen', '%s,%s' % (format,  LOGFILE)])
    #    '--exitCodeOnFail', '-1',
    #    '--interactive',
    #    '--reportgen', 'xls,%s' % LOGFILE])
    #    '--reportgen', 'stdout,%s' % LOGFILE])
    
    # this version works ok for the test suite mode
    #testlog = subprocess.check_output([squishrunner, '--debugLog', argsdebug, '--testsuite',\
    #    os.path.join(HOME, testsuite),\
    #    '--testcase='+name,\
    #    '--resultdir='+'results',\
    #    '--envvar Major=21',\
    #    '--envvar Release={}'.format(Release),\
    #    '--envvar Revision={}'.format(Revision),\
    #    '--reportgen', '%s,%s' % (format,  LOGFILE)])
    """
    try:
        """
        setupresult = subprocess.call([squishrunner, '--config', \
            'setGlobalScriptDirs', '{}/SquishTests/Global/shared'.format(config.Root)])
        setupresult = subprocess.call([squishrunner, '--config', \
            'setGlobalScriptDirs', '{}/SquishTests/Global/shared/SSE-Scripts'.format(config.Root)])
        setupresult = subprocess.call([squishrunner, '--config', \
            'setGlobalScriptDirs', '{}/SquishTests/Global/shared/HL-Scripts'.format(config.Root)])
        setupresult = subprocess.call([squishrunner, '--config', \
            'setGlobalScriptDirs', '{}/SquishTests/Global/shared/TM-Scripts'.format(config.Root)])
        setupresult = subprocess.call([squishrunner, '--config', \
            'setGlobalScriptDirs', '{}/SquishTests/Global/shared/QS-Scripts'.format(config.Root)])
        setupresult = subprocess.call([squishrunner, '--config', \
            'setGlobalScriptDirs', '{}/SquishTests/Global/shared'.format(config.Root),\
                '{}/SquishTests/Global/shared/SSE-Scripts'.format(config.Root)])
        print('first success')
        """
       
        if productinfo.startCenterVersion(machinename):
            setupresult = subprocess.check_output([squishrunner,  #  '--aut', 'StartCenter',\
                         '--config',\
                         'setGlobalScriptDirs', '{}/SquishTests/Global/shared, '.format(config.Root)+\
                         '{}/SquishTests/Global/shared/SSE-Scripts, '.format(config.Root)+\
                         '{}/SquishTests/Global/shared/HL-Scripts, '.format(config.Root)+\
                         '{}/SquishTests/Global/shared/TM-Scripts, '.format(config.Root)+\
                         '{}/SquishTests/Global/shared/QS-Scripts'.format(config.Root)])
        else:
            setupresult = subprocess.check_output([squishrunner,  # '--aut', 'SSE',\
                          '--config',\
                         'setGlobalScriptDirs', '{}/SquishTests/Global/shared, '.format(config.Root)+\
                         '{}/SquishTests/Global/shared/SSE-Scripts, '.format(config.Root)+\
                         '{}/SquishTests/Global/shared/HL-Scripts, '.format(config.Root)+\
                         '{}/SquishTests/Global/shared/TM-Scripts, '.format(config.Root)+\
                         '{}/SquishTests/Global/shared/QS-Scripts'.format(config.Root)])
        pass
    except:
        print(fname+': exception while setting squish global scripts dir '+ SCRIPTNAME)
        input()

    if machinename == None:
        return ''
    print(os.path.join(HOME, testsuite))
    testlog = 'No run completed, yet!'
    try:
        """ currently we test with batch files as AUT, which start the SSE directly, the
            logic used here does not work in this context"""
        if productinfo.startCenterVersion(machinename):
            print('found a startcenter program')
            testlog = subprocess.check_output([squishrunner, '--debugLog', argsdebug,'--testsuite',\
                os.path.join(HOME, testsuite),\
                '--testcase='+testname,\
                '--aut=StartCenter',\
                '--envvar AUT=StartCenter',\
                '--resultdir='+'results',\
                '--envvar Major={}'.format(Major),\
                '--envvar Release={}'.format(Release),\
                '--envvar Revision={}'.format(Revision),\
                '--envvar Version={}'.format(version),\
                '--envvars=envvars.txt',\
                '--reportgen', '%s,%s' % (format, logfile)])
        else:
            print('found a non startcenter program')
            print(os.getcwd())
            testlog = subprocess.check_output([squishrunner, '--debugLog', argsdebug,\
                '--testsuite='+os.path.join('./', testsuite),\
                '--testcase='+testname,\
                '--aut=SSE',\
                '--resultdir='+'results',\
                '--envvar AUT=SSE',\
                '--envvar Major={}'.format(Major),\
                '--envvar Release={}'.format(Release),\
                '--envvar Revision={}'.format(Revision),\
                '--envvar Version={}'.format(version),\
                '--envvars=envvars.txt',\
                '--reportgen', '%s,%s' % (format, logfile)])
    except subprocess.CalledProcessError as e:
        testlog = 'There was an exception during test execution: '+str(e)
    argssendemail = False
    if argssendemail:
        logfiles = sorted([f for f in os.listdir(LOGDIR)])
        log = logfiles[-1]
        if log != None:
            sendemail(logfile, testlog)

     #  '--exitCodeOnFail', '-1',
     #  '--interactive',
     #   '--reportgen', 'xls,%s' % LOGFILE])
     #   '--reportgen', 'stdout,%s' % LOGFILE])
    return testlog

    
def runTests(args):
    fname = 'runTests'
    global SQUISHINSTALLATION, SCRIPTNAME
    print('starting '+fname)
    print('args.format: ' + args.format )

    Major = args.Major # 21 # os.environ['Major']  # args.major
    Release = args.Release # os.environ['Release'] #
    revision = args.revision # os.environ['Revision'] # 

    if args.environment:
        if os.path.exists(os.getenv('SQUISH_PACKAGE')):
            SQUISHINSTALLATION = os.getenv('SQUISH_PACKAGE')
        else:
            print(SCRIPTNAME + ': -e given as option, but SQUISH_PACKAGE is not set in the environment!')

    # first we bring the 'local' up to date if so desired
    if args.update:
        print('first we start an update of the "local"!')
        # synchronous call
        subprocess.call(['python', '/local/Stp/{}/Scripts/localupdate.py'.format(Major)])
        #g.callBAT(['C:/local/Stp/21/Scripts/localUpdate.bat'])
        #exit

        # testSet = tinyTest

    #print('testbatch args.testset: ' + str(args.testset))
    # if args.testset == 'allTests':
    #    testSet=allTests
    #testSet = testsets.allTests
    #if args.testset == 'tinyTest':
    #    testSet = testsets.tinyTest
    #if args.testset == 'dataTest':
    #    testSet = testsets.dataTest
    #if args.testset == 'iconBarTest':
    #    testSet = testsets.iconBarTest

    # testSet = args.testset
    testSet = testsets.allTests

    print(SCRIPTNAME+': '+fname+' testsSet: '+ str(testSet))
    # testSet = testsets.iconBarTest

    testSuite = args.testsuite
    # ---- argument handling >  

    # here we set the home directory of the test suite
    if sys.platform.startswith('win'): # Windows
        HOME = config.Root+'/SquishTests/' #'M:/Test/squish' # Python understands Unix paths even on Windows
    elif sys.platform.startswith('darwin'): # Mac OS X
        HOME = '/Users/squish'
    else: # Other Unix-like, e.g. Linux
        HOME = '/home/squish'

    if args.debug:
        print(SCRIPTNAME+': '+fname+': HOME: ', HOME)
        #print(SCRIPTNAME+': '+fname+': SQUISHINSTALLATION: ', SQUISHINSTALLATION)
        print(SCRIPTNAME+': '+fname+': testSet: ', str(testSet)) 
        print(SCRIPTNAME+': '+fname+': '+'argsformat: '+args.format)

    if SQUISHINSTALLATION not in sys.path:
        sys.path.append(SQUISHINSTALLATION)

    # start the squishserver (and don't wait)
    if sys.platform.startswith('win'):
        squishserver = SQUISHINSTALLATION+ '/squishserver.exe'
        squishrunner = SQUISHINSTALLATION+ '/squishrunner.exe'
        # if args.verbose or args.debug: 
        print( SCRIPTNAME+': '+fname+': '+'squish server path: ' + squishserver)
        print( SCRIPTNAME+': '+fname+': '+'squish runner path: ' + squishrunner)
        os.environ['SQUISH_SCRIPT_DIR']='{}/SquishTests/Global/shared; '.format(config.Root)\
                                      + '{}/SquishTests/Global/shared/SSE-Scripts; '.format(config.Root)\
                                      + '{}/SquishTests/Global/shared/HL-Scripts; '.format(config.Root)\
                                      + '{}/SquishTests/Global/shared/QS-Scripts; '.format(config.Root)\
                                      + '{}/SquishTests/Global/shared/TM-Scripts; '.format(config.Root)

        pid = subprocess.Popen([squishserver]).pid
    else:
        pid = subprocess.Popen([squishserver]).pid

    print(SCRIPTNAME+': '+fname+': starting squishrunner with test suite ' + testSuite)
    # execute the test (and wait for it to finish)
    argsdebugargs = ''
    if args.debug:
        argsdebugargs = 'apw'

    # available test sets: allTests, tinyTest, dataTest
    # if args.debug:
    print(SCRIPTNAME+': '+fname+': testSet: ', str(testSet) )

    testlog = '----------\n'
    # now we iterate over the list of tests and call each one individually
    print(os.getcwd())
    for testname in testSet:
        print(SCRIPTNAME+': '+fname+': '+'testname: '+testname)
        testlog = testlog + str(runTest(squishrunner, args.Machinename, testSuite, testname, argsdebugargs, args.format, args.sendemail, 
                                        HOME, Major, Release, revision, args.log, args.version))
    print(SCRIPTNAME+' ----------------testlog: \n'+testlog)
    print(SCRIPTNAME+' ----------------testlog')
    #input()

    logfile = filesystemutils.createLogFile(str(args.Product).strip(), str(args.Machinename).strip(),'Squish')
    filesystemutils.logprint(logfile, 'main', testlog, SCRIPTNAME)

    print(SCRIPTNAME+': '+fname+': '+' stopping squish server')
    # stop the squishserver
    try:
        subprocess.call([squishserver, ' --stop'])
    except:
        print(SCRIPTNAME+': '+fname+': '+' failed to stop squish server')

    # first we kill spawned processes that might block access to the generated files
    if args.cleanup:
        subprocess.call(['python', 'killSpawnedProcesses.py'])

    # then we archive the generated files to a time-stamped directory
    indir = os.path.join(os.path.expanduser('~'),'Documents/Steuerfälle')
    outdir = '/temp/squishresults'+str(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))

    '''
    try: 
        os.mkdir(outdir)
    except:
        pass
    '''
    shutil.copytree(indir,outdir)

    # and finally we remove the generated files, so that we have a clean slate
    # for the next run and we won't get any confirmation dialogs for overwriting files
    if args.cleanup:
        subprocess.call(['python', 'deleteGeneratedFiles.py'])

    if testlog == None:
        testlog = 'No testlog generated'
    return testlog


if __name__ == "__main__":
    # --- < argument handling            
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cleanup', help='clean up after run (kill all spawned processes)',\
                        action='store_true')
    parser.add_argument('-d', '--debug', help='print debug info to C:/temp/debug.txt',\
                        action='store_true')
    parser.add_argument('-e', '--environment', help='take the value of SQUISH_PACKAGE from the environment',\
                        action='store_true')
    parser.add_argument('-f', '--format', help='specify the output format (xml, xls, ascii)',\
                        action='store', default='xml')
    parser.add_argument('-l', '--log', help='specify the log file',\
                        action='store')
    parser.add_argument('-m', '--Major', help='specify the major version to be tested',\
                        action='store', default='{}'.format(config.Major))
    parser.add_argument('-n', '--Machinename', help='specify the machine where the test is running',\
                        action='store')
    parser.add_argument('-p', '--Product', help='specify the product to be tested',\
                        action='store', default='{}'.format(config.Major))
    parser.add_argument('-R', '--Release', help='specify the release to be tested',\
                        action='store', default = 0)
    parser.add_argument('-r', '--revision', help='specify the revision version to be tested',\
                        action='store', default = 0)
    parser.add_argument('-s', '--testset', help='give a name of the test set to be run {allTests, tinyTest}',\
                        action='store', default=['tst_VersionCheck',])
    parser.add_argument('-se', '--sendemail', help='have the test results automatically mailed to the QA mailing list',\
                        action='store_true')
    parser.add_argument('-t', '--testsuite', help='give a name of the test suite to be run (the directory name relative to .)',\
                        action='store', default='suite_SSE')
    parser.add_argument('-u', '--update', help='update the \'local\' first',\
                        action='store_true')
    parser.add_argument('-v', '--verbose', help='print more info in the course of the script execution',\
                        action='store_true')
    parser.add_argument('-V', '--version', help='give the type of product to be tested (SSE, TM, QS)',\
                        action='store', default='SSE')
    args = parser.parse_args()
    runTests(args)
