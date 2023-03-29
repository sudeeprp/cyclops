# Cyclops

Complexity in product code goes up in increments. Simple code keeps getting enhanced, eventually becoming hard-to-read and hard-to-test.

Limiting the cyclomatic complexity per function is one way to keep things simple.

However, what if your code already has high complexity? How do we limit it then?
This tool, along with [lizard](https://github.com/terryyin/lizard) helps in limiting complexity in newly written functions, while preventing existing functions from increasing their complexity.

## Installation and setup

Install lizard using one of the methods described in https://github.com/terryyin/lizard/blob/master/README.rst

Setup the baseline by running

`lizard <source-code-folder> -o baseline.csv`

## Check complexity growth

After a period of development, run lizard again to measure complexity

`lizard <source-code-folder> -o updated.csv`

Compare per-function complexity using Cyclops

`python .\comparecyclo.py 4 updated.csv baseline.csv`

The tool reports any new functions with a cyclomatic complexity > 4, along with existing functions whose complexity has increased. And provides a non-zero exit code.
