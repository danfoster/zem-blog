---
title: Configuration Management Work Flows
category: sysadmin
tags: cfgman
---


# Code Review

Any changes to the configuration repo should be submitted as a patch / pull request to the staging branch. It should then be reviewed by another member of the team before being accepted. I personally find Githubs pull request system suitable.

# Continuous Integration

Continuous Integration (CI) testing can be applied at multiple stages, both for pull requests and for complete branches. The difficulty comes in to using CI to trigger appropriate tests.

It's very easy to trigger lint tests against your configuration to pick up syntax errors (e.g [Puppet Lint](http://puppet-lint.com/)). It would be
