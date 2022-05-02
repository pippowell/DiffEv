# DiffEv

Repository for Crew C - Differential Evolution

## Git branch handling

Please always create sub-branches of your corresponding group branch for every new feature/function/bugfix you make: ```prog2/feature/nameOfFeature```

To do so, click on "create a new branch" in the corresponding task you're going to work on. That way, the branch is automatically linked to that task.

## 1. Project organization

To get a better sense of how your files should be organized, here's a simplified structure of our Python project:

```
DiffEv
├── docs
│   └── doc.md
├── task_name
│   ├── ...
├── tests
│   └── test_code.py
├── .gitignore
├── README.md
├── requirements.txt
├── pylintrc
├── .style.yapf
```

## 2. Developing

### 2.1 Prerequisites

TBD

### 2.2 Setting up Dev

```shell
git clone https://github.com/pippowell/DiffEv.git
cd DiffEv/
python install -r requirements.txt
```

### 2.3 Python Style Guide

We'll use the [Python Style Guide provided by Google](https://google.github.io/styleguide/pyguide.html). Code style will be checked using pylint and yapf via either pre-commit hooks or GitHub Actions after your commit.

While Python does encourage duck typing, please use [types](https://docs.python.org/3/library/typing.html) as much as possible, especially on function parameters, class constructors and so on. This will enable a more efficient teamwork and leads to less bugs due to `TypeErrors`.

### 2.4 Some Git rules

There are a set of rules to keep in mind:

- Perform work in a feature branch.

  _Why:_

  > Because this way all work is done in isolation on a dedicated branch rather than the main branch. It allows you to submit multiple pull requests without confusion. You can iterate without polluting the master branch with potentially unstable, unfinished code. [read more...](https://www.atlassian.com/git/tutorials/comparing-workflows#feature-branch-workflow)

- Never push into `main` branch. Make a Pull Request.

  _Why:_

  > It notifies team members that they have completed a feature. It also enables easy peer-review of the code and dedicates forum for discussing the proposed feature.

- Update your local development branch and do an interactive rebase before pushing your feature and making a Pull Request.

  _Why:_

  > Rebasing will merge in the requested branch (`main`) and apply the commits that you have made locally to the top of the history without creating a merge commit (assuming there were no conflicts). Resulting in a nice and clean history. [read more ...](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

- Resolve potential conflicts while rebasing and before making a Pull Request.
- Delete local and remote feature branches after merging.

  _Why:_

  > It will clutter up your list of branches with dead branches. It ensures you only ever merge the branch back into (`main`) once. Feature branches should only exist while the work is still in progress.

- Before making a Pull Request, make sure your feature branch builds successfully and passes all tests (including code style checks).

  _Why:_

  > You are about to add your code to a stable branch. If your feature-branch tests fail, there is a high chance that your destination branch build will fail too. Additionally, you need to apply code style check before making a Pull Request. It aids readability and reduces the chance of formatting fixes being mingled in with actual changes.

### 2.5 Git workflow

Because of most of the reasons above, we use [Feature-branch-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#feature-branch-workflow) with [Interactive Rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing) and some elements of [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows#gitflow-workflow) (naming and having a develop branch). The main steps are as follows:

- For a new project, initialize a git repository in the project directory. **For subsequent features/changes this step should be ignored**.

  ```sh
  cd <project directory>
  git init
  ```

- Checkout a new feature/bug-fix branch.
  ```sh
  git checkout -b <branchname>
  ```

- Make Changes.

  ```sh
  git add <file1> <file2> ...
  git commit
  ```

  _Why:_

  > `git add <file1> <file2> ...` - you should add only files that make up a small and coherent change.

  > `git commit` will start an editor which lets you separate the subject from the body.

  > Read more about it in _section 1.3_.

  _Tip:_

  > You could use `git add -p` instead, which will give you chance to review all of the introduced changes one by one, and decide whether to include them in the commit or not.

- Sync with remote to get changes you’ve missed.

  ```sh
  git checkout develop
  git pull
  ```

  _Why:_
  > This will give you a chance to deal with conflicts on your machine while rebasing (later) rather than creating a Pull Request that contains conflicts.
- Update your feature branch with latest changes from develop by interactive rebase.
  
  ```sh
  git checkout <branchname>
  git rebase -i --autosquash develop
  ```

  _Why:_
  > You can use --autosquash to squash all your commits to a single commit. Nobody wants many commits for a single feature in develop branch. [read more...](https://robots.thoughtbot.com/autosquashing-git-commits)
- If you don’t have conflicts, skip this step. If you have conflicts, [resolve them](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/) and continue rebase.
  
  ```sh
  git add <file1> <file2> ...
  git rebase --continue
  ```

- Push your branch. Rebase will change history, so you'll have to use `-f` to force changes into the remote branch. If someone else is working on your branch, use the less destructive `--force-with-lease`.
  
  ```sh
  git push -f(orce-with-lease)
  ```
  
  _Why:_
  > When you do a rebase, you are changing the history on your feature branch. As a result, Git will reject normal `git push`. Instead, you'll need to use the -f or --force flag. [read more...](https://developer.atlassian.com/blog/2015/04/force-with-lease/)
- Make a Pull Request.
- Pull request will be accepted, merged and closed by a reviewer.

### 2.6 Writing good commit messages

Having a good guideline for creating commits and sticking to it makes working with Git and collaborating with others a lot easier. Here are some rules of thumb ([source](https://chris.beams.io/posts/git-commit/#seven-rules)):

- Limit the subject line to 50 characters.
- Use [imperative mood](https://en.wikipedia.org/wiki/Imperative_mood) in the subject line.

  _Why:_

  > Rather than writing messages that say what a committer has done. It's better to consider these messages as the instructions for what is going to be done after the commit is applied on the repository. [read more...](https://news.ycombinator.com/item?id=2079612)

- Use the body to explain **what** and **why** as opposed to **how**.

## 3. Tests

TBD

Describe and show how to run the tests with code examples.
Explain what these tests test and why.

```shell
Give an example
```
