# Rundeck JIRA Plugin

This project provides integration between Rundeck and JIRA. By using this workflowstep plugin
Rundeck will automatically add the execution link to a given JIRA Issue.

## Requirements

These plugins require the jira python library to be installed on the rundeck server.
For example, you can install it using `pip3 install jira`.

Further information here: [https://github.com/pycontribs/jira](https://github.com/pycontribs/jira).

## Install

Download the zipped version you like to install from [https://github.com/geraldhansen/rundeck-jira-plugin/tree/master/build/libs](https://github.com/geraldhansen/rundeck-jira-plugin/tree/master/build/libs)  
Use the Upload Plugin function from Rundeck and choose the downloaded zip file -> Install

## Job Configuration and Setup

This Plugin will use the rundeck key storage for the jira credentials.
If no JIRA issue is given nothing will happend, it depends on the job options to set the JIRA issue as
required or not.

## Build

Run `gradle build` to build the zip file. Then, copy the zip file to the `$RDECK_BASE\libext` folder.
Easy build without installing gradle and java by using the gradle docker container
`docker run --rm -u gradle -v "$PWD":/home/gradle/project -w /home/gradle/project gradle:4.10-jre8-alpine gradle build`  
If you build and there is a tag on the commit like "0.0.2" gradle will use this as version and you will find
in `build/libs/jira-plugin-0.0.2.zip` your version. If you build on a commit without tag the version number will
be increased and a suffix -SNAPSHOT will be appended.
