# Contributing to CipherX

Welcome! CipherX is a community project that aims to work for a wide range of Python users and codebases. If you're trying CipherX on your Python code, your experience and what you can contribute are important to the project's success.

## Code of Conduct

Everyone participating in the CipherX community, and in particular our issue tracker and pull requests, is expected to treat other people with respect and more generally to follow the guidelines articulated in the [Python Community Code of Conduct](https://www.python.org/psf/conduct/).

## Non-code contributions

Even if you don't feel ready or able to contribute code, you can still help out. There are always things that can be improved on the documentation (even just proof reading, or telling us if a section isn't clear enough). Maybe you can propose general examples for the documentation?

## Reporting bugs and issues

If you've run into behaviour in CipherX that you don't understand, or you're having trouble working out a good way to apply it to your code, or you've found a bug or would like a feature it doesn't have, we want to hear from you!

Our forum for discussion is the project's [GitHub issue tracker](https://github.com/aceking007/CipherX/issues). This is the right place to start a discussion of any of the above or most any other topic concerning the project.

## Submitting Code

Even more excellent than a good bug report is a fix for a bug, or the implementation of a much needed new feature. *We'd love to have your contributions*.

If your new feature will be a lot of work, we recommend talking to us early -- [see below](#preparing-changes).

We use the usual GitHub pull-request flow, which may be familiar to you if you've contributed to other projects on GitHub. For the mechanics, see [GitHub's own documentation](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests).

## Preparing Changes

Before you begin: if your change will be a significant amount of work to write, we highly recommend starting by opening an issue laying out what you want to do. That lets a conversation happen early in case other contributors disagree with what you'd like to do or have ideas that will help you do it.

The best pull requests are focused, clearly describe what they're for and why they're correct, and contain tests for whatever changes they make to the code's behaviour. As a bonus these are easiest for someone to review, which helps your pull request get merged quickly! Standard advice about good pull requests for open-source projects applies.

Also, do not squash your commits after you have submitted a pull request, as this erases context during review. We will squash commits when the pull request is merged.

## Coding Conventions

Follow the coding conventions specified in [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/). The important highlights are:
- Classes should be AllFirstLetterUppercase style.
- Functions should be in lowecase_separated_by_underscores style.
- Variables are either in lowecase_separated_by_underscores or lowercasemungedtogether style, depending on your preferences and the length of the variable.
- _single_leading_underscores to indicate internal functions or classes that shouldn't be called directly by a user.
- Tabs are bad. Most people in the Python community now dislike tabs and instead prefer using 4 spaces for indentation. Most editors can help you take care of this.
- Documentation is important, use the PEP 257 as a guide for adding docstrings in appropriate places.
- Modules, classes and function documentation should start with a one line description. This must end with a period.
- Additionally, you should add tests for any code that you write using the pytest module.

Here's an example of a module along with the proper documentation:

```python
"""This is a one line description of the module followed with a period.

More information about the module and its goals and usage.
"""

class MyClass:
    """One line description fo the class followed by a period.

    More information about the class -- its purpose, usage, and implementation.
    """

    def my_function(self, spam):
      """A terse description of my function followed with a period.

      A longer description with all kinds of additional goodies. This may include information about what the function does, along with what parameters it will be passed and what it returns. You know, information so people know how to use the function.
      """

      # the code...
```

## Core Developer Guidelines

Core developers should follow these rules when processing pull requests:
- Always wait for tests to pass before merging PRs (tests using GitHub workflows, if any).
- Additionally, carry out the tests for the PRs using `coverage` and `pytest` modules.
- Use "[Squash and merge](https://github.blog/2016-04-01-squash-your-commits/)" to merge PRs.
- Delete branches for merged PRs (by core devs pushing to the main repo).
- Edit the final commit message before merging to conform to the following style (we wish to have a clean `git log` output):
  - When merging a multi-commit PR make sure that the commit message doesn't contain the local history from the committer and the review history from the PR. Edit the message to only describe the end state of the PR.
  - Make sure there is a single newline at the end of the commit message. This way there is a single empty line between commits in `git log` output.
  - Split lines as needed so that the maximum line length of the commit message is under 80 characters, including the subject line.
  - Capitalize the subject and each paragraph.
  - Make sure that the subject of the commit message has no trailing dot.
  - If the PR fixes an issue, make sure something like "Fixes #xxx" occurs in the body of the message (not in the subject).
  - The subject should start with one of the following tags
    - `feat` - Addition of a new feature
    - `fix` - Bug fixes
    - `perf` - Performance improvements
    - `refactor` - Code refactorization
    - `doc` - Improvements or revisions in documentation
    - `chore` - A side job that needed to be done  
    A subject line for the commit should look like this:  
    `feat: Added Feature X` or `chore: Initial commit`
  - Use markdown for formatting

## Issue-tracker conventions

We aim to reply to all new issues promptly. We'll assign a milestone to help us track which issues we intend to get to when, and may apply labels to carry some other information. Here's what our milestones and labels mean.

### Task priority and sizing

We use GitHub "labels" ([see our list](https://github.com/aceking007/CipherX/labels)) to roughly order what we want to do soon and less soon. There's two dimensions taken into account: **priority** (does it matter to our users) and **size** (how long will it take to complete).

Bugs that aren't a huge deal but do matter to users and don't seem like a lot of work to fix generally will be dealt with sooner; things that will take longer may go further out.

WE are trying to keep the backlog at a manageable size, an issue that is unlikely to be acted upon in foreseeable future is going to be respectfully closed. This doesn't mean the issue is not important, but rather reflects the limits of the team.

The **question** label is for issue threads where a user is asking a question but it isn't yet clear that it represents something to actually change. We use the issue tracker as the preferred venue for such questions, even when they aren't literally issues, to keep down the number of distinct discussion venues anyone needs to track. These might evolve into a bug or feature request.

Issues **without a priority or size** haven't been triaged. We aim to triage all new issues promptly, but there maybe some issues that we haven't yet reviewed since adopting these conventions.

### Other labels

- **needs discussion**: This issue needs agreement on some kind of design before it makes sense to implement it, and it either doesn't yet have a design or doesn't yet have agreement on one.
- **feature, bug, crash, refactoring, documentation**: These classify the user-facing impact of the change. Specifically "refactoring" means there should be no user-facing effect.
- **topic**: labels group issues touching a similar aspect of the project, for example PEP 484 compatibility, a specific command-line option or dependency.

### References and Sources for the document:
- [mypy Contribution Guidelines](https://github.com/python/mypy/blob/master/CONTRIBUTING.md)
- [Contributing to Biopython](https://biopython.org/wiki/Contributing)
