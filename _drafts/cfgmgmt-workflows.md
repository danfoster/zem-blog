---
title: Configuration Management Work Flows
category: sysadmin
tags: cfgman
---

Configuration management tools make it very easy to configure a large number of
servers easily. It also means it's very easy to break a large number of servers
in one go. To minimise the latter it's important to have a robust work flow to
your configuration changes to be able to prevent as many negative changes from
hitting production as possible.

Over time I came to the realisation that another area has already solved many of these challenges: ``software development''. By treating configuration the same as developers treat their code base, we can hopefully stamp out any bugs before our configuration hits production services.

Below are some paradigms taken from software development that believe work well for configuration management.

# Code Review

Any changes to the configuration repo should be submitted as a patch / pull request to the staging branch. It should then be reviewed by another member of the team before being accepted. I personally find Githubs pull request system suitable.

# Continuous Integration

Continuous Integration (CI) testing can be applied at multiple stages, both for pull requests and for complete branches. The difficulty comes in to using CI to trigger appropriate tests.

It's very easy to trigger lint tests against your configuration to pick up syntax errors (e.g [Puppet Lint](http://puppet-lint.com/)). It would be
