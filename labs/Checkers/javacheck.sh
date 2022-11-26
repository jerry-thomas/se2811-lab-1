#!/bin/bash

echo "This script should be run from a Git Bash shell."
# Run this script by typing ./javacheck.sh from your prompt.

echo "If this script prints ANY errors, please consult with your instructor."
echo "You could also try reinstalling Java. But do NOT simply create these" 
echo "files or edit this script."
echo ""
echo "There are other files needed for a proper installation beyond this short check."

echo
echo "Files confirmed present:"
ls 'C:\Users\'$(whoami)'\AppData\Local\SceneBuilder\SceneBuilder.exe'
ls 'C:\Program Files\Java\jdk-17.0.5\bin\java.exe'
ls 'C:\Program Files\Java\javafx-sdk-19\lib\javafx.fxml.jar'
