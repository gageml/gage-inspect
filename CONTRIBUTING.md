# Contributing to Gage Inspect

The following is a set of guidelines for contributing to Gage Inspect.

These guidelines are intended to make this project fun. If you're not
having fun as a result of a rule or procedure in this document, we'd
like to fix that.

## Code of Conduct

Take a moment to review our [Code of Conduct][conduct] before engaging
with the Gage Inspect community. The purpose of the Code of Conduct is
to support fairness and safety for everyone.

## Source code repository

The main Gage Inspect source code repository is hosted on GitHub at:

<https://github.com/gageml/gage-inspect>

Contributions should be made by submitting pull requests to this
repository.

## Contributions

Your positive engagement with the Gage Inspect community is our highest
priority. We are committed to making contributions as easy as possible.

Contributions generally fall into one of these categories:

- Bug report
- Feature request
- Fixes
- Help with features

We use these GitHub tools to facilitate contributions:

- [Discussions][discussions]
- [Issues][issues]
- [Pull requests][prs]

If you're not sure where to start, just [ask a question][discussions].

### Report a bug

If you see something that's broken, please report it by [opening a new
issue][issues]. If you happen to see an existing issue that describes
your issue, contribute to it by adding comments up upvotes (thumbs up).

Don't worry about creating duplicate issues. We'll sort that out later.

When reporting an issue, try to include this information:

- Summary of the problem
- Steps to reproduce

We don't use templates with detailed steps for reporting a bug. Just
tell us. If we need more information we'll ask.

### Request a feature

Gage Inspect is a community effort. Your ideas are central to its
effectiveness and ongoing improvement.

Use [project discussions][discussions] to present your idea. We'll work
to move your idea forward. If your submission lingers without feedback,
we apologize --- that's an oversight. We encourage you to "bump" a topic
if you feel it's not getting due attention.

Your idea can advance in different ways.

- The current software may already do what you want
- You might be able to solve your problem in a different way
- We may be planning a similar feature that you can help with
- The idea is promising but needs more work
- The idea is a good one but doesn't fit well with the current project
  scope or road map
- The idea results in one or more issues to be worked on

We will collaborate with you in good faith to move your idea forward to
a clear conclusion.

### Fix a bug

We encourage you to submit bug fixes.

We value your time and effort as a contributor and want you code to make
into future releases. It's frustrating to spend time fixing a bug only
to have your code rejected for petty reasons. We commit to making this
as easy as possible for both you and us.

Before spending time on a bug, take a moment to review this short
checklist.

