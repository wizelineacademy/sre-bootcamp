#!/bin/bash

set -ex

cd auth_api || exit 1
mvn package
java -cp target/auth-api-1.0-SNAPSHOT-jar-with-dependencies.jar com.wizeline.App
