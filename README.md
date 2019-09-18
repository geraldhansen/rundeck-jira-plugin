# Rundeck JIRA Plugin

This project provides integration between Rundeck and JIRA. By using this workflowstep plugin
Rundeck will automatically add the execution link to a given JIRA Issue.

## Requirements

These plugins require the jira python library to be installed on the rundeck server.
For example, you can install it using `pip3 install jira`.

Further information here: [https://github.com/pycontribs/jira](https://github.com/pycontribs/jira).

## Build and Install

Run `gradle build` to build the zip file. Then, copy the zip file to the `$RDECK_BASE\libext` folder.
Easy build without installing gradle and java by using the gradle docker container
`docker run --rm -u gradle -v "$PWD":/home/gradle/project -w /home/gradle/project gradle:4.10-jre8-alpine gradle build`

## Job Configuration and Setup

This Plugin will use the rundeck key storage for the jira credentials.
If no JIRA issue is given nothing will happend, it depends on the job options to set the JIRA issue as
required or not.