- [ ] Is there an open issue that describes the bug? (see
      [Request a feature](#request-a-feature))
- [ ] Is the issue classified as a bug or is there otherwise agreement
      with the project maintainers that the issue needs to be fixed now?

Any documented feature in Gage Inspect that doesn't work as designed is
a bug and always meets the "needs to be fixed now" standard.

Reasons for rejecting a contribution:

- The fix is not for an agreed upon problem that needs to be fixed now
- We feel you are not working in good faith to address concerns we have
  about your contribution

Use the [GitHub pull request model][github-prs] to submit fixes.

Your pull request may need revision for any of these reasons:

- Incorrect implementation (code doesn't work as it should)
- Code that we feel would require controversial changes (i.e. changes
  that you might not agree with)
- Lack of acceptable tests

We will NOT delay merging your PR for these reasons:

- Code formatting
- Code style
- Easily correct errors (generally defined as errors that can be fixed
  without controversy)
- Easily added tests

Rather than present you with a series of change requests, we may move
your PR to a project branch and make the changes ourselves. For minor
changes or changes we feel are not controversial, we may merge our
changes directly without your input. For cases that we feel require your
input, we will defer merging until you've had a chance to review our
changes.

We will explain any changes we make so you know why we made them.

### Help with a feature

Feature development is different from bug fixes. Features address
yet-to-be-solved problems whereas bugs address existing-but-incorrect
solutions.

If you would like to contribute to a feature with the expectation that
it be included in future releases, review this checklist:

- [ ] Are we aware that you are working on a feature that you would like
      merged at some point?
- [ ] Is there some level of agreement with us that the feature is in
      scope and desirable for the project?
- [ ] Have you established a positive working relationship with the
      project maintainers, e.g. by submitting accepted bug fixes, etc.

We recognize that you may need to solve problems without taking the time
and effort to work with us. In this case, fork the project and make your
changes. This can be a path to merge later. It allows you to resolve any
issue to your satisfaction and later present us with a working solution.

We may decline to merge downstream changes for any of these reasons:

- The feature is not in scope for the project
- We feel the cost of maintaining the feature is too high (e.g. we lack
  the expertise or skill to fix issues, lack ready access to required
  software or systems, high defect rate, etc.)

## Conventions

This project is light on rules but we value consistency. That said, if
something isn't working as well as we'd like it to, we'll consider
changing it even in the face of well established convention.

Here's a list of some of our project conventions.

- Gage Inspect is a Python application and so uses the Python
  programming language for all core code --- we use "Pythonic"
  conventions and tooling unless there's a good reason not to
- Use [uv] for package related problems
- Use [pytest] for unit tests
- Project automation is implemented in the [justfile].
- Prefer functional programming idioms over imperative or object
  oriented
- Use Python classes for data structures only --- we avoid use of
  Python's class inheritance features
- Avoid styles and conventions that clash with those used by Inspect AI
  unless there's a good reason

## Documentation

Documentation is currently hosted at <https://gage.io/docs/api>. The
source code for Gage Inspect is currently in a private repository. This
will change in the near future. All Gage Inspect document will
eventually be located in this repository under `/docs` and will be
freely modifiable via contributions.

For the time being, if you need to change the Gage Inspect
documentation, please [open an issue][issues].

## Relationship to Inspect AI project

Generally speaking, Gage Inspect addresses issue that are out of scope
for Inspect AI. If Inspect AI provides a feature, we tend to use and
promote that feature rather than duplicate or replace it. That said,
there are cases where Gage Inspect provides alternative implementations
for some Inspect AI features.

In particular, Gage Inspect may release alternative solvers and scorers
according to our unique community needs.

We seek to insulate the Inspect AI from the needs of the Gage Inspect
community. While any Gage Inspect code is available to incorporate into
the core Inspect AI project, Gage Inspect requirements should not cause
pressure on Inspect AI maintainers to change Inspect AI.

For this reason we adopt a runtime patching strategy whereby we can
alter Inspect AI behavior without requiring changes to upstream code.

Patching is performed in [`gage_inspect.patch`][patch].

We may submit pull requests to Inspect AI for some changes, especially
bug fixes.

If you face an issue with Gage Inspect that can only be addressed by
modifying Inspect AI, we will work with you to apply a patch as needed
or otherwise find an approach that minimizes the burden on the Inspect
AI project.

## Semantic versioning and API stability

Gage Inspect uses [semantic versioning][semver]. As it has not reached
`1.0` its APIs are subject to change in ways that may break existing
code.

We make a good faith effort to maintain backward compatibility across
changes using interim deprecation strategies.

## Style

These notes apply to maintainers as well as external contributors.

Code should be free from individual style or idioms.

### Module names

The module names in Gage Inspect can be confusing. Some module names
start with an underscore `_` while others don't. Any module that appears
in user documentation must not contain an underscore `_`. All other
modules should contain an underscore to indicate they are private to the
project. A private module must be renamed if it appears in user
documentation.

Always use lower snake case when naming modules.

### Classes

Classes should be limited only to define data structures. They should
not define methods unless those methods relate to reading or writing
state.

Use higher order functions with function protocols (type definitions)
for extensibility rather than class inheritance.

### Function and variable names

Use lower snake case for all function and variable names. Use screaming
case case for all module constants.

Do not use screaming snake case for function level variables or class
attributes. Limit this style to module level constants.

In general, avoid using leading `_` for function and variable names.

Use Python's `__all__` export convention to denote functions and
constants that are intended for use from other modules.

Never use `_` (a single underscore) when the assigned value is later
referenced.

Names are among the most important considerations in good code. Initial
names are rarely the best names. We reserve the right to change names to
improve them. If we change a published function, we will try to maintain
backward compatibility for a number of releases by deprecating the old
functions.

### Git commit messages

Our commit rules are simple but strict.

- First line is the message title
  - Must begin with a capital letter
  - Must not exceed 50 chars
- Additional content
  - Must be separated from the title with a single blank line
  - No line may exceed 72 chars
- No line may contain trailing whitespace (tabs or spaces)

These rules are enforced by a local Git commit hook.

There are otherwise no rules governing commit message content. We are
not concerned with tags, labels, or other patterns that might be used by
automated tools.

You are free to make good faith mistakes in your commit message.

That said, commit messages present a unique opportunity to think about
what you're submitting and put those thoughts into words. This is a
powerful mental exercise that can cause you to rethink what you're about
to submit.

Here's an outline you might when writing your commit message.

- Title should be short and to the point
  - Fix for #12345
  - Add "Foo Bar" section to docs
  - First-pass implementation of Bar Foo feature
- Followup explanatory content is entirely optional --- we can see what
  your change is by looking at the diff --- BUT this is the stage where
  you can process your submission with a critical review
- Use bullets to identify the high points
- Call attention to weaknesses, compromises, areas for improvement,
  other future topics

Lean into the parts of your submission that you're not happy with. These
are emotional signals telling you there may be a breakthrough just
around the corner. It just needs a bit more work.

Consider this dynamic:

- You've just finished some work and are eager to memorialize it in a
  commit --- your effort presents a strong gravitational pull to be
  "done"
- You capture the highlights in your message
- No one likes to be critical of their own work, but as a matter of
  discipline, you to tick off the areas you're not totally happy with
- This process gets you thinking about some different approaches or what
  it might look like to address the weak points
- You realize the different approaches _might not be that much more
  work_ or could _dramatically simplify your submission_
- The gravitational pull of your effort compels you to just commit the
  code --- you're only seconds away from being done afterall!

If you know you have a good idea for improvement, consider making an
interim commit as checkpoint and then experimenting with your idea. This
is the point when code often goes from mediocre to good or from good to
great.

This is often how high quality code is written. You get something to
work and only then can you see the better path. If you settle for "it
works, just move on" you forego the payoff of your work leading to a
moment of clarity. You suffer by not realizing your potential and the
project suffers for never seeing the better code.

This is the power of commit messages. They give you a moment to
experience the tinges of regret that signal a good idea ahead.

Even so, you're free to type anything you like.

## Tests

Tests are maintained under [`/tests`][tests].

If you provide a fix, please include tests that show the fix works as
you intend.

If you feel the fix doesn't warrant tests, mention that in your pull
request. We may ask you to add tests, add tests ourselves, or agree that
the fix does not warrant tests.

Tests require the `dev` package option.

```shell
uv pip install -e .[dev]
```

To run tests, use the `test` [justfile] recipe.

```shell
just test
```

## Changes to this document

Please use [discussions] to submit ideas for improving this document.

<!-- Links -->

[conduct]: ./CONDUCT.md
[discussions]: https://github.com/gageml/gage-inspect/discussions
[issues]: https://github.com/gageml/gage-inspect/issues
[prs]: https://github.com/gageml/gage-inspect/pulls
[github-prs]:
  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
[pytest]: https://docs.pytest.org/en/stable/
[uv]: https://docs.astral.sh/uv/
[patch]: src/gage_inspect/patch.py
[semver]: https://semver.org/
[tests]: ./tests
[justfile]: ./justfile
