# Contributing To JobSeeker

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to JobSeeker and its packages, which are hosted in the [RedHat-Beyond](https://github.com/redhat-beyond) Organization on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

You are welcome to contact us through slack, with link #os-07-group4 on [beyond slack](redhat-beyond.slack.com).

#### Table Of Contents

- [Getting Started](#Getting-Started)
    - [New Contributor Guide](#New-Contributor-Guide)

- [Conventions](#Conventions)

- [Issues & PRs](#Issues--PRs)
    - [Issues](#Issues)
    - [Pull Requests (PRs)](#Pull-Requests-PRs)
 
## Getting Started

- To get an overview of the project, read the [README](README.md).
- Make sure you have all the [prerequisites](README.md#prerequisites) so you can contribute to this project.

### New Contributor Guide

Here are some resources to help you get started with open source contributions:

- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)

## Conventions

### Consider Starting The **Issue / Commit / PR Title** With An Applicable **Emoji**

These are the conventional emojis for our project:

Name|Emoji|Text Of Emoji To Provide|When To Use|
|:---:|:---:|:---|:---|
**FEATURE**|:rocket:|`:rocket:`|When working on a new feature.
**DOC**|:memo:|`:memo:`|When writing docs.
**BUG**|:bug:|`:bug:`|When fixing a bug.
**STRUCT**|:file_folder:|`:file_folder:`|When rearranging files for better structure or orientation.
**IMPROVE**|:horse_racing:|`:horse_racing:`|When improving performance of an existing feature.

The *"Text Of Emoji To Provide"* should be the first word in the title.

#### Examples

- The PR title of:
    ```
    :memo: Updating `README.md`'s Description
    ```
    Will look like this:
    ![](https://i.imgur.com/pNGetUm.png)

- The commit title of:
    ```
    :memo: Adding A `CONTRIBUTING.md` File
    ```
    Will look like this:
    ![](https://i.imgur.com/DfOnEPK.png)

## Issues & PRs

When contributing to this repository, please first discuss the change you wish to make via an issue.

### Issues

#### Create A New Issue
If you spot a problem with the docs, search if an issue already exists. If a related issue doesn't exist, you can open a new issue.

- #### Creating A New **Issue** That Contains **Many Tasks** Required To Be Done
  If that is the case, then consider making a separate *"checkbox"* for each task.

    #### Example
    The issue content of:
    ```
    We need to complete the following tasks to be able to make coffee:
      - [X] Buy coffee.
      - [ ] Buy milk.
      - [ ] Boil water.
    ```
    Will look like this:

    ![](https://i.imgur.com/zr3acoh.png)

#### Solve An Issue
Scan through our existing issues to find one that interests you. You can narrow down the search using labels as filters, or a specific word in the issue title. If you find an issue to work on, you are welcome to open a PR with a fix.


#### Commit Your Update

Commit the changes once you are happy with them.

Once your changes are ready, don't forget to self-review to speed up the review process :zap:.

### Pull Requests (PRs)

When you're finished with the changes, create a pull request, also known as a PR.

- Verify the PR is ready for Core Review, and please elaborate what actions needed.
- Enable the checkbox to [allow maintainer edits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork) so the branch can be updated for a merge.
- Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.
Once you submit your PR, a Docs team member will review your proposal. We may ask questions or request for additional information.
- We may ask for changes to be made before a PR can be merged, either using [suggested changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request) or pull request comments. You can apply suggested changes directly through the UI. You can make any other changes in your fork, then commit them to your branch.
- As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).
- If you run into any merge issues, checkout this [git tutorial](https://lab.github.com/githubtraining/managing-merge-conflicts) to help you resolve merge conflicts and other issues.
