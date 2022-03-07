# Flake8

*Flake8* is a CI tool that checks the code written in python.
> For example, it checks that the max-line-length is below 120
characters.

## Our Project Supports *Flake8*

### How To Use *Flake8* Along Your Code

In the root folder of the project, once you have run the commands:
```sh
vagrant up
vagrant ssh
cd /vagrant
```
you may run *Flake8* and review your code,
by running the command:
```sh
pipenv run flake8 --max-line-length 120
```

## Support For Github's PRs By CI With *Flake8*
When contributing a PR, Github will now review the code in it
with *Flake8*, and will print the results of it.

#### **ATTENTION:**
We have setup branch-protection for the `main` branch, by asserting that
every PR to the `main` branch must be approved by the *Flake8* tool.
> NOTE: That means, no one would be able to `push` changes to the `main` branch without requesting an official PR.
