---
title: Writing Puppet Modules
category: sysadmin
tags: cfgman, puppet
---

Writing and testing puppet modules in a way that can easily be used by others can be confusing. Puppetlabs guide, (Beginner's Guide to Modules)[https://docs.puppetlabs.com/guides/module_guides/bgtm.html], is a good start. But doesn't go the full way. The following is my thought on writing puppet modules.

## Aim to publish your module.

From the start, you should aim to writing your module in such a way that it
could be published to the [Forge](http://forge.puppetlabs.com). This will force
you to follow best practises which, while having a steeper learning curve, will
produce much more maintainable code. You also get that extra fuzzy feeling that
you've helped others in the wider world.

To get started, use the following command to generate some boilerplate:

```
puppet module generate danfoster-mynewmodule
mv danfoster-mynewmodule mynewmodule
```

Note the format of the module name is that of `author-modulename` and then we
rename the directory to just contain the modulename. I've heard rumours that
this 2nd step won't be needed in future versions of puppet, but you'll have to
do it for now.

Some tips for writing a good module:

### Config / Code seperation

Your module should not have any site local configuration data in. Class
parameters should be put in a separate file (`params.pp`) with sensible
defaults where possible. The users of your module can then overwrite your
parameters in their class definition.



## Unit testing

Unit testing is important once your module had any sort of conditional logic in
it. It's best to start writing your unit tests from the start to ease the pain.

(RSpec)[http://rspec.info/) is the de facto testing tool for Ruby and
(rspec-puppet)[http://rspec-puppet.com/] provides a suite of test to run
against your puppet manifests. There is a still a significant amount of
boilerplate code that has to be written. Luckily Puppetlabs have created
(puppetlabs_spec_hlper)[https://github.com/puppetlabs/puppetlabs_spec_helper] to easy some of this pain. A good guide on using `puppet_spec_helper` can be found (here)[http://puppetlabs.com/blog/the-next-generation-of-puppet-module-testing].


## Acceptance Testing

### Testing workflow

While developing a module and/or tests, you probably don't want to be provisioning the VM every time. You also probably want to be able to get a shell on the test VM to see what's going on. You can do this by using the following workflow

. For the first time, provision the box and run the tests (but do not destroy the VM) by running: `BEAKER_destroy=no bundle exec rake beaker`
. For subsequent runs, run the tests using: BEAKER_destroy=no BEAKER_provision=no bundle exec rake beaker`
. If you want to SSH to the VM for diagnostic, run: `( cd .vagrant/beaker_vagrant_files/default.yml; vagrant ssh )`
