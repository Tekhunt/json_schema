# Description

This project reads a json file, sniffs the schema and dumps the result in a folder `/schema`

I created a class called `JsonOps` which has three methods each having a single responsibility(S in SOLID Principles).

## load_file Method

This method loads the json file and extracts the required contents

## sniff_schema Method

This method checks for some conditions and sniffs the schema of the data accordingly

## save_to_folder Method

This method saves the json schema into a folder in the working directory
